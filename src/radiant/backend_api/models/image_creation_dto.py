from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageCreationDTO")


@_attrs_define
class ImageCreationDTO:
    """
    Attributes:
        sex (str | Unset):
        age_years (int | Unset):
        study_date (datetime.date | Unset):
        kvp (float | Unset):
        exposure_mas (float | Unset):
        convolution_kernel (str | Unset):
        slice_thickness_mm (float | Unset):
        pixel_spacing_mm (float | Unset):
        manufacturer (str | Unset):
        manufacturer_model (str | Unset):
        software_version (str | Unset):
        rows (int | Unset):
        columns (int | Unset):
        has_segmentation (bool | Unset):
        shape_mesh_volume (float | Unset):
        shape_voxel_volume (float | Unset):
        shape_surface_area (float | Unset):
        shape_sphericity (float | Unset):
        shape_compactness_1 (float | Unset):
        shape_compactness_2 (float | Unset):
        shape_maximum_3_d_diameter (float | Unset):
        shape_major_axis_length (float | Unset):
        shape_minor_axis_length (float | Unset):
        shape_least_axis_length (float | Unset):
        shape_elongation (float | Unset):
        shape_flatness (float | Unset):
        first_energy (float | Unset):
        first_total_energy (float | Unset):
        first_entropy (float | Unset):
        first_minimum (float | Unset):
        first_10_th_percentile (float | Unset):
        first_90_th_percentile (float | Unset):
        first_maximum (float | Unset):
        first_mean (float | Unset):
        first_median (float | Unset):
        first_interquartile_range (float | Unset):
        first_range (float | Unset):
        first_mean_absolute_deviation (float | Unset):
        first_robust_mean_absolute_deviation (float | Unset):
        first_root_mean_squared (float | Unset):
        first_skewness (float | Unset):
        first_kurtosis (float | Unset):
        first_variance (float | Unset):
        first_uniformity (float | Unset):
        glcm_autocorrelation (float | Unset):
        glcm_cluster_prominence (float | Unset):
        glcm_cluster_shade (float | Unset):
        glcm_cluster_tendency (float | Unset):
        glcm_contrast (float | Unset):
        glcm_correlation (float | Unset):
        glcm_difference_average (float | Unset):
        glcm_difference_entropy (float | Unset):
        glcm_difference_variance (float | Unset):
        glcm_id (float | Unset):
        glcm_idm (float | Unset):
        glcm_idmn (float | Unset):
        glcm_idn (float | Unset):
        glcm_imc_1 (float | Unset):
        glcm_imc_2 (float | Unset):
        glcm_inverse_variance (float | Unset):
        glcm_joint_average (float | Unset):
        glcm_joint_energy (float | Unset):
        glcm_joint_entropy (float | Unset):
        glcm_max_probabilities (float | Unset):
        glcm_sum_average (float | Unset):
        glcm_sum_entropy (float | Unset):
        glcm_sum_squares (float | Unset):
        glrlm_gray_level_non_uniformity (float | Unset):
        glrlm_gray_level_non_uniformity_normalized (float | Unset):
        glrlm_gray_level_variance (float | Unset):
        glrlm_high_gray_level_run_emphasis (float | Unset):
        glrlm_long_run_emphasis (float | Unset):
        glrlm_long_run_high_gray_level_emphasis (float | Unset):
        glrlm_long_run_low_gray_level_emphasis (float | Unset):
        glrlm_low_gray_level_run_emphasis (float | Unset):
        glrlm_run_entropy (float | Unset):
        glrlm_run_length_non_uniformity (float | Unset):
        glrlm_run_length_non_uniformity_normalized (float | Unset):
        glrlm_run_percentage (float | Unset):
        glrlm_run_variance (float | Unset):
        glrlm_short_run_emphasis (float | Unset):
        glrlm_short_run_high_gray_level_emphasis (float | Unset):
        glrlm_short_run_low_gray_level_emphasis (float | Unset):
        glszm_gray_level_non_uniformity (float | Unset):
        glszm_gray_level_non_uniformity_normalized (float | Unset):
        glszm_gray_level_variance (float | Unset):
        glszm_high_gray_level_zone_emphasis (float | Unset):
        glszm_large_area_emphasis (float | Unset):
        glszm_large_area_high_gray_level_emphasis (float | Unset):
        glszm_large_area_low_gray_level_emphasis (float | Unset):
        glszm_low_gray_level_zone_emphasis (float | Unset):
        glszm_size_zone_non_uniformity (float | Unset):
        glszm_size_zone_non_uniformity_normalized (float | Unset):
        glszm_small_area_emphasis (float | Unset):
        glszm_small_area_high_gray_level_emphasis (float | Unset):
        glszm_small_area_low_gray_level_emphasis (float | Unset):
        glszm_zone_entropy (float | Unset):
        glszm_zone_percentage (float | Unset):
        glszm_zone_variance (float | Unset):
        ngtdm_busyness (float | Unset):
        ngtdm_coarseness (float | Unset):
        ngtdm_complexity (float | Unset):
        ngtdm_contrast (float | Unset):
        ngtdm_strength (float | Unset):
        gldm_dependence_entropy (float | Unset):
        gldm_dependence_non_uniformity (float | Unset):
        gldm_dependence_non_uniformity_normalized (float | Unset):
        gldm_dependence_variance (float | Unset):
        gldm_gray_level_non_uniformity (float | Unset):
        gldm_gray_level_variance (float | Unset):
        gldm_high_gray_level_emphasis (float | Unset):
        gldm_large_dependence_emphasis (float | Unset):
        gldm_large_dependence_high_gray_level_emphasis (float | Unset):
        gldm_large_dependence_low_gray_level_emphasis (float | Unset):
        gldm_low_gray_level_emphasis (float | Unset):
        gldm_small_dependence_emphasis (float | Unset):
        gldm_small_dependence_high_gray_level_emphasis (float | Unset):
        gldm_small_dependence_low_gray_level_emphasis (float | Unset):
        nslices (int | Unset):
    """

    sex: str | Unset = UNSET
    age_years: int | Unset = UNSET
    study_date: datetime.date | Unset = UNSET
    kvp: float | Unset = UNSET
    exposure_mas: float | Unset = UNSET
    convolution_kernel: str | Unset = UNSET
    slice_thickness_mm: float | Unset = UNSET
    pixel_spacing_mm: float | Unset = UNSET
    manufacturer: str | Unset = UNSET
    manufacturer_model: str | Unset = UNSET
    software_version: str | Unset = UNSET
    rows: int | Unset = UNSET
    columns: int | Unset = UNSET
    has_segmentation: bool | Unset = UNSET
    shape_mesh_volume: float | Unset = UNSET
    shape_voxel_volume: float | Unset = UNSET
    shape_surface_area: float | Unset = UNSET
    shape_sphericity: float | Unset = UNSET
    shape_compactness_1: float | Unset = UNSET
    shape_compactness_2: float | Unset = UNSET
    shape_maximum_3_d_diameter: float | Unset = UNSET
    shape_major_axis_length: float | Unset = UNSET
    shape_minor_axis_length: float | Unset = UNSET
    shape_least_axis_length: float | Unset = UNSET
    shape_elongation: float | Unset = UNSET
    shape_flatness: float | Unset = UNSET
    first_energy: float | Unset = UNSET
    first_total_energy: float | Unset = UNSET
    first_entropy: float | Unset = UNSET
    first_minimum: float | Unset = UNSET
    first_10_th_percentile: float | Unset = UNSET
    first_90_th_percentile: float | Unset = UNSET
    first_maximum: float | Unset = UNSET
    first_mean: float | Unset = UNSET
    first_median: float | Unset = UNSET
    first_interquartile_range: float | Unset = UNSET
    first_range: float | Unset = UNSET
    first_mean_absolute_deviation: float | Unset = UNSET
    first_robust_mean_absolute_deviation: float | Unset = UNSET
    first_root_mean_squared: float | Unset = UNSET
    first_skewness: float | Unset = UNSET
    first_kurtosis: float | Unset = UNSET
    first_variance: float | Unset = UNSET
    first_uniformity: float | Unset = UNSET
    glcm_autocorrelation: float | Unset = UNSET
    glcm_cluster_prominence: float | Unset = UNSET
    glcm_cluster_shade: float | Unset = UNSET
    glcm_cluster_tendency: float | Unset = UNSET
    glcm_contrast: float | Unset = UNSET
    glcm_correlation: float | Unset = UNSET
    glcm_difference_average: float | Unset = UNSET
    glcm_difference_entropy: float | Unset = UNSET
    glcm_difference_variance: float | Unset = UNSET
    glcm_id: float | Unset = UNSET
    glcm_idm: float | Unset = UNSET
    glcm_idmn: float | Unset = UNSET
    glcm_idn: float | Unset = UNSET
    glcm_imc_1: float | Unset = UNSET
    glcm_imc_2: float | Unset = UNSET
    glcm_inverse_variance: float | Unset = UNSET
    glcm_joint_average: float | Unset = UNSET
    glcm_joint_energy: float | Unset = UNSET
    glcm_joint_entropy: float | Unset = UNSET
    glcm_max_probabilities: float | Unset = UNSET
    glcm_sum_average: float | Unset = UNSET
    glcm_sum_entropy: float | Unset = UNSET
    glcm_sum_squares: float | Unset = UNSET
    glrlm_gray_level_non_uniformity: float | Unset = UNSET
    glrlm_gray_level_non_uniformity_normalized: float | Unset = UNSET
    glrlm_gray_level_variance: float | Unset = UNSET
    glrlm_high_gray_level_run_emphasis: float | Unset = UNSET
    glrlm_long_run_emphasis: float | Unset = UNSET
    glrlm_long_run_high_gray_level_emphasis: float | Unset = UNSET
    glrlm_long_run_low_gray_level_emphasis: float | Unset = UNSET
    glrlm_low_gray_level_run_emphasis: float | Unset = UNSET
    glrlm_run_entropy: float | Unset = UNSET
    glrlm_run_length_non_uniformity: float | Unset = UNSET
    glrlm_run_length_non_uniformity_normalized: float | Unset = UNSET
    glrlm_run_percentage: float | Unset = UNSET
    glrlm_run_variance: float | Unset = UNSET
    glrlm_short_run_emphasis: float | Unset = UNSET
    glrlm_short_run_high_gray_level_emphasis: float | Unset = UNSET
    glrlm_short_run_low_gray_level_emphasis: float | Unset = UNSET
    glszm_gray_level_non_uniformity: float | Unset = UNSET
    glszm_gray_level_non_uniformity_normalized: float | Unset = UNSET
    glszm_gray_level_variance: float | Unset = UNSET
    glszm_high_gray_level_zone_emphasis: float | Unset = UNSET
    glszm_large_area_emphasis: float | Unset = UNSET
    glszm_large_area_high_gray_level_emphasis: float | Unset = UNSET
    glszm_large_area_low_gray_level_emphasis: float | Unset = UNSET
    glszm_low_gray_level_zone_emphasis: float | Unset = UNSET
    glszm_size_zone_non_uniformity: float | Unset = UNSET
    glszm_size_zone_non_uniformity_normalized: float | Unset = UNSET
    glszm_small_area_emphasis: float | Unset = UNSET
    glszm_small_area_high_gray_level_emphasis: float | Unset = UNSET
    glszm_small_area_low_gray_level_emphasis: float | Unset = UNSET
    glszm_zone_entropy: float | Unset = UNSET
    glszm_zone_percentage: float | Unset = UNSET
    glszm_zone_variance: float | Unset = UNSET
    ngtdm_busyness: float | Unset = UNSET
    ngtdm_coarseness: float | Unset = UNSET
    ngtdm_complexity: float | Unset = UNSET
    ngtdm_contrast: float | Unset = UNSET
    ngtdm_strength: float | Unset = UNSET
    gldm_dependence_entropy: float | Unset = UNSET
    gldm_dependence_non_uniformity: float | Unset = UNSET
    gldm_dependence_non_uniformity_normalized: float | Unset = UNSET
    gldm_dependence_variance: float | Unset = UNSET
    gldm_gray_level_non_uniformity: float | Unset = UNSET
    gldm_gray_level_variance: float | Unset = UNSET
    gldm_high_gray_level_emphasis: float | Unset = UNSET
    gldm_large_dependence_emphasis: float | Unset = UNSET
    gldm_large_dependence_high_gray_level_emphasis: float | Unset = UNSET
    gldm_large_dependence_low_gray_level_emphasis: float | Unset = UNSET
    gldm_low_gray_level_emphasis: float | Unset = UNSET
    gldm_small_dependence_emphasis: float | Unset = UNSET
    gldm_small_dependence_high_gray_level_emphasis: float | Unset = UNSET
    gldm_small_dependence_low_gray_level_emphasis: float | Unset = UNSET
    nslices: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sex = self.sex

        age_years = self.age_years

        study_date: str | Unset = UNSET
        if not isinstance(self.study_date, Unset):
            study_date = self.study_date.isoformat()

        kvp = self.kvp

        exposure_mas = self.exposure_mas

        convolution_kernel = self.convolution_kernel

        slice_thickness_mm = self.slice_thickness_mm

        pixel_spacing_mm = self.pixel_spacing_mm

        manufacturer = self.manufacturer

        manufacturer_model = self.manufacturer_model

        software_version = self.software_version

        rows = self.rows

        columns = self.columns

        has_segmentation = self.has_segmentation

        shape_mesh_volume = self.shape_mesh_volume

        shape_voxel_volume = self.shape_voxel_volume

        shape_surface_area = self.shape_surface_area

        shape_sphericity = self.shape_sphericity

        shape_compactness_1 = self.shape_compactness_1

        shape_compactness_2 = self.shape_compactness_2

        shape_maximum_3_d_diameter = self.shape_maximum_3_d_diameter

        shape_major_axis_length = self.shape_major_axis_length

        shape_minor_axis_length = self.shape_minor_axis_length

        shape_least_axis_length = self.shape_least_axis_length

        shape_elongation = self.shape_elongation

        shape_flatness = self.shape_flatness

        first_energy = self.first_energy

        first_total_energy = self.first_total_energy

        first_entropy = self.first_entropy

        first_minimum = self.first_minimum

        first_10_th_percentile = self.first_10_th_percentile

        first_90_th_percentile = self.first_90_th_percentile

        first_maximum = self.first_maximum

        first_mean = self.first_mean

        first_median = self.first_median

        first_interquartile_range = self.first_interquartile_range

        first_range = self.first_range

        first_mean_absolute_deviation = self.first_mean_absolute_deviation

        first_robust_mean_absolute_deviation = self.first_robust_mean_absolute_deviation

        first_root_mean_squared = self.first_root_mean_squared

        first_skewness = self.first_skewness

        first_kurtosis = self.first_kurtosis

        first_variance = self.first_variance

        first_uniformity = self.first_uniformity

        glcm_autocorrelation = self.glcm_autocorrelation

        glcm_cluster_prominence = self.glcm_cluster_prominence

        glcm_cluster_shade = self.glcm_cluster_shade

        glcm_cluster_tendency = self.glcm_cluster_tendency

        glcm_contrast = self.glcm_contrast

        glcm_correlation = self.glcm_correlation

        glcm_difference_average = self.glcm_difference_average

        glcm_difference_entropy = self.glcm_difference_entropy

        glcm_difference_variance = self.glcm_difference_variance

        glcm_id = self.glcm_id

        glcm_idm = self.glcm_idm

        glcm_idmn = self.glcm_idmn

        glcm_idn = self.glcm_idn

        glcm_imc_1 = self.glcm_imc_1

        glcm_imc_2 = self.glcm_imc_2

        glcm_inverse_variance = self.glcm_inverse_variance

        glcm_joint_average = self.glcm_joint_average

        glcm_joint_energy = self.glcm_joint_energy

        glcm_joint_entropy = self.glcm_joint_entropy

        glcm_max_probabilities = self.glcm_max_probabilities

        glcm_sum_average = self.glcm_sum_average

        glcm_sum_entropy = self.glcm_sum_entropy

        glcm_sum_squares = self.glcm_sum_squares

        glrlm_gray_level_non_uniformity = self.glrlm_gray_level_non_uniformity

        glrlm_gray_level_non_uniformity_normalized = self.glrlm_gray_level_non_uniformity_normalized

        glrlm_gray_level_variance = self.glrlm_gray_level_variance

        glrlm_high_gray_level_run_emphasis = self.glrlm_high_gray_level_run_emphasis

        glrlm_long_run_emphasis = self.glrlm_long_run_emphasis

        glrlm_long_run_high_gray_level_emphasis = self.glrlm_long_run_high_gray_level_emphasis

        glrlm_long_run_low_gray_level_emphasis = self.glrlm_long_run_low_gray_level_emphasis

        glrlm_low_gray_level_run_emphasis = self.glrlm_low_gray_level_run_emphasis

        glrlm_run_entropy = self.glrlm_run_entropy

        glrlm_run_length_non_uniformity = self.glrlm_run_length_non_uniformity

        glrlm_run_length_non_uniformity_normalized = self.glrlm_run_length_non_uniformity_normalized

        glrlm_run_percentage = self.glrlm_run_percentage

        glrlm_run_variance = self.glrlm_run_variance

        glrlm_short_run_emphasis = self.glrlm_short_run_emphasis

        glrlm_short_run_high_gray_level_emphasis = self.glrlm_short_run_high_gray_level_emphasis

        glrlm_short_run_low_gray_level_emphasis = self.glrlm_short_run_low_gray_level_emphasis

        glszm_gray_level_non_uniformity = self.glszm_gray_level_non_uniformity

        glszm_gray_level_non_uniformity_normalized = self.glszm_gray_level_non_uniformity_normalized

        glszm_gray_level_variance = self.glszm_gray_level_variance

        glszm_high_gray_level_zone_emphasis = self.glszm_high_gray_level_zone_emphasis

        glszm_large_area_emphasis = self.glszm_large_area_emphasis

        glszm_large_area_high_gray_level_emphasis = self.glszm_large_area_high_gray_level_emphasis

        glszm_large_area_low_gray_level_emphasis = self.glszm_large_area_low_gray_level_emphasis

        glszm_low_gray_level_zone_emphasis = self.glszm_low_gray_level_zone_emphasis

        glszm_size_zone_non_uniformity = self.glszm_size_zone_non_uniformity

        glszm_size_zone_non_uniformity_normalized = self.glszm_size_zone_non_uniformity_normalized

        glszm_small_area_emphasis = self.glszm_small_area_emphasis

        glszm_small_area_high_gray_level_emphasis = self.glszm_small_area_high_gray_level_emphasis

        glszm_small_area_low_gray_level_emphasis = self.glszm_small_area_low_gray_level_emphasis

        glszm_zone_entropy = self.glszm_zone_entropy

        glszm_zone_percentage = self.glszm_zone_percentage

        glszm_zone_variance = self.glszm_zone_variance

        ngtdm_busyness = self.ngtdm_busyness

        ngtdm_coarseness = self.ngtdm_coarseness

        ngtdm_complexity = self.ngtdm_complexity

        ngtdm_contrast = self.ngtdm_contrast

        ngtdm_strength = self.ngtdm_strength

        gldm_dependence_entropy = self.gldm_dependence_entropy

        gldm_dependence_non_uniformity = self.gldm_dependence_non_uniformity

        gldm_dependence_non_uniformity_normalized = self.gldm_dependence_non_uniformity_normalized

        gldm_dependence_variance = self.gldm_dependence_variance

        gldm_gray_level_non_uniformity = self.gldm_gray_level_non_uniformity

        gldm_gray_level_variance = self.gldm_gray_level_variance

        gldm_high_gray_level_emphasis = self.gldm_high_gray_level_emphasis

        gldm_large_dependence_emphasis = self.gldm_large_dependence_emphasis

        gldm_large_dependence_high_gray_level_emphasis = self.gldm_large_dependence_high_gray_level_emphasis

        gldm_large_dependence_low_gray_level_emphasis = self.gldm_large_dependence_low_gray_level_emphasis

        gldm_low_gray_level_emphasis = self.gldm_low_gray_level_emphasis

        gldm_small_dependence_emphasis = self.gldm_small_dependence_emphasis

        gldm_small_dependence_high_gray_level_emphasis = self.gldm_small_dependence_high_gray_level_emphasis

        gldm_small_dependence_low_gray_level_emphasis = self.gldm_small_dependence_low_gray_level_emphasis

        nslices = self.nslices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sex is not UNSET:
            field_dict["sex"] = sex
        if age_years is not UNSET:
            field_dict["ageYears"] = age_years
        if study_date is not UNSET:
            field_dict["studyDate"] = study_date
        if kvp is not UNSET:
            field_dict["kvp"] = kvp
        if exposure_mas is not UNSET:
            field_dict["exposureMas"] = exposure_mas
        if convolution_kernel is not UNSET:
            field_dict["convolutionKernel"] = convolution_kernel
        if slice_thickness_mm is not UNSET:
            field_dict["sliceThicknessMm"] = slice_thickness_mm
        if pixel_spacing_mm is not UNSET:
            field_dict["pixelSpacingMm"] = pixel_spacing_mm
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if manufacturer_model is not UNSET:
            field_dict["manufacturerModel"] = manufacturer_model
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if rows is not UNSET:
            field_dict["rows"] = rows
        if columns is not UNSET:
            field_dict["columns"] = columns
        if has_segmentation is not UNSET:
            field_dict["hasSegmentation"] = has_segmentation
        if shape_mesh_volume is not UNSET:
            field_dict["shapeMeshVolume"] = shape_mesh_volume
        if shape_voxel_volume is not UNSET:
            field_dict["shapeVoxelVolume"] = shape_voxel_volume
        if shape_surface_area is not UNSET:
            field_dict["shapeSurfaceArea"] = shape_surface_area
        if shape_sphericity is not UNSET:
            field_dict["shapeSphericity"] = shape_sphericity
        if shape_compactness_1 is not UNSET:
            field_dict["shapeCompactness1"] = shape_compactness_1
        if shape_compactness_2 is not UNSET:
            field_dict["shapeCompactness2"] = shape_compactness_2
        if shape_maximum_3_d_diameter is not UNSET:
            field_dict["shapeMaximum3dDiameter"] = shape_maximum_3_d_diameter
        if shape_major_axis_length is not UNSET:
            field_dict["shapeMajorAxisLength"] = shape_major_axis_length
        if shape_minor_axis_length is not UNSET:
            field_dict["shapeMinorAxisLength"] = shape_minor_axis_length
        if shape_least_axis_length is not UNSET:
            field_dict["shapeLeastAxisLength"] = shape_least_axis_length
        if shape_elongation is not UNSET:
            field_dict["shapeElongation"] = shape_elongation
        if shape_flatness is not UNSET:
            field_dict["shapeFlatness"] = shape_flatness
        if first_energy is not UNSET:
            field_dict["firstEnergy"] = first_energy
        if first_total_energy is not UNSET:
            field_dict["firstTotalEnergy"] = first_total_energy
        if first_entropy is not UNSET:
            field_dict["firstEntropy"] = first_entropy
        if first_minimum is not UNSET:
            field_dict["firstMinimum"] = first_minimum
        if first_10_th_percentile is not UNSET:
            field_dict["first10thPercentile"] = first_10_th_percentile
        if first_90_th_percentile is not UNSET:
            field_dict["first90thPercentile"] = first_90_th_percentile
        if first_maximum is not UNSET:
            field_dict["firstMaximum"] = first_maximum
        if first_mean is not UNSET:
            field_dict["firstMean"] = first_mean
        if first_median is not UNSET:
            field_dict["firstMedian"] = first_median
        if first_interquartile_range is not UNSET:
            field_dict["firstInterquartileRange"] = first_interquartile_range
        if first_range is not UNSET:
            field_dict["firstRange"] = first_range
        if first_mean_absolute_deviation is not UNSET:
            field_dict["firstMeanAbsoluteDeviation"] = first_mean_absolute_deviation
        if first_robust_mean_absolute_deviation is not UNSET:
            field_dict["firstRobustMeanAbsoluteDeviation"] = first_robust_mean_absolute_deviation
        if first_root_mean_squared is not UNSET:
            field_dict["firstRootMeanSquared"] = first_root_mean_squared
        if first_skewness is not UNSET:
            field_dict["firstSkewness"] = first_skewness
        if first_kurtosis is not UNSET:
            field_dict["firstKurtosis"] = first_kurtosis
        if first_variance is not UNSET:
            field_dict["firstVariance"] = first_variance
        if first_uniformity is not UNSET:
            field_dict["firstUniformity"] = first_uniformity
        if glcm_autocorrelation is not UNSET:
            field_dict["glcmAutocorrelation"] = glcm_autocorrelation
        if glcm_cluster_prominence is not UNSET:
            field_dict["glcmClusterProminence"] = glcm_cluster_prominence
        if glcm_cluster_shade is not UNSET:
            field_dict["glcmClusterShade"] = glcm_cluster_shade
        if glcm_cluster_tendency is not UNSET:
            field_dict["glcmClusterTendency"] = glcm_cluster_tendency
        if glcm_contrast is not UNSET:
            field_dict["glcmContrast"] = glcm_contrast
        if glcm_correlation is not UNSET:
            field_dict["glcmCorrelation"] = glcm_correlation
        if glcm_difference_average is not UNSET:
            field_dict["glcmDifferenceAverage"] = glcm_difference_average
        if glcm_difference_entropy is not UNSET:
            field_dict["glcmDifferenceEntropy"] = glcm_difference_entropy
        if glcm_difference_variance is not UNSET:
            field_dict["glcmDifferenceVariance"] = glcm_difference_variance
        if glcm_id is not UNSET:
            field_dict["glcmId"] = glcm_id
        if glcm_idm is not UNSET:
            field_dict["glcmIdm"] = glcm_idm
        if glcm_idmn is not UNSET:
            field_dict["glcmIdmn"] = glcm_idmn
        if glcm_idn is not UNSET:
            field_dict["glcmIdn"] = glcm_idn
        if glcm_imc_1 is not UNSET:
            field_dict["glcmImc1"] = glcm_imc_1
        if glcm_imc_2 is not UNSET:
            field_dict["glcmImc2"] = glcm_imc_2
        if glcm_inverse_variance is not UNSET:
            field_dict["glcmInverseVariance"] = glcm_inverse_variance
        if glcm_joint_average is not UNSET:
            field_dict["glcmJointAverage"] = glcm_joint_average
        if glcm_joint_energy is not UNSET:
            field_dict["glcmJointEnergy"] = glcm_joint_energy
        if glcm_joint_entropy is not UNSET:
            field_dict["glcmJointEntropy"] = glcm_joint_entropy
        if glcm_max_probabilities is not UNSET:
            field_dict["glcmMaxProbabilities"] = glcm_max_probabilities
        if glcm_sum_average is not UNSET:
            field_dict["glcmSumAverage"] = glcm_sum_average
        if glcm_sum_entropy is not UNSET:
            field_dict["glcmSumEntropy"] = glcm_sum_entropy
        if glcm_sum_squares is not UNSET:
            field_dict["glcmSumSquares"] = glcm_sum_squares
        if glrlm_gray_level_non_uniformity is not UNSET:
            field_dict["glrlmGrayLevelNonUniformity"] = glrlm_gray_level_non_uniformity
        if glrlm_gray_level_non_uniformity_normalized is not UNSET:
            field_dict["glrlmGrayLevelNonUniformityNormalized"] = glrlm_gray_level_non_uniformity_normalized
        if glrlm_gray_level_variance is not UNSET:
            field_dict["glrlmGrayLevelVariance"] = glrlm_gray_level_variance
        if glrlm_high_gray_level_run_emphasis is not UNSET:
            field_dict["glrlmHighGrayLevelRunEmphasis"] = glrlm_high_gray_level_run_emphasis
        if glrlm_long_run_emphasis is not UNSET:
            field_dict["glrlmLongRunEmphasis"] = glrlm_long_run_emphasis
        if glrlm_long_run_high_gray_level_emphasis is not UNSET:
            field_dict["glrlmLongRunHighGrayLevelEmphasis"] = glrlm_long_run_high_gray_level_emphasis
        if glrlm_long_run_low_gray_level_emphasis is not UNSET:
            field_dict["glrlmLongRunLowGrayLevelEmphasis"] = glrlm_long_run_low_gray_level_emphasis
        if glrlm_low_gray_level_run_emphasis is not UNSET:
            field_dict["glrlmLowGrayLevelRunEmphasis"] = glrlm_low_gray_level_run_emphasis
        if glrlm_run_entropy is not UNSET:
            field_dict["glrlmRunEntropy"] = glrlm_run_entropy
        if glrlm_run_length_non_uniformity is not UNSET:
            field_dict["glrlmRunLengthNonUniformity"] = glrlm_run_length_non_uniformity
        if glrlm_run_length_non_uniformity_normalized is not UNSET:
            field_dict["glrlmRunLengthNonUniformityNormalized"] = glrlm_run_length_non_uniformity_normalized
        if glrlm_run_percentage is not UNSET:
            field_dict["glrlmRunPercentage"] = glrlm_run_percentage
        if glrlm_run_variance is not UNSET:
            field_dict["glrlmRunVariance"] = glrlm_run_variance
        if glrlm_short_run_emphasis is not UNSET:
            field_dict["glrlmShortRunEmphasis"] = glrlm_short_run_emphasis
        if glrlm_short_run_high_gray_level_emphasis is not UNSET:
            field_dict["glrlmShortRunHighGrayLevelEmphasis"] = glrlm_short_run_high_gray_level_emphasis
        if glrlm_short_run_low_gray_level_emphasis is not UNSET:
            field_dict["glrlmShortRunLowGrayLevelEmphasis"] = glrlm_short_run_low_gray_level_emphasis
        if glszm_gray_level_non_uniformity is not UNSET:
            field_dict["glszmGrayLevelNonUniformity"] = glszm_gray_level_non_uniformity
        if glszm_gray_level_non_uniformity_normalized is not UNSET:
            field_dict["glszmGrayLevelNonUniformityNormalized"] = glszm_gray_level_non_uniformity_normalized
        if glszm_gray_level_variance is not UNSET:
            field_dict["glszmGrayLevelVariance"] = glszm_gray_level_variance
        if glszm_high_gray_level_zone_emphasis is not UNSET:
            field_dict["glszmHighGrayLevelZoneEmphasis"] = glszm_high_gray_level_zone_emphasis
        if glszm_large_area_emphasis is not UNSET:
            field_dict["glszmLargeAreaEmphasis"] = glszm_large_area_emphasis
        if glszm_large_area_high_gray_level_emphasis is not UNSET:
            field_dict["glszmLargeAreaHighGrayLevelEmphasis"] = glszm_large_area_high_gray_level_emphasis
        if glszm_large_area_low_gray_level_emphasis is not UNSET:
            field_dict["glszmLargeAreaLowGrayLevelEmphasis"] = glszm_large_area_low_gray_level_emphasis
        if glszm_low_gray_level_zone_emphasis is not UNSET:
            field_dict["glszmLowGrayLevelZoneEmphasis"] = glszm_low_gray_level_zone_emphasis
        if glszm_size_zone_non_uniformity is not UNSET:
            field_dict["glszmSizeZoneNonUniformity"] = glszm_size_zone_non_uniformity
        if glszm_size_zone_non_uniformity_normalized is not UNSET:
            field_dict["glszmSizeZoneNonUniformityNormalized"] = glszm_size_zone_non_uniformity_normalized
        if glszm_small_area_emphasis is not UNSET:
            field_dict["glszmSmallAreaEmphasis"] = glszm_small_area_emphasis
        if glszm_small_area_high_gray_level_emphasis is not UNSET:
            field_dict["glszmSmallAreaHighGrayLevelEmphasis"] = glszm_small_area_high_gray_level_emphasis
        if glszm_small_area_low_gray_level_emphasis is not UNSET:
            field_dict["glszmSmallAreaLowGrayLevelEmphasis"] = glszm_small_area_low_gray_level_emphasis
        if glszm_zone_entropy is not UNSET:
            field_dict["glszmZoneEntropy"] = glszm_zone_entropy
        if glszm_zone_percentage is not UNSET:
            field_dict["glszmZonePercentage"] = glszm_zone_percentage
        if glszm_zone_variance is not UNSET:
            field_dict["glszmZoneVariance"] = glszm_zone_variance
        if ngtdm_busyness is not UNSET:
            field_dict["ngtdmBusyness"] = ngtdm_busyness
        if ngtdm_coarseness is not UNSET:
            field_dict["ngtdmCoarseness"] = ngtdm_coarseness
        if ngtdm_complexity is not UNSET:
            field_dict["ngtdmComplexity"] = ngtdm_complexity
        if ngtdm_contrast is not UNSET:
            field_dict["ngtdmContrast"] = ngtdm_contrast
        if ngtdm_strength is not UNSET:
            field_dict["ngtdmStrength"] = ngtdm_strength
        if gldm_dependence_entropy is not UNSET:
            field_dict["gldmDependenceEntropy"] = gldm_dependence_entropy
        if gldm_dependence_non_uniformity is not UNSET:
            field_dict["gldmDependenceNonUniformity"] = gldm_dependence_non_uniformity
        if gldm_dependence_non_uniformity_normalized is not UNSET:
            field_dict["gldmDependenceNonUniformityNormalized"] = gldm_dependence_non_uniformity_normalized
        if gldm_dependence_variance is not UNSET:
            field_dict["gldmDependenceVariance"] = gldm_dependence_variance
        if gldm_gray_level_non_uniformity is not UNSET:
            field_dict["gldmGrayLevelNonUniformity"] = gldm_gray_level_non_uniformity
        if gldm_gray_level_variance is not UNSET:
            field_dict["gldmGrayLevelVariance"] = gldm_gray_level_variance
        if gldm_high_gray_level_emphasis is not UNSET:
            field_dict["gldmHighGrayLevelEmphasis"] = gldm_high_gray_level_emphasis
        if gldm_large_dependence_emphasis is not UNSET:
            field_dict["gldmLargeDependenceEmphasis"] = gldm_large_dependence_emphasis
        if gldm_large_dependence_high_gray_level_emphasis is not UNSET:
            field_dict["gldmLargeDependenceHighGrayLevelEmphasis"] = gldm_large_dependence_high_gray_level_emphasis
        if gldm_large_dependence_low_gray_level_emphasis is not UNSET:
            field_dict["gldmLargeDependenceLowGrayLevelEmphasis"] = gldm_large_dependence_low_gray_level_emphasis
        if gldm_low_gray_level_emphasis is not UNSET:
            field_dict["gldmLowGrayLevelEmphasis"] = gldm_low_gray_level_emphasis
        if gldm_small_dependence_emphasis is not UNSET:
            field_dict["gldmSmallDependenceEmphasis"] = gldm_small_dependence_emphasis
        if gldm_small_dependence_high_gray_level_emphasis is not UNSET:
            field_dict["gldmSmallDependenceHighGrayLevelEmphasis"] = gldm_small_dependence_high_gray_level_emphasis
        if gldm_small_dependence_low_gray_level_emphasis is not UNSET:
            field_dict["gldmSmallDependenceLowGrayLevelEmphasis"] = gldm_small_dependence_low_gray_level_emphasis
        if nslices is not UNSET:
            field_dict["nslices"] = nslices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sex = d.pop("sex", UNSET)

        age_years = d.pop("ageYears", UNSET)

        _study_date = d.pop("studyDate", UNSET)
        study_date: datetime.date | Unset
        if isinstance(_study_date, Unset):
            study_date = UNSET
        else:
            study_date = isoparse(_study_date).date()

        kvp = d.pop("kvp", UNSET)

        exposure_mas = d.pop("exposureMas", UNSET)

        convolution_kernel = d.pop("convolutionKernel", UNSET)

        slice_thickness_mm = d.pop("sliceThicknessMm", UNSET)

        pixel_spacing_mm = d.pop("pixelSpacingMm", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        manufacturer_model = d.pop("manufacturerModel", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        rows = d.pop("rows", UNSET)

        columns = d.pop("columns", UNSET)

        has_segmentation = d.pop("hasSegmentation", UNSET)

        shape_mesh_volume = d.pop("shapeMeshVolume", UNSET)

        shape_voxel_volume = d.pop("shapeVoxelVolume", UNSET)

        shape_surface_area = d.pop("shapeSurfaceArea", UNSET)

        shape_sphericity = d.pop("shapeSphericity", UNSET)

        shape_compactness_1 = d.pop("shapeCompactness1", UNSET)

        shape_compactness_2 = d.pop("shapeCompactness2", UNSET)

        shape_maximum_3_d_diameter = d.pop("shapeMaximum3dDiameter", UNSET)

        shape_major_axis_length = d.pop("shapeMajorAxisLength", UNSET)

        shape_minor_axis_length = d.pop("shapeMinorAxisLength", UNSET)

        shape_least_axis_length = d.pop("shapeLeastAxisLength", UNSET)

        shape_elongation = d.pop("shapeElongation", UNSET)

        shape_flatness = d.pop("shapeFlatness", UNSET)

        first_energy = d.pop("firstEnergy", UNSET)

        first_total_energy = d.pop("firstTotalEnergy", UNSET)

        first_entropy = d.pop("firstEntropy", UNSET)

        first_minimum = d.pop("firstMinimum", UNSET)

        first_10_th_percentile = d.pop("first10thPercentile", UNSET)

        first_90_th_percentile = d.pop("first90thPercentile", UNSET)

        first_maximum = d.pop("firstMaximum", UNSET)

        first_mean = d.pop("firstMean", UNSET)

        first_median = d.pop("firstMedian", UNSET)

        first_interquartile_range = d.pop("firstInterquartileRange", UNSET)

        first_range = d.pop("firstRange", UNSET)

        first_mean_absolute_deviation = d.pop("firstMeanAbsoluteDeviation", UNSET)

        first_robust_mean_absolute_deviation = d.pop("firstRobustMeanAbsoluteDeviation", UNSET)

        first_root_mean_squared = d.pop("firstRootMeanSquared", UNSET)

        first_skewness = d.pop("firstSkewness", UNSET)

        first_kurtosis = d.pop("firstKurtosis", UNSET)

        first_variance = d.pop("firstVariance", UNSET)

        first_uniformity = d.pop("firstUniformity", UNSET)

        glcm_autocorrelation = d.pop("glcmAutocorrelation", UNSET)

        glcm_cluster_prominence = d.pop("glcmClusterProminence", UNSET)

        glcm_cluster_shade = d.pop("glcmClusterShade", UNSET)

        glcm_cluster_tendency = d.pop("glcmClusterTendency", UNSET)

        glcm_contrast = d.pop("glcmContrast", UNSET)

        glcm_correlation = d.pop("glcmCorrelation", UNSET)

        glcm_difference_average = d.pop("glcmDifferenceAverage", UNSET)

        glcm_difference_entropy = d.pop("glcmDifferenceEntropy", UNSET)

        glcm_difference_variance = d.pop("glcmDifferenceVariance", UNSET)

        glcm_id = d.pop("glcmId", UNSET)

        glcm_idm = d.pop("glcmIdm", UNSET)

        glcm_idmn = d.pop("glcmIdmn", UNSET)

        glcm_idn = d.pop("glcmIdn", UNSET)

        glcm_imc_1 = d.pop("glcmImc1", UNSET)

        glcm_imc_2 = d.pop("glcmImc2", UNSET)

        glcm_inverse_variance = d.pop("glcmInverseVariance", UNSET)

        glcm_joint_average = d.pop("glcmJointAverage", UNSET)

        glcm_joint_energy = d.pop("glcmJointEnergy", UNSET)

        glcm_joint_entropy = d.pop("glcmJointEntropy", UNSET)

        glcm_max_probabilities = d.pop("glcmMaxProbabilities", UNSET)

        glcm_sum_average = d.pop("glcmSumAverage", UNSET)

        glcm_sum_entropy = d.pop("glcmSumEntropy", UNSET)

        glcm_sum_squares = d.pop("glcmSumSquares", UNSET)

        glrlm_gray_level_non_uniformity = d.pop("glrlmGrayLevelNonUniformity", UNSET)

        glrlm_gray_level_non_uniformity_normalized = d.pop("glrlmGrayLevelNonUniformityNormalized", UNSET)

        glrlm_gray_level_variance = d.pop("glrlmGrayLevelVariance", UNSET)

        glrlm_high_gray_level_run_emphasis = d.pop("glrlmHighGrayLevelRunEmphasis", UNSET)

        glrlm_long_run_emphasis = d.pop("glrlmLongRunEmphasis", UNSET)

        glrlm_long_run_high_gray_level_emphasis = d.pop("glrlmLongRunHighGrayLevelEmphasis", UNSET)

        glrlm_long_run_low_gray_level_emphasis = d.pop("glrlmLongRunLowGrayLevelEmphasis", UNSET)

        glrlm_low_gray_level_run_emphasis = d.pop("glrlmLowGrayLevelRunEmphasis", UNSET)

        glrlm_run_entropy = d.pop("glrlmRunEntropy", UNSET)

        glrlm_run_length_non_uniformity = d.pop("glrlmRunLengthNonUniformity", UNSET)

        glrlm_run_length_non_uniformity_normalized = d.pop("glrlmRunLengthNonUniformityNormalized", UNSET)

        glrlm_run_percentage = d.pop("glrlmRunPercentage", UNSET)

        glrlm_run_variance = d.pop("glrlmRunVariance", UNSET)

        glrlm_short_run_emphasis = d.pop("glrlmShortRunEmphasis", UNSET)

        glrlm_short_run_high_gray_level_emphasis = d.pop("glrlmShortRunHighGrayLevelEmphasis", UNSET)

        glrlm_short_run_low_gray_level_emphasis = d.pop("glrlmShortRunLowGrayLevelEmphasis", UNSET)

        glszm_gray_level_non_uniformity = d.pop("glszmGrayLevelNonUniformity", UNSET)

        glszm_gray_level_non_uniformity_normalized = d.pop("glszmGrayLevelNonUniformityNormalized", UNSET)

        glszm_gray_level_variance = d.pop("glszmGrayLevelVariance", UNSET)

        glszm_high_gray_level_zone_emphasis = d.pop("glszmHighGrayLevelZoneEmphasis", UNSET)

        glszm_large_area_emphasis = d.pop("glszmLargeAreaEmphasis", UNSET)

        glszm_large_area_high_gray_level_emphasis = d.pop("glszmLargeAreaHighGrayLevelEmphasis", UNSET)

        glszm_large_area_low_gray_level_emphasis = d.pop("glszmLargeAreaLowGrayLevelEmphasis", UNSET)

        glszm_low_gray_level_zone_emphasis = d.pop("glszmLowGrayLevelZoneEmphasis", UNSET)

        glszm_size_zone_non_uniformity = d.pop("glszmSizeZoneNonUniformity", UNSET)

        glszm_size_zone_non_uniformity_normalized = d.pop("glszmSizeZoneNonUniformityNormalized", UNSET)

        glszm_small_area_emphasis = d.pop("glszmSmallAreaEmphasis", UNSET)

        glszm_small_area_high_gray_level_emphasis = d.pop("glszmSmallAreaHighGrayLevelEmphasis", UNSET)

        glszm_small_area_low_gray_level_emphasis = d.pop("glszmSmallAreaLowGrayLevelEmphasis", UNSET)

        glszm_zone_entropy = d.pop("glszmZoneEntropy", UNSET)

        glszm_zone_percentage = d.pop("glszmZonePercentage", UNSET)

        glszm_zone_variance = d.pop("glszmZoneVariance", UNSET)

        ngtdm_busyness = d.pop("ngtdmBusyness", UNSET)

        ngtdm_coarseness = d.pop("ngtdmCoarseness", UNSET)

        ngtdm_complexity = d.pop("ngtdmComplexity", UNSET)

        ngtdm_contrast = d.pop("ngtdmContrast", UNSET)

        ngtdm_strength = d.pop("ngtdmStrength", UNSET)

        gldm_dependence_entropy = d.pop("gldmDependenceEntropy", UNSET)

        gldm_dependence_non_uniformity = d.pop("gldmDependenceNonUniformity", UNSET)

        gldm_dependence_non_uniformity_normalized = d.pop("gldmDependenceNonUniformityNormalized", UNSET)

        gldm_dependence_variance = d.pop("gldmDependenceVariance", UNSET)

        gldm_gray_level_non_uniformity = d.pop("gldmGrayLevelNonUniformity", UNSET)

        gldm_gray_level_variance = d.pop("gldmGrayLevelVariance", UNSET)

        gldm_high_gray_level_emphasis = d.pop("gldmHighGrayLevelEmphasis", UNSET)

        gldm_large_dependence_emphasis = d.pop("gldmLargeDependenceEmphasis", UNSET)

        gldm_large_dependence_high_gray_level_emphasis = d.pop("gldmLargeDependenceHighGrayLevelEmphasis", UNSET)

        gldm_large_dependence_low_gray_level_emphasis = d.pop("gldmLargeDependenceLowGrayLevelEmphasis", UNSET)

        gldm_low_gray_level_emphasis = d.pop("gldmLowGrayLevelEmphasis", UNSET)

        gldm_small_dependence_emphasis = d.pop("gldmSmallDependenceEmphasis", UNSET)

        gldm_small_dependence_high_gray_level_emphasis = d.pop("gldmSmallDependenceHighGrayLevelEmphasis", UNSET)

        gldm_small_dependence_low_gray_level_emphasis = d.pop("gldmSmallDependenceLowGrayLevelEmphasis", UNSET)

        nslices = d.pop("nslices", UNSET)

        image_creation_dto = cls(
            sex=sex,
            age_years=age_years,
            study_date=study_date,
            kvp=kvp,
            exposure_mas=exposure_mas,
            convolution_kernel=convolution_kernel,
            slice_thickness_mm=slice_thickness_mm,
            pixel_spacing_mm=pixel_spacing_mm,
            manufacturer=manufacturer,
            manufacturer_model=manufacturer_model,
            software_version=software_version,
            rows=rows,
            columns=columns,
            has_segmentation=has_segmentation,
            shape_mesh_volume=shape_mesh_volume,
            shape_voxel_volume=shape_voxel_volume,
            shape_surface_area=shape_surface_area,
            shape_sphericity=shape_sphericity,
            shape_compactness_1=shape_compactness_1,
            shape_compactness_2=shape_compactness_2,
            shape_maximum_3_d_diameter=shape_maximum_3_d_diameter,
            shape_major_axis_length=shape_major_axis_length,
            shape_minor_axis_length=shape_minor_axis_length,
            shape_least_axis_length=shape_least_axis_length,
            shape_elongation=shape_elongation,
            shape_flatness=shape_flatness,
            first_energy=first_energy,
            first_total_energy=first_total_energy,
            first_entropy=first_entropy,
            first_minimum=first_minimum,
            first_10_th_percentile=first_10_th_percentile,
            first_90_th_percentile=first_90_th_percentile,
            first_maximum=first_maximum,
            first_mean=first_mean,
            first_median=first_median,
            first_interquartile_range=first_interquartile_range,
            first_range=first_range,
            first_mean_absolute_deviation=first_mean_absolute_deviation,
            first_robust_mean_absolute_deviation=first_robust_mean_absolute_deviation,
            first_root_mean_squared=first_root_mean_squared,
            first_skewness=first_skewness,
            first_kurtosis=first_kurtosis,
            first_variance=first_variance,
            first_uniformity=first_uniformity,
            glcm_autocorrelation=glcm_autocorrelation,
            glcm_cluster_prominence=glcm_cluster_prominence,
            glcm_cluster_shade=glcm_cluster_shade,
            glcm_cluster_tendency=glcm_cluster_tendency,
            glcm_contrast=glcm_contrast,
            glcm_correlation=glcm_correlation,
            glcm_difference_average=glcm_difference_average,
            glcm_difference_entropy=glcm_difference_entropy,
            glcm_difference_variance=glcm_difference_variance,
            glcm_id=glcm_id,
            glcm_idm=glcm_idm,
            glcm_idmn=glcm_idmn,
            glcm_idn=glcm_idn,
            glcm_imc_1=glcm_imc_1,
            glcm_imc_2=glcm_imc_2,
            glcm_inverse_variance=glcm_inverse_variance,
            glcm_joint_average=glcm_joint_average,
            glcm_joint_energy=glcm_joint_energy,
            glcm_joint_entropy=glcm_joint_entropy,
            glcm_max_probabilities=glcm_max_probabilities,
            glcm_sum_average=glcm_sum_average,
            glcm_sum_entropy=glcm_sum_entropy,
            glcm_sum_squares=glcm_sum_squares,
            glrlm_gray_level_non_uniformity=glrlm_gray_level_non_uniformity,
            glrlm_gray_level_non_uniformity_normalized=glrlm_gray_level_non_uniformity_normalized,
            glrlm_gray_level_variance=glrlm_gray_level_variance,
            glrlm_high_gray_level_run_emphasis=glrlm_high_gray_level_run_emphasis,
            glrlm_long_run_emphasis=glrlm_long_run_emphasis,
            glrlm_long_run_high_gray_level_emphasis=glrlm_long_run_high_gray_level_emphasis,
            glrlm_long_run_low_gray_level_emphasis=glrlm_long_run_low_gray_level_emphasis,
            glrlm_low_gray_level_run_emphasis=glrlm_low_gray_level_run_emphasis,
            glrlm_run_entropy=glrlm_run_entropy,
            glrlm_run_length_non_uniformity=glrlm_run_length_non_uniformity,
            glrlm_run_length_non_uniformity_normalized=glrlm_run_length_non_uniformity_normalized,
            glrlm_run_percentage=glrlm_run_percentage,
            glrlm_run_variance=glrlm_run_variance,
            glrlm_short_run_emphasis=glrlm_short_run_emphasis,
            glrlm_short_run_high_gray_level_emphasis=glrlm_short_run_high_gray_level_emphasis,
            glrlm_short_run_low_gray_level_emphasis=glrlm_short_run_low_gray_level_emphasis,
            glszm_gray_level_non_uniformity=glszm_gray_level_non_uniformity,
            glszm_gray_level_non_uniformity_normalized=glszm_gray_level_non_uniformity_normalized,
            glszm_gray_level_variance=glszm_gray_level_variance,
            glszm_high_gray_level_zone_emphasis=glszm_high_gray_level_zone_emphasis,
            glszm_large_area_emphasis=glszm_large_area_emphasis,
            glszm_large_area_high_gray_level_emphasis=glszm_large_area_high_gray_level_emphasis,
            glszm_large_area_low_gray_level_emphasis=glszm_large_area_low_gray_level_emphasis,
            glszm_low_gray_level_zone_emphasis=glszm_low_gray_level_zone_emphasis,
            glszm_size_zone_non_uniformity=glszm_size_zone_non_uniformity,
            glszm_size_zone_non_uniformity_normalized=glszm_size_zone_non_uniformity_normalized,
            glszm_small_area_emphasis=glszm_small_area_emphasis,
            glszm_small_area_high_gray_level_emphasis=glszm_small_area_high_gray_level_emphasis,
            glszm_small_area_low_gray_level_emphasis=glszm_small_area_low_gray_level_emphasis,
            glszm_zone_entropy=glszm_zone_entropy,
            glszm_zone_percentage=glszm_zone_percentage,
            glszm_zone_variance=glszm_zone_variance,
            ngtdm_busyness=ngtdm_busyness,
            ngtdm_coarseness=ngtdm_coarseness,
            ngtdm_complexity=ngtdm_complexity,
            ngtdm_contrast=ngtdm_contrast,
            ngtdm_strength=ngtdm_strength,
            gldm_dependence_entropy=gldm_dependence_entropy,
            gldm_dependence_non_uniformity=gldm_dependence_non_uniformity,
            gldm_dependence_non_uniformity_normalized=gldm_dependence_non_uniformity_normalized,
            gldm_dependence_variance=gldm_dependence_variance,
            gldm_gray_level_non_uniformity=gldm_gray_level_non_uniformity,
            gldm_gray_level_variance=gldm_gray_level_variance,
            gldm_high_gray_level_emphasis=gldm_high_gray_level_emphasis,
            gldm_large_dependence_emphasis=gldm_large_dependence_emphasis,
            gldm_large_dependence_high_gray_level_emphasis=gldm_large_dependence_high_gray_level_emphasis,
            gldm_large_dependence_low_gray_level_emphasis=gldm_large_dependence_low_gray_level_emphasis,
            gldm_low_gray_level_emphasis=gldm_low_gray_level_emphasis,
            gldm_small_dependence_emphasis=gldm_small_dependence_emphasis,
            gldm_small_dependence_high_gray_level_emphasis=gldm_small_dependence_high_gray_level_emphasis,
            gldm_small_dependence_low_gray_level_emphasis=gldm_small_dependence_low_gray_level_emphasis,
            nslices=nslices,
        )

        image_creation_dto.additional_properties = d
        return image_creation_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
