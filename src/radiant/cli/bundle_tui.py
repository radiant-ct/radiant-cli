"""
radiant/cli/bundle_tui.py

Full Textual TUI for `radiant bundle add`.
Run standalone for development: python bundle_tui.py
"""

from __future__ import annotations
from typing import Any

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.reactive import reactive
from textual.screen import Screen, ModalScreen
from textual.widgets import (
    Button, Checkbox, DataTable, Footer, Header,
    Input, Label, ListItem, ListView, Pretty,
    Static, Switch, TabbedContent, TabPane,
)
from textual.widget import Widget

# ─────────────────────────────────────────────────────────────────────────────
# Field definitions (same as bundle.py — keep in sync or import from there)
# ─────────────────────────────────────────────────────────────────────────────

CATEGORICAL_FIELDS: list[tuple[str, str, str]] = [
    # (label,                ImageFilter snake attr,  camelCase key)
    ("Sex",                  "sex",                   "sex"),
    ("Convolution Kernel",   "convolution_kernel",    "convolutionKernel"),
    ("Manufacturer",         "manufacturer",          "manufacturer"),
    ("Manufacturer Model",   "manufacturer_model",    "manufacturerModel"),
    ("Software Version",     "software_version",      "softwareVersion"),
]

RANGE_FIELDS: list[tuple[str, str, type]] = [
    # (label,                          base attr,                                        type)
    ("Age (years)",                    "age_years",                                      int),
    ("Study Date (YYYY-MM-DD)",        "study_date",                                     str),
    ("KVP",                            "kvp",                                            float),
    ("Exposure mAs",                   "exposure_mas",                                   float),
    ("Slice Thickness (mm)",           "slice_thickness_mm",                             float),
    ("Pixel Spacing (mm)",             "pixel_spacing_mm",                               float),
    ("Rows",                           "rows",                                           int),
    ("Columns",                        "columns",                                        int),
    ("N Slices",                       "n_slices",                                       int),
    # Shape
    ("Shape Mesh Volume",              "shape_mesh_volume",                              float),
    ("Shape Voxel Volume",             "shape_voxel_volume",                             float),
    ("Shape Surface Area",             "shape_surface_area",                             float),
    ("Shape Sphericity",               "shape_sphericity",                               float),
    ("Shape Compactness 1",            "shape_compactness_1",                            float),
    ("Shape Compactness 2",            "shape_compactness_2",                            float),
    ("Shape Max 3D Diameter",          "shape_maximum_3_d_diameter",                     float),
    ("Shape Major Axis Length",        "shape_major_axis_length",                        float),
    ("Shape Minor Axis Length",        "shape_minor_axis_length",                        float),
    ("Shape Least Axis Length",        "shape_least_axis_length",                        float),
    ("Shape Elongation",               "shape_elongation",                               float),
    ("Shape Flatness",                 "shape_flatness",                                 float),
    # First order
    ("First Energy",                   "first_energy",                                   float),
    ("First Total Energy",             "first_total_energy",                             float),
    ("First Entropy",                  "first_entropy",                                  float),
    ("First Minimum",                  "first_minimum",                                  float),
    ("First 10th Percentile",          "first_10_th_percentile",                         float),
    ("First 90th Percentile",          "first_90_th_percentile",                         float),
    ("First Maximum",                  "first_maximum",                                  float),
    ("First Mean",                     "first_mean",                                     float),
    ("First Median",                   "first_median",                                   float),
    ("First IQR",                      "first_interquartile_range",                      float),
    ("First Range",                    "first_range",                                    float),
    ("First Mean Abs Deviation",       "first_mean_absolute_deviation",                  float),
    ("First Robust MAD",               "first_robust_mean_absolute_deviation",           float),
    ("First RMS",                      "first_root_mean_squared",                        float),
    ("First Skewness",                 "first_skewness",                                 float),
    ("First Kurtosis",                 "first_kurtosis",                                 float),
    ("First Variance",                 "first_variance",                                 float),
    ("First Uniformity",               "first_uniformity",                               float),
    # GLCM
    ("GLCM Autocorrelation",           "glcm_autocorrelation",                           float),
    ("GLCM Cluster Prominence",        "glcm_cluster_prominence",                        float),
    ("GLCM Cluster Shade",             "glcm_cluster_shade",                             float),
    ("GLCM Cluster Tendency",          "glcm_cluster_tendency",                          float),
    ("GLCM Contrast",                  "glcm_contrast",                                  float),
    ("GLCM Correlation",               "glcm_correlation",                               float),
    ("GLCM Difference Average",        "glcm_difference_average",                        float),
    ("GLCM Difference Entropy",        "glcm_difference_entropy",                        float),
    ("GLCM Difference Variance",       "glcm_difference_variance",                       float),
    ("GLCM ID",                        "glcm_id",                                        float),
    ("GLCM IDM",                       "glcm_idm",                                       float),
    ("GLCM IDMN",                      "glcm_idmn",                                      float),
    ("GLCM IDN",                       "glcm_idn",                                       float),
    ("GLCM IMC1",                      "glcm_imc_1",                                     float),
    ("GLCM IMC2",                      "glcm_imc_2",                                     float),
    ("GLCM Inverse Variance",          "glcm_inverse_variance",                          float),
    ("GLCM Joint Average",             "glcm_joint_average",                             float),
    ("GLCM Joint Energy",              "glcm_joint_energy",                              float),
    ("GLCM Joint Entropy",             "glcm_joint_entropy",                             float),
    ("GLCM Max Probabilities",         "glcm_max_probabilities",                         float),
    ("GLCM Sum Average",               "glcm_sum_average",                               float),
    ("GLCM Sum Entropy",               "glcm_sum_entropy",                               float),
    ("GLCM Sum Squares",               "glcm_sum_squares",                               float),
    # GLRLM
    ("GLRLM GL Non-Uniformity",        "glrlm_gray_level_non_uniformity",                float),
    ("GLRLM GLNU Normalized",          "glrlm_gray_level_non_uniformity_normalized",     float),
    ("GLRLM GL Variance",              "glrlm_gray_level_variance",                      float),
    ("GLRLM High GL Run Emphasis",     "glrlm_high_gray_level_run_emphasis",             float),
    ("GLRLM Long Run Emphasis",        "glrlm_long_run_emphasis",                        float),
    ("GLRLM Long Run High GL",         "glrlm_long_run_high_gray_level_emphasis",        float),
    ("GLRLM Long Run Low GL",          "glrlm_long_run_low_gray_level_emphasis",         float),
    ("GLRLM Low GL Run Emphasis",      "glrlm_low_gray_level_run_emphasis",              float),
    ("GLRLM Run Entropy",              "glrlm_run_entropy",                              float),
    ("GLRLM Run Length Non-Unif.",     "glrlm_run_length_non_uniformity",                float),
    ("GLRLM RLNU Normalized",          "glrlm_run_length_non_uniformity_normalized",     float),
    ("GLRLM Run Percentage",           "glrlm_run_percentage",                           float),
    ("GLRLM Run Variance",             "glrlm_run_variance",                             float),
    ("GLRLM Short Run Emphasis",       "glrlm_short_run_emphasis",                       float),
    ("GLRLM Short Run High GL",        "glrlm_short_run_high_gray_level_emphasis",       float),
    ("GLRLM Short Run Low GL",         "glrlm_short_run_low_gray_level_emphasis",        float),
    # GLSZM
    ("GLSZM GL Non-Uniformity",        "glszm_gray_level_non_uniformity",                float),
    ("GLSZM GLNU Normalized",          "glszm_gray_level_non_uniformity_normalized",     float),
    ("GLSZM GL Variance",              "glszm_gray_level_variance",                      float),
    ("GLSZM High GL Zone Emphasis",    "glszm_high_gray_level_zone_emphasis",            float),
    ("GLSZM Large Area Emphasis",      "glszm_large_area_emphasis",                      float),
    ("GLSZM Large Area High GL",       "glszm_large_area_high_gray_level_emphasis",      float),
    ("GLSZM Large Area Low GL",        "glszm_large_area_low_gray_level_emphasis",       float),
    ("GLSZM Low GL Zone Emphasis",     "glszm_low_gray_level_zone_emphasis",             float),
    ("GLSZM Size Zone Non-Unif.",      "glszm_size_zone_non_uniformity",                 float),
    ("GLSZM SZNU Normalized",          "glszm_size_zone_non_uniformity_normalized",      float),
    ("GLSZM Small Area Emphasis",      "glszm_small_area_emphasis",                      float),
    ("GLSZM Small Area High GL",       "glszm_small_area_high_gray_level_emphasis",      float),
    ("GLSZM Small Area Low GL",        "glszm_small_area_low_gray_level_emphasis",       float),
    ("GLSZM Zone Entropy",             "glszm_zone_entropy",                             float),
    ("GLSZM Zone Percentage",          "glszm_zone_percentage",                          float),
    ("GLSZM Zone Variance",            "glszm_zone_variance",                            float),
    # NGTDM
    ("NGTDM Busyness",                 "ngtdm_busyness",                                 float),
    ("NGTDM Coarseness",               "ngtdm_coarseness",                               float),
    ("NGTDM Complexity",               "ngtdm_complexity",                               float),
    ("NGTDM Contrast",                 "ngtdm_contrast",                                 float),
    ("NGTDM Strength",                 "ngtdm_strength",                                 float),
    # GLDM
    ("GLDM Dependence Entropy",        "gldm_dependence_entropy",                        float),
    ("GLDM Dependence Non-Unif.",      "gldm_dependence_non_uniformity",                 float),
    ("GLDM Dep. Non-Unif. Norm.",      "gldm_dependence_non_uniformity_normalized",      float),
    ("GLDM Dependence Variance",       "gldm_dependence_variance",                       float),
    ("GLDM GL Non-Uniformity",         "gldm_gray_level_non_uniformity",                 float),
    ("GLDM GL Variance",               "gldm_gray_level_variance",                       float),
    ("GLDM High GL Emphasis",          "gldm_high_gray_level_emphasis",                  float),
    ("GLDM Large Dep. Emphasis",       "gldm_large_dependence_emphasis",                 float),
    ("GLDM Large Dep. High GL",        "gldm_large_dependence_high_gray_level_emphasis", float),
    ("GLDM Large Dep. Low GL",         "gldm_large_dependence_low_gray_level_emphasis",  float),
    ("GLDM Low GL Emphasis",           "gldm_low_gray_level_emphasis",                   float),
    ("GLDM Small Dep. Emphasis",       "gldm_small_dependence_emphasis",                 float),
    ("GLDM Small Dep. High GL",        "gldm_small_dependence_high_gray_level_emphasis", float),
    ("GLDM Small Dep. Low GL",         "gldm_small_dependence_low_gray_level_emphasis",  float),
]

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _to_camel(snake: str) -> str:
    parts = snake.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


# ─────────────────────────────────────────────────────────────────────────────
# Widgets
# ─────────────────────────────────────────────────────────────────────────────

class RangeRow(Widget):
    """A labelled min/max input pair for a numeric field."""

    DEFAULT_CSS = """
    RangeRow {
        layout: horizontal;
        height: 3;
        margin-bottom: 0;
    }
    RangeRow .range-label {
        width: 28;
        height: 3;
        content-align: left middle;
        padding: 0 1;
        color: $text-muted;
    }
    RangeRow .range-label.active {
        color: $accent;
        text-style: bold;
    }
    RangeRow Input {
        width: 1fr;
        margin: 0 1;
    }
    """

    def __init__(self, label: str, camel_base: str, cast: type, **kwargs):
        super().__init__(**kwargs)
        self.label      = label
        self.camel_base = camel_base
        self.cast       = cast

    def compose(self) -> ComposeResult:
        yield Label(self.label, classes="range-label", id=f"lbl-{self.camel_base}")
        yield Input(placeholder="min", id=f"{self.camel_base}_min", classes="range-input")
        yield Input(placeholder="max", id=f"{self.camel_base}_max", classes="range-input")

    @on(Input.Changed)
    def _mark_active(self, event: Input.Changed) -> None:
        lbl = self.query_one(f"#lbl-{self.camel_base}", Label)
        has_value = bool(
            self.query_one(f"#{self.camel_base}_min", Input).value or
            self.query_one(f"#{self.camel_base}_max", Input).value
        )
        lbl.set_class(has_value, "active")

    def collect(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        raw_min = self.query_one(f"#{self.camel_base}_min", Input).value.strip()
        raw_max = self.query_one(f"#{self.camel_base}_max", Input).value.strip()
        try:
            if raw_min:
                result[self.camel_base + "Min"] = self.cast(raw_min)
        except ValueError:
            pass
        try:
            if raw_max:
                result[self.camel_base + "Max"] = self.cast(raw_max)
        except ValueError:
            pass
        return result


class ActiveFiltersBar(Static):
    """Status bar showing how many filters are active."""

    DEFAULT_CSS = """
    ActiveFiltersBar {
        height: 1;
        background: $accent;
        color: $background;
        text-align: center;
        text-style: bold;
    }
    """

    count: reactive[int] = reactive(0)

    def render(self) -> str:
        if self.count == 0:
            return "  No filters active — all images will be returned"
        return f"  {self.count} filter{'s' if self.count != 1 else ''} active"


# ─────────────────────────────────────────────────────────────────────────────
# Confirm modal
# ─────────────────────────────────────────────────────────────────────────────

class ConfirmScreen(ModalScreen[bool]):
    """Ask user to confirm before saving."""

    DEFAULT_CSS = """
    ConfirmScreen {
        align: center middle;
    }
    ConfirmScreen > Vertical {
        width: 60;
        height: auto;
        border: round $accent;
        background: $surface;
        padding: 2 4;
    }
    ConfirmScreen .confirm-title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }
    ConfirmScreen .confirm-body {
        text-align: center;
        margin-bottom: 2;
    }
    ConfirmScreen Horizontal {
        align: center middle;
        height: auto;
    }
    ConfirmScreen Button {
        margin: 0 2;
        min-width: 12;
    }
    """

    def __init__(self, n_results: int, bundle_name: str):
        super().__init__()
        self.n_results   = n_results
        self.bundle_name = bundle_name

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("Confirm", classes="confirm-title")
            yield Static(
                f"Add [bold]{self.n_results}[/bold] image ID(s) to bundle "
                f"[bold cyan]{self.bundle_name}[/bold cyan]?",
                classes="confirm-body",
                markup=True,
            )
            with Horizontal():
                yield Button("Yes, add them", variant="success", id="yes")
                yield Button("Cancel",        variant="error",   id="no")

    @on(Button.Pressed, "#yes")
    def _yes(self) -> None:
        self.dismiss(True)

    @on(Button.Pressed, "#no")
    def _no(self) -> None:
        self.dismiss(False)


# ─────────────────────────────────────────────────────────────────────────────
# Results screen
# ─────────────────────────────────────────────────────────────────────────────

class ResultsScreen(Screen):
    """Shows query results and lets user confirm."""

    BINDINGS = [
        Binding("escape", "go_back",  "Back"),
        Binding("enter",  "confirm",  "Confirm & Save"),
    ]

    DEFAULT_CSS = """
    ResultsScreen {
        layout: vertical;
    }
    ResultsScreen DataTable {
        height: 1fr;
    }
    ResultsScreen .results-footer {
        height: 3;
        layout: horizontal;
        align: right middle;
        padding: 0 2;
        background: $surface;
    }
    ResultsScreen Button {
        margin: 0 1;
        min-width: 14;
    }
    ResultsScreen .results-count {
        width: 1fr;
        content-align: left middle;
        color: $text-muted;
    }
    """

    def __init__(self, results: list, bundle_name: str):
        super().__init__()
        self.results     = results
        self.bundle_name = bundle_name

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        tbl = DataTable(id="results-table", cursor_type="row")
        yield tbl
        with Horizontal(classes="results-footer"):
            yield Static(
                f"{len(self.results)} image(s) matched",
                classes="results-count",
            )
            yield Button("← Back",       id="back",    variant="default")
            yield Button("Save IDs ✓",   id="confirm", variant="success")
        yield Footer()

    def on_mount(self) -> None:
        tbl = self.query_one("#results-table", DataTable)
        tbl.add_columns("ID", "Sex", "Age", "Manufacturer", "Model", "Seg?", "Slices")
        for img in self.results:
            tbl.add_row(
                str(img.id),
                getattr(img, "sex",               None) or "—",
                str(getattr(img, "age_years",     None) or "—"),
                getattr(img, "manufacturer",      None) or "—",
                getattr(img, "manufacturer_model",None) or "—",
                "✓" if getattr(img, "has_segmentation", False) else "✗",
                str(getattr(img, "n_slices",      None) or "—"),
            )

    @on(Button.Pressed, "#back")
    def action_go_back(self) -> None:
        self.app.pop_screen()

    @on(Button.Pressed, "#confirm")
    def action_confirm(self) -> None:
        self.app.push_screen(
            ConfirmScreen(len(self.results), self.bundle_name),
            self._on_confirm,
        )

    def _on_confirm(self, confirmed: bool) -> None:
        if confirmed:
            self.app.exit(self.results)
        else:
            self.app.pop_screen()   # back to results


# ─────────────────────────────────────────────────────────────────────────────
# Main TUI App
# ─────────────────────────────────────────────────────────────────────────────

class BundleFilterApp(App):
    """Interactive filter builder for radiant bundle add."""

    TITLE   = "radiant — bundle filter"
    CSS     = """
    /* ── Layout ─────────────────────────────────────────────────── */
    BundleFilterApp {
        layout: vertical;
    }

    /* ── Tabs ────────────────────────────────────────────────────── */
    TabbedContent {
        height: 1fr;
    }
    TabPane {
        padding: 0;
    }
    .tab-scroll {
        height: 1fr;
        padding: 1 2;
    }

    /* ── Section headers ─────────────────────────────────────────── */
    .section-header {
        height: 1;
        background: $primary;
        color: $background;
        text-style: bold;
        padding: 0 1;
        margin-bottom: 1;
    }

    /* ── Categorical row ─────────────────────────────────────────── */
    .cat-row {
        layout: horizontal;
        height: 3;
        margin-bottom: 0;
    }
    .cat-label {
        width: 28;
        height: 3;
        content-align: left middle;
        padding: 0 1;
        color: $text-muted;
    }
    .cat-label.active {
        color: $accent;
        text-style: bold;
    }
    .cat-row Input {
        width: 1fr;
        margin: 0 1;
    }

    /* ── Dataset / boolean row ───────────────────────────────────── */
    .meta-row {
        layout: horizontal;
        height: 3;
        margin-bottom: 0;
    }
    .meta-label {
        width: 28;
        height: 3;
        content-align: left middle;
        padding: 0 1;
        color: $text-muted;
    }
    .seg-switch-row {
        layout: horizontal;
        height: 3;
        align: left middle;
        margin-bottom: 1;
    }
    .seg-switch-row Label {
        width: 28;
        content-align: left middle;
        padding: 0 1;
        color: $text-muted;
    }
    .seg-options {
        layout: horizontal;
        height: 3;
        align: left middle;
    }
    .seg-options Button {
        min-width: 8;
        margin: 0 1;
        height: 2;
    }
    .seg-options Button.selected-yes {
        background: $success;
        color: $background;
    }
    .seg-options Button.selected-no {
        background: $error;
        color: $background;
    }

    /* ── Action bar ──────────────────────────────────────────────── */
    .action-bar {
        height: 3;
        layout: horizontal;
        align: right middle;
        padding: 0 2;
        background: $surface;
        border-top: solid $primary;
    }
    .action-bar Button {
        margin: 0 1;
        min-width: 14;
    }
    .spacer { width: 1fr; }

    /* ── Error toast ─────────────────────────────────────────────── */
    .error-bar {
        height: 1;
        background: $error;
        color: $background;
        text-align: center;
        display: none;
    }
    .error-bar.visible {
        display: block;
    }
    """

    BINDINGS = [
        Binding("ctrl+q", "quit",    "Quit"),
        Binding("ctrl+r", "run",     "Run Query"),
        Binding("ctrl+x", "clear",   "Clear All"),
    ]

    def __init__(self, bundle_name: str, search_fn, **kwargs):
        super().__init__(**kwargs)
        self.bundle_name = bundle_name
        self.search_fn   = search_fn          # callable(ImageFilter) -> list[ImageResponseDTO]
        self._seg_value: bool | None = None   # None=any, True=yes, False=no

    # ── Compose ────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield ActiveFiltersBar(id="filter-bar")
        yield Static("", classes="error-bar", id="error-bar")

        with TabbedContent():

            # ── Tab 1: Identity & DICOM ──────────────────────────────────
            with TabPane("DICOM", id="tab-dicom"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("Identity", classes="section-header")
                    with Container(classes="meta-row"):
                        yield Label("Dataset ID", classes="meta-label")
                        yield Input(placeholder="UUID (optional)", id="dataset_id")

                    yield Static("", classes="section-header")   # spacer
                    with Horizontal(classes="seg-switch-row"):
                        yield Label("Has Segmentation", classes="meta-label")
                        with Horizontal(classes="seg-options"):
                            yield Button("Any", id="seg-any", variant="primary")
                            yield Button("Yes", id="seg-yes", variant="default")
                            yield Button("No",  id="seg-no",  variant="default")

                    yield Static("Patient & Acquisition", classes="section-header")
                    for label, camel_id in _cat_fields_dicom():
                        with Container(classes="cat-row"):
                            yield Label(label, classes="cat-label", id=f"lbl-cat-{camel_id}")
                            yield Input(placeholder=label, id=f"cat-{camel_id}", classes="cat-input")

                    yield Static("Numeric Ranges", classes="section-header")
                    for label, base_attr, cast in _dicom_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

            # ── Tab 2: Shape ─────────────────────────────────────────────
            with TabPane("Shape", id="tab-shape"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("Shape Features", classes="section-header")
                    for label, base_attr, cast in _shape_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

            # ── Tab 3: First Order ───────────────────────────────────────
            with TabPane("First Order", id="tab-first"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("First Order Statistics", classes="section-header")
                    for label, base_attr, cast in _first_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

            # ── Tab 4: GLCM ──────────────────────────────────────────────
            with TabPane("GLCM", id="tab-glcm"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("Gray-Level Co-occurrence Matrix", classes="section-header")
                    for label, base_attr, cast in _glcm_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

            # ── Tab 5: GLRLM / GLSZM ─────────────────────────────────────
            with TabPane("GLRLM / GLSZM", id="tab-gl2"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("GLRLM", classes="section-header")
                    for label, base_attr, cast in _glrlm_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")
                    yield Static("GLSZM", classes="section-header")
                    for label, base_attr, cast in _glszm_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

            # ── Tab 6: NGTDM / GLDM ──────────────────────────────────────
            with TabPane("NGTDM / GLDM", id="tab-ng"):
                with ScrollableContainer(classes="tab-scroll"):
                    yield Static("NGTDM", classes="section-header")
                    for label, base_attr, cast in _ngtdm_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")
                    yield Static("GLDM", classes="section-header")
                    for label, base_attr, cast in _gldm_range_fields():
                        yield RangeRow(label, _to_camel(base_attr), cast,
                                       id=f"rr-{_to_camel(base_attr)}")

        with Horizontal(classes="action-bar"):
            yield Static(classes="spacer")
            yield Button("Clear All",  id="btn-clear",  variant="warning")
            yield Button("Run Query ▶", id="btn-run",   variant="success")

        yield Footer()

    # ── Segmentation toggle ────────────────────────────────────────────────

    @on(Button.Pressed, "#seg-any")
    def _seg_any(self) -> None:
        self._seg_value = None
        self._update_seg_buttons()

    @on(Button.Pressed, "#seg-yes")
    def _seg_yes(self) -> None:
        self._seg_value = True
        self._update_seg_buttons()

    @on(Button.Pressed, "#seg-no")
    def _seg_no(self) -> None:
        self._seg_value = False
        self._update_seg_buttons()

    def _update_seg_buttons(self) -> None:
        for btn_id, val in [("seg-any", None), ("seg-yes", True), ("seg-no", False)]:
            btn = self.query_one(f"#{btn_id}", Button)
            btn.variant = "primary" if self._seg_value == val else "default"
            btn.remove_class("selected-yes", "selected-no")
            if self._seg_value == val:
                if val is True:  btn.add_class("selected-yes")
                if val is False: btn.add_class("selected-no")
        self._refresh_filter_count()

    # ── Categorical active highlight ───────────────────────────────────────

    @on(Input.Changed)
    def _on_any_input(self, event: Input.Changed) -> None:
        # Highlight categorical labels
        if event.input.has_class("cat-input"):
            cat_id = event.input.id.removeprefix("cat-")
            lbl = self.query_one(f"#lbl-cat-{cat_id}", Label)
            lbl.set_class(bool(event.value), "active")
        self._refresh_filter_count()

    # ── Filter count badge ─────────────────────────────────────────────────

    def _refresh_filter_count(self) -> None:
        n = len(self._collect_filter())
        self.query_one("#filter-bar", ActiveFiltersBar).count = n

    def _collect_filter(self) -> dict[str, Any]:
        collected: dict[str, Any] = {}

        # dataset id
        raw = self.query_one("#dataset_id", Input).value.strip()
        if raw:
            collected["datasetId"] = raw

        # segmentation
        if self._seg_value is not None:
            collected["hasSegmentation"] = self._seg_value

        # categoricals
        for _label, camel_id in _cat_fields_dicom():
            raw = self.query_one(f"#cat-{camel_id}", Input).value.strip()
            if raw:
                collected[camel_id] = raw

        # all range rows
        for rr in self.query(RangeRow):
            collected.update(rr.collect())

        return collected

    # ── Actions ────────────────────────────────────────────────────────────

    @on(Button.Pressed, "#btn-run")
    def action_run(self) -> None:
        self._run_query()

    @on(Button.Pressed, "#btn-clear")
    def action_clear(self) -> None:
        for inp in self.query(Input):
            inp.value = ""
        self._seg_value = None
        self._update_seg_buttons()
        self._refresh_filter_count()

    def _run_query(self) -> None:
        from radiant.backend_api.models.image_filter import ImageFilter

        collected = self._collect_filter()
        error_bar = self.query_one("#error-bar", Static)

        try:
            image_filter = ImageFilter.from_dict(collected)
            results      = self.search_fn(image_filter)
        except Exception as exc:
            error_bar.update(f"Error: {exc}")
            error_bar.add_class("visible")
            return

        error_bar.remove_class("visible")

        if not results:
            error_bar.update("No images matched — try relaxing your filters")
            error_bar.add_class("visible")
            return

        self.push_screen(ResultsScreen(results, self.bundle_name))

    # Exit with None if user quits without confirming
    def action_quit(self) -> None:
        self.exit(None)


# ─────────────────────────────────────────────────────────────────────────────
# Field group helpers (slice RANGE_FIELDS into tabs)
# ─────────────────────────────────────────────────────────────────────────────

def _cat_fields_dicom() -> list[tuple[str, str]]:
    return [(label, camel) for label, _attr, camel in CATEGORICAL_FIELDS]

def _dicom_range_fields():
    return [r for r in RANGE_FIELDS if not any(
        r[1].startswith(p) for p in
        ("shape_", "first_", "glcm_", "glrlm_", "glszm_", "ngtdm_", "gldm_")
    )]

def _shape_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("shape_")]

def _first_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("first_")]

def _glcm_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("glcm_")]

def _glrlm_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("glrlm_")]

def _glszm_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("glszm_")]

def _ngtdm_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("ngtdm_")]

def _gldm_range_fields():
    return [r for r in RANGE_FIELDS if r[1].startswith("gldm_")]


# ─────────────────────────────────────────────────────────────────────────────
# Public entry point called from bundle.py
# ─────────────────────────────────────────────────────────────────────────────

def run_filter_tui(bundle_name: str, search_fn) -> list | None:
    """
    Launch the TUI. Returns a list[ImageResponseDTO] if the user confirmed,
    or None if they quit without saving.
    """
    app = BundleFilterApp(bundle_name=bundle_name, search_fn=search_fn)
    return app.run()


# ─────────────────────────────────────────────────────────────────────────────
# Dev entrypoint (mock data, no real backend needed)
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from dataclasses import dataclass
    import uuid

    @dataclass
    class FakeImage:
        id: uuid.UUID
        sex: str
        age_years: int
        manufacturer: str
        manufacturer_model: str
        has_segmentation: bool
        n_slices: int

    def _mock_search(f):
        return [
            FakeImage(uuid.uuid4(), "M", 45, "Siemens", "SOMATOM", True,  64),
            FakeImage(uuid.uuid4(), "F", 62, "GE",      "Optima",  False, 128),
            FakeImage(uuid.uuid4(), "M", 38, "Philips", "Ingenia", True,  96),
        ]

    result = run_filter_tui("my-bundle", _mock_search)
    if result:
        print(f"\nSaved {len(result)} image IDs.")
    else:
        print("\nCancelled.")