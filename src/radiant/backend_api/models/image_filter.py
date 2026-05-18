from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageFilter")


@_attrs_define
class ImageFilter:
    """
    Attributes:
        dataset_id (UUID | Unset):
        sex (str | Unset):
        convolution_kernel (str | Unset):
        manufacturer (str | Unset):
        manufacturer_model (str | Unset):
        software_version (str | Unset):
        has_segmentation (bool | Unset):
        age_years_min (int | Unset):
        age_years_max (int | Unset):
        study_date_min (datetime.date | Unset):
        study_date_max (datetime.date | Unset):
        kvp_min (float | Unset):
        kvp_max (float | Unset):
        exposure_mas_min (float | Unset):
        exposure_mas_max (float | Unset):
        slice_thickness_mm_min (float | Unset):
        slice_thickness_mm_max (float | Unset):
        pixel_spacing_mm_min (float | Unset):
        pixel_spacing_mm_max (float | Unset):
        rows_min (int | Unset):
        rows_max (int | Unset):
        columns_min (int | Unset):
        columns_max (int | Unset):
        n_slices_min (int | Unset):
        n_slices_max (int | Unset):
        shape_mesh_volume_min (float | Unset):
        shape_mesh_volume_max (float | Unset):
        shape_voxel_volume_min (float | Unset):
        shape_voxel_volume_max (float | Unset):
        shape_surface_area_min (float | Unset):
        shape_surface_area_max (float | Unset):
        shape_sphericity_min (float | Unset):
        shape_sphericity_max (float | Unset):
        shape_compactness_1_min (float | Unset):
        shape_compactness_1_max (float | Unset):
        shape_compactness_2_min (float | Unset):
        shape_compactness_2_max (float | Unset):
        shape_maximum_3_d_diameter_min (float | Unset):
        shape_maximum_3_d_diameter_max (float | Unset):
        shape_major_axis_length_min (float | Unset):
        shape_major_axis_length_max (float | Unset):
        shape_minor_axis_length_min (float | Unset):
        shape_minor_axis_length_max (float | Unset):
        shape_least_axis_length_min (float | Unset):
        shape_least_axis_length_max (float | Unset):
        shape_elongation_min (float | Unset):
        shape_elongation_max (float | Unset):
        shape_flatness_min (float | Unset):
        shape_flatness_max (float | Unset):
        first_energy_min (float | Unset):
        first_energy_max (float | Unset):
        first_total_energy_min (float | Unset):
        first_total_energy_max (float | Unset):
        first_entropy_min (float | Unset):
        first_entropy_max (float | Unset):
        first_minimum_min (float | Unset):
        first_minimum_max (float | Unset):
        first_10_th_percentile_min (float | Unset):
        first_10_th_percentile_max (float | Unset):
        first_90_th_percentile_min (float | Unset):
        first_90_th_percentile_max (float | Unset):
        first_maximum_min (float | Unset):
        first_maximum_max (float | Unset):
        first_mean_min (float | Unset):
        first_mean_max (float | Unset):
        first_median_min (float | Unset):
        first_median_max (float | Unset):
        first_interquartile_range_min (float | Unset):
        first_interquartile_range_max (float | Unset):
        first_range_min (float | Unset):
        first_range_max (float | Unset):
        first_mean_absolute_deviation_min (float | Unset):
        first_mean_absolute_deviation_max (float | Unset):
        first_robust_mean_absolute_deviation_min (float | Unset):
        first_robust_mean_absolute_deviation_max (float | Unset):
        first_root_mean_squared_min (float | Unset):
        first_root_mean_squared_max (float | Unset):
        first_skewness_min (float | Unset):
        first_skewness_max (float | Unset):
        first_kurtosis_min (float | Unset):
        first_kurtosis_max (float | Unset):
        first_variance_min (float | Unset):
        first_variance_max (float | Unset):
        first_uniformity_min (float | Unset):
        first_uniformity_max (float | Unset):
        glcm_autocorrelation_min (float | Unset):
        glcm_autocorrelation_max (float | Unset):
        glcm_cluster_prominence_min (float | Unset):
        glcm_cluster_prominence_max (float | Unset):
        glcm_cluster_shade_min (float | Unset):
        glcm_cluster_shade_max (float | Unset):
        glcm_cluster_tendency_min (float | Unset):
        glcm_cluster_tendency_max (float | Unset):
        glcm_contrast_min (float | Unset):
        glcm_contrast_max (float | Unset):
        glcm_correlation_min (float | Unset):
        glcm_correlation_max (float | Unset):
        glcm_difference_average_min (float | Unset):
        glcm_difference_average_max (float | Unset):
        glcm_difference_entropy_min (float | Unset):
        glcm_difference_entropy_max (float | Unset):
        glcm_difference_variance_min (float | Unset):
        glcm_difference_variance_max (float | Unset):
        glcm_id_min (float | Unset):
        glcm_id_max (float | Unset):
        glcm_idm_min (float | Unset):
        glcm_idm_max (float | Unset):
        glcm_idmn_min (float | Unset):
        glcm_idmn_max (float | Unset):
        glcm_idn_min (float | Unset):
        glcm_idn_max (float | Unset):
        glcm_imc_1_min (float | Unset):
        glcm_imc_1_max (float | Unset):
        glcm_imc_2_min (float | Unset):
        glcm_imc_2_max (float | Unset):
        glcm_inverse_variance_min (float | Unset):
        glcm_inverse_variance_max (float | Unset):
        glcm_joint_average_min (float | Unset):
        glcm_joint_average_max (float | Unset):
        glcm_joint_energy_min (float | Unset):
        glcm_joint_energy_max (float | Unset):
        glcm_joint_entropy_min (float | Unset):
        glcm_joint_entropy_max (float | Unset):
        glcm_max_probabilities_min (float | Unset):
        glcm_max_probabilities_max (float | Unset):
        glcm_sum_average_min (float | Unset):
        glcm_sum_average_max (float | Unset):
        glcm_sum_entropy_min (float | Unset):
        glcm_sum_entropy_max (float | Unset):
        glcm_sum_squares_min (float | Unset):
        glcm_sum_squares_max (float | Unset):
        glrlm_gray_level_non_uniformity_min (float | Unset):
        glrlm_gray_level_non_uniformity_max (float | Unset):
        glrlm_gray_level_non_uniformity_normalized_min (float | Unset):
        glrlm_gray_level_non_uniformity_normalized_max (float | Unset):
        glrlm_gray_level_variance_min (float | Unset):
        glrlm_gray_level_variance_max (float | Unset):
        glrlm_high_gray_level_run_emphasis_min (float | Unset):
        glrlm_high_gray_level_run_emphasis_max (float | Unset):
        glrlm_long_run_emphasis_min (float | Unset):
        glrlm_long_run_emphasis_max (float | Unset):
        glrlm_long_run_high_gray_level_emphasis_min (float | Unset):
        glrlm_long_run_high_gray_level_emphasis_max (float | Unset):
        glrlm_long_run_low_gray_level_emphasis_min (float | Unset):
        glrlm_long_run_low_gray_level_emphasis_max (float | Unset):
        glrlm_low_gray_level_run_emphasis_min (float | Unset):
        glrlm_low_gray_level_run_emphasis_max (float | Unset):
        glrlm_run_entropy_min (float | Unset):
        glrlm_run_entropy_max (float | Unset):
        glrlm_run_length_non_uniformity_min (float | Unset):
        glrlm_run_length_non_uniformity_max (float | Unset):
        glrlm_run_length_non_uniformity_normalized_min (float | Unset):
        glrlm_run_length_non_uniformity_normalized_max (float | Unset):
        glrlm_run_percentage_min (float | Unset):
        glrlm_run_percentage_max (float | Unset):
        glrlm_run_variance_min (float | Unset):
        glrlm_run_variance_max (float | Unset):
        glrlm_short_run_emphasis_min (float | Unset):
        glrlm_short_run_emphasis_max (float | Unset):
        glrlm_short_run_high_gray_level_emphasis_min (float | Unset):
        glrlm_short_run_high_gray_level_emphasis_max (float | Unset):
        glrlm_short_run_low_gray_level_emphasis_min (float | Unset):
        glrlm_short_run_low_gray_level_emphasis_max (float | Unset):
        glszm_gray_level_non_uniformity_min (float | Unset):
        glszm_gray_level_non_uniformity_max (float | Unset):
        glszm_gray_level_non_uniformity_normalized_min (float | Unset):
        glszm_gray_level_non_uniformity_normalized_max (float | Unset):
        glszm_gray_level_variance_min (float | Unset):
        glszm_gray_level_variance_max (float | Unset):
        glszm_high_gray_level_zone_emphasis_min (float | Unset):
        glszm_high_gray_level_zone_emphasis_max (float | Unset):
        glszm_large_area_emphasis_min (float | Unset):
        glszm_large_area_emphasis_max (float | Unset):
        glszm_large_area_high_gray_level_emphasis_min (float | Unset):
        glszm_large_area_high_gray_level_emphasis_max (float | Unset):
        glszm_large_area_low_gray_level_emphasis_min (float | Unset):
        glszm_large_area_low_gray_level_emphasis_max (float | Unset):
        glszm_low_gray_level_zone_emphasis_min (float | Unset):
        glszm_low_gray_level_zone_emphasis_max (float | Unset):
        glszm_size_zone_non_uniformity_min (float | Unset):
        glszm_size_zone_non_uniformity_max (float | Unset):
        glszm_size_zone_non_uniformity_normalized_min (float | Unset):
        glszm_size_zone_non_uniformity_normalized_max (float | Unset):
        glszm_small_area_emphasis_min (float | Unset):
        glszm_small_area_emphasis_max (float | Unset):
        glszm_small_area_high_gray_level_emphasis_min (float | Unset):
        glszm_small_area_high_gray_level_emphasis_max (float | Unset):
        glszm_small_area_low_gray_level_emphasis_min (float | Unset):
        glszm_small_area_low_gray_level_emphasis_max (float | Unset):
        glszm_zone_entropy_min (float | Unset):
        glszm_zone_entropy_max (float | Unset):
        glszm_zone_percentage_min (float | Unset):
        glszm_zone_percentage_max (float | Unset):
        glszm_zone_variance_min (float | Unset):
        glszm_zone_variance_max (float | Unset):
        ngtdm_busyness_min (float | Unset):
        ngtdm_busyness_max (float | Unset):
        ngtdm_coarseness_min (float | Unset):
        ngtdm_coarseness_max (float | Unset):
        ngtdm_complexity_min (float | Unset):
        ngtdm_complexity_max (float | Unset):
        ngtdm_contrast_min (float | Unset):
        ngtdm_contrast_max (float | Unset):
        ngtdm_strength_min (float | Unset):
        ngtdm_strength_max (float | Unset):
        gldm_dependence_entropy_min (float | Unset):
        gldm_dependence_entropy_max (float | Unset):
        gldm_dependence_non_uniformity_min (float | Unset):
        gldm_dependence_non_uniformity_max (float | Unset):
        gldm_dependence_non_uniformity_normalized_min (float | Unset):
        gldm_dependence_non_uniformity_normalized_max (float | Unset):
        gldm_dependence_variance_min (float | Unset):
        gldm_dependence_variance_max (float | Unset):
        gldm_gray_level_non_uniformity_min (float | Unset):
        gldm_gray_level_non_uniformity_max (float | Unset):
        gldm_gray_level_variance_min (float | Unset):
        gldm_gray_level_variance_max (float | Unset):
        gldm_high_gray_level_emphasis_min (float | Unset):
        gldm_high_gray_level_emphasis_max (float | Unset):
        gldm_large_dependence_emphasis_min (float | Unset):
        gldm_large_dependence_emphasis_max (float | Unset):
        gldm_large_dependence_high_gray_level_emphasis_min (float | Unset):
        gldm_large_dependence_high_gray_level_emphasis_max (float | Unset):
        gldm_large_dependence_low_gray_level_emphasis_min (float | Unset):
        gldm_large_dependence_low_gray_level_emphasis_max (float | Unset):
        gldm_low_gray_level_emphasis_min (float | Unset):
        gldm_low_gray_level_emphasis_max (float | Unset):
        gldm_small_dependence_emphasis_min (float | Unset):
        gldm_small_dependence_emphasis_max (float | Unset):
        gldm_small_dependence_high_gray_level_emphasis_min (float | Unset):
        gldm_small_dependence_high_gray_level_emphasis_max (float | Unset):
        gldm_small_dependence_low_gray_level_emphasis_min (float | Unset):
        gldm_small_dependence_low_gray_level_emphasis_max (float | Unset):
    """

    dataset_id: UUID | Unset = UNSET
    sex: str | Unset = UNSET
    convolution_kernel: str | Unset = UNSET
    manufacturer: str | Unset = UNSET
    manufacturer_model: str | Unset = UNSET
    software_version: str | Unset = UNSET
    has_segmentation: bool | Unset = UNSET
    age_years_min: int | Unset = UNSET
    age_years_max: int | Unset = UNSET
    study_date_min: datetime.date | Unset = UNSET
    study_date_max: datetime.date | Unset = UNSET
    kvp_min: float | Unset = UNSET
    kvp_max: float | Unset = UNSET
    exposure_mas_min: float | Unset = UNSET
    exposure_mas_max: float | Unset = UNSET
    slice_thickness_mm_min: float | Unset = UNSET
    slice_thickness_mm_max: float | Unset = UNSET
    pixel_spacing_mm_min: float | Unset = UNSET
    pixel_spacing_mm_max: float | Unset = UNSET
    rows_min: int | Unset = UNSET
    rows_max: int | Unset = UNSET
    columns_min: int | Unset = UNSET
    columns_max: int | Unset = UNSET
    n_slices_min: int | Unset = UNSET
    n_slices_max: int | Unset = UNSET
    shape_mesh_volume_min: float | Unset = UNSET
    shape_mesh_volume_max: float | Unset = UNSET
    shape_voxel_volume_min: float | Unset = UNSET
    shape_voxel_volume_max: float | Unset = UNSET
    shape_surface_area_min: float | Unset = UNSET
    shape_surface_area_max: float | Unset = UNSET
    shape_sphericity_min: float | Unset = UNSET
    shape_sphericity_max: float | Unset = UNSET
    shape_compactness_1_min: float | Unset = UNSET
    shape_compactness_1_max: float | Unset = UNSET
    shape_compactness_2_min: float | Unset = UNSET
    shape_compactness_2_max: float | Unset = UNSET
    shape_maximum_3_d_diameter_min: float | Unset = UNSET
    shape_maximum_3_d_diameter_max: float | Unset = UNSET
    shape_major_axis_length_min: float | Unset = UNSET
    shape_major_axis_length_max: float | Unset = UNSET
    shape_minor_axis_length_min: float | Unset = UNSET
    shape_minor_axis_length_max: float | Unset = UNSET
    shape_least_axis_length_min: float | Unset = UNSET
    shape_least_axis_length_max: float | Unset = UNSET
    shape_elongation_min: float | Unset = UNSET
    shape_elongation_max: float | Unset = UNSET
    shape_flatness_min: float | Unset = UNSET
    shape_flatness_max: float | Unset = UNSET
    first_energy_min: float | Unset = UNSET
    first_energy_max: float | Unset = UNSET
    first_total_energy_min: float | Unset = UNSET
    first_total_energy_max: float | Unset = UNSET
    first_entropy_min: float | Unset = UNSET
    first_entropy_max: float | Unset = UNSET
    first_minimum_min: float | Unset = UNSET
    first_minimum_max: float | Unset = UNSET
    first_10_th_percentile_min: float | Unset = UNSET
    first_10_th_percentile_max: float | Unset = UNSET
    first_90_th_percentile_min: float | Unset = UNSET
    first_90_th_percentile_max: float | Unset = UNSET
    first_maximum_min: float | Unset = UNSET
    first_maximum_max: float | Unset = UNSET
    first_mean_min: float | Unset = UNSET
    first_mean_max: float | Unset = UNSET
    first_median_min: float | Unset = UNSET
    first_median_max: float | Unset = UNSET
    first_interquartile_range_min: float | Unset = UNSET
    first_interquartile_range_max: float | Unset = UNSET
    first_range_min: float | Unset = UNSET
    first_range_max: float | Unset = UNSET
    first_mean_absolute_deviation_min: float | Unset = UNSET
    first_mean_absolute_deviation_max: float | Unset = UNSET
    first_robust_mean_absolute_deviation_min: float | Unset = UNSET
    first_robust_mean_absolute_deviation_max: float | Unset = UNSET
    first_root_mean_squared_min: float | Unset = UNSET
    first_root_mean_squared_max: float | Unset = UNSET
    first_skewness_min: float | Unset = UNSET
    first_skewness_max: float | Unset = UNSET
    first_kurtosis_min: float | Unset = UNSET
    first_kurtosis_max: float | Unset = UNSET
    first_variance_min: float | Unset = UNSET
    first_variance_max: float | Unset = UNSET
    first_uniformity_min: float | Unset = UNSET
    first_uniformity_max: float | Unset = UNSET
    glcm_autocorrelation_min: float | Unset = UNSET
    glcm_autocorrelation_max: float | Unset = UNSET
    glcm_cluster_prominence_min: float | Unset = UNSET
    glcm_cluster_prominence_max: float | Unset = UNSET
    glcm_cluster_shade_min: float | Unset = UNSET
    glcm_cluster_shade_max: float | Unset = UNSET
    glcm_cluster_tendency_min: float | Unset = UNSET
    glcm_cluster_tendency_max: float | Unset = UNSET
    glcm_contrast_min: float | Unset = UNSET
    glcm_contrast_max: float | Unset = UNSET
    glcm_correlation_min: float | Unset = UNSET
    glcm_correlation_max: float | Unset = UNSET
    glcm_difference_average_min: float | Unset = UNSET
    glcm_difference_average_max: float | Unset = UNSET
    glcm_difference_entropy_min: float | Unset = UNSET
    glcm_difference_entropy_max: float | Unset = UNSET
    glcm_difference_variance_min: float | Unset = UNSET
    glcm_difference_variance_max: float | Unset = UNSET
    glcm_id_min: float | Unset = UNSET
    glcm_id_max: float | Unset = UNSET
    glcm_idm_min: float | Unset = UNSET
    glcm_idm_max: float | Unset = UNSET
    glcm_idmn_min: float | Unset = UNSET
    glcm_idmn_max: float | Unset = UNSET
    glcm_idn_min: float | Unset = UNSET
    glcm_idn_max: float | Unset = UNSET
    glcm_imc_1_min: float | Unset = UNSET
    glcm_imc_1_max: float | Unset = UNSET
    glcm_imc_2_min: float | Unset = UNSET
    glcm_imc_2_max: float | Unset = UNSET
    glcm_inverse_variance_min: float | Unset = UNSET
    glcm_inverse_variance_max: float | Unset = UNSET
    glcm_joint_average_min: float | Unset = UNSET
    glcm_joint_average_max: float | Unset = UNSET
    glcm_joint_energy_min: float | Unset = UNSET
    glcm_joint_energy_max: float | Unset = UNSET
    glcm_joint_entropy_min: float | Unset = UNSET
    glcm_joint_entropy_max: float | Unset = UNSET
    glcm_max_probabilities_min: float | Unset = UNSET
    glcm_max_probabilities_max: float | Unset = UNSET
    glcm_sum_average_min: float | Unset = UNSET
    glcm_sum_average_max: float | Unset = UNSET
    glcm_sum_entropy_min: float | Unset = UNSET
    glcm_sum_entropy_max: float | Unset = UNSET
    glcm_sum_squares_min: float | Unset = UNSET
    glcm_sum_squares_max: float | Unset = UNSET
    glrlm_gray_level_non_uniformity_min: float | Unset = UNSET
    glrlm_gray_level_non_uniformity_max: float | Unset = UNSET
    glrlm_gray_level_non_uniformity_normalized_min: float | Unset = UNSET
    glrlm_gray_level_non_uniformity_normalized_max: float | Unset = UNSET
    glrlm_gray_level_variance_min: float | Unset = UNSET
    glrlm_gray_level_variance_max: float | Unset = UNSET
    glrlm_high_gray_level_run_emphasis_min: float | Unset = UNSET
    glrlm_high_gray_level_run_emphasis_max: float | Unset = UNSET
    glrlm_long_run_emphasis_min: float | Unset = UNSET
    glrlm_long_run_emphasis_max: float | Unset = UNSET
    glrlm_long_run_high_gray_level_emphasis_min: float | Unset = UNSET
    glrlm_long_run_high_gray_level_emphasis_max: float | Unset = UNSET
    glrlm_long_run_low_gray_level_emphasis_min: float | Unset = UNSET
    glrlm_long_run_low_gray_level_emphasis_max: float | Unset = UNSET
    glrlm_low_gray_level_run_emphasis_min: float | Unset = UNSET
    glrlm_low_gray_level_run_emphasis_max: float | Unset = UNSET
    glrlm_run_entropy_min: float | Unset = UNSET
    glrlm_run_entropy_max: float | Unset = UNSET
    glrlm_run_length_non_uniformity_min: float | Unset = UNSET
    glrlm_run_length_non_uniformity_max: float | Unset = UNSET
    glrlm_run_length_non_uniformity_normalized_min: float | Unset = UNSET
    glrlm_run_length_non_uniformity_normalized_max: float | Unset = UNSET
    glrlm_run_percentage_min: float | Unset = UNSET
    glrlm_run_percentage_max: float | Unset = UNSET
    glrlm_run_variance_min: float | Unset = UNSET
    glrlm_run_variance_max: float | Unset = UNSET
    glrlm_short_run_emphasis_min: float | Unset = UNSET
    glrlm_short_run_emphasis_max: float | Unset = UNSET
    glrlm_short_run_high_gray_level_emphasis_min: float | Unset = UNSET
    glrlm_short_run_high_gray_level_emphasis_max: float | Unset = UNSET
    glrlm_short_run_low_gray_level_emphasis_min: float | Unset = UNSET
    glrlm_short_run_low_gray_level_emphasis_max: float | Unset = UNSET
    glszm_gray_level_non_uniformity_min: float | Unset = UNSET
    glszm_gray_level_non_uniformity_max: float | Unset = UNSET
    glszm_gray_level_non_uniformity_normalized_min: float | Unset = UNSET
    glszm_gray_level_non_uniformity_normalized_max: float | Unset = UNSET
    glszm_gray_level_variance_min: float | Unset = UNSET
    glszm_gray_level_variance_max: float | Unset = UNSET
    glszm_high_gray_level_zone_emphasis_min: float | Unset = UNSET
    glszm_high_gray_level_zone_emphasis_max: float | Unset = UNSET
    glszm_large_area_emphasis_min: float | Unset = UNSET
    glszm_large_area_emphasis_max: float | Unset = UNSET
    glszm_large_area_high_gray_level_emphasis_min: float | Unset = UNSET
    glszm_large_area_high_gray_level_emphasis_max: float | Unset = UNSET
    glszm_large_area_low_gray_level_emphasis_min: float | Unset = UNSET
    glszm_large_area_low_gray_level_emphasis_max: float | Unset = UNSET
    glszm_low_gray_level_zone_emphasis_min: float | Unset = UNSET
    glszm_low_gray_level_zone_emphasis_max: float | Unset = UNSET
    glszm_size_zone_non_uniformity_min: float | Unset = UNSET
    glszm_size_zone_non_uniformity_max: float | Unset = UNSET
    glszm_size_zone_non_uniformity_normalized_min: float | Unset = UNSET
    glszm_size_zone_non_uniformity_normalized_max: float | Unset = UNSET
    glszm_small_area_emphasis_min: float | Unset = UNSET
    glszm_small_area_emphasis_max: float | Unset = UNSET
    glszm_small_area_high_gray_level_emphasis_min: float | Unset = UNSET
    glszm_small_area_high_gray_level_emphasis_max: float | Unset = UNSET
    glszm_small_area_low_gray_level_emphasis_min: float | Unset = UNSET
    glszm_small_area_low_gray_level_emphasis_max: float | Unset = UNSET
    glszm_zone_entropy_min: float | Unset = UNSET
    glszm_zone_entropy_max: float | Unset = UNSET
    glszm_zone_percentage_min: float | Unset = UNSET
    glszm_zone_percentage_max: float | Unset = UNSET
    glszm_zone_variance_min: float | Unset = UNSET
    glszm_zone_variance_max: float | Unset = UNSET
    ngtdm_busyness_min: float | Unset = UNSET
    ngtdm_busyness_max: float | Unset = UNSET
    ngtdm_coarseness_min: float | Unset = UNSET
    ngtdm_coarseness_max: float | Unset = UNSET
    ngtdm_complexity_min: float | Unset = UNSET
    ngtdm_complexity_max: float | Unset = UNSET
    ngtdm_contrast_min: float | Unset = UNSET
    ngtdm_contrast_max: float | Unset = UNSET
    ngtdm_strength_min: float | Unset = UNSET
    ngtdm_strength_max: float | Unset = UNSET
    gldm_dependence_entropy_min: float | Unset = UNSET
    gldm_dependence_entropy_max: float | Unset = UNSET
    gldm_dependence_non_uniformity_min: float | Unset = UNSET
    gldm_dependence_non_uniformity_max: float | Unset = UNSET
    gldm_dependence_non_uniformity_normalized_min: float | Unset = UNSET
    gldm_dependence_non_uniformity_normalized_max: float | Unset = UNSET
    gldm_dependence_variance_min: float | Unset = UNSET
    gldm_dependence_variance_max: float | Unset = UNSET
    gldm_gray_level_non_uniformity_min: float | Unset = UNSET
    gldm_gray_level_non_uniformity_max: float | Unset = UNSET
    gldm_gray_level_variance_min: float | Unset = UNSET
    gldm_gray_level_variance_max: float | Unset = UNSET
    gldm_high_gray_level_emphasis_min: float | Unset = UNSET
    gldm_high_gray_level_emphasis_max: float | Unset = UNSET
    gldm_large_dependence_emphasis_min: float | Unset = UNSET
    gldm_large_dependence_emphasis_max: float | Unset = UNSET
    gldm_large_dependence_high_gray_level_emphasis_min: float | Unset = UNSET
    gldm_large_dependence_high_gray_level_emphasis_max: float | Unset = UNSET
    gldm_large_dependence_low_gray_level_emphasis_min: float | Unset = UNSET
    gldm_large_dependence_low_gray_level_emphasis_max: float | Unset = UNSET
    gldm_low_gray_level_emphasis_min: float | Unset = UNSET
    gldm_low_gray_level_emphasis_max: float | Unset = UNSET
    gldm_small_dependence_emphasis_min: float | Unset = UNSET
    gldm_small_dependence_emphasis_max: float | Unset = UNSET
    gldm_small_dependence_high_gray_level_emphasis_min: float | Unset = UNSET
    gldm_small_dependence_high_gray_level_emphasis_max: float | Unset = UNSET
    gldm_small_dependence_low_gray_level_emphasis_min: float | Unset = UNSET
    gldm_small_dependence_low_gray_level_emphasis_max: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id: str | Unset = UNSET
        if not isinstance(self.dataset_id, Unset):
            dataset_id = str(self.dataset_id)

        sex = self.sex

        convolution_kernel = self.convolution_kernel

        manufacturer = self.manufacturer

        manufacturer_model = self.manufacturer_model

        software_version = self.software_version

        has_segmentation = self.has_segmentation

        age_years_min = self.age_years_min

        age_years_max = self.age_years_max

        study_date_min: str | Unset = UNSET
        if not isinstance(self.study_date_min, Unset):
            study_date_min = self.study_date_min.isoformat()

        study_date_max: str | Unset = UNSET
        if not isinstance(self.study_date_max, Unset):
            study_date_max = self.study_date_max.isoformat()

        kvp_min = self.kvp_min

        kvp_max = self.kvp_max

        exposure_mas_min = self.exposure_mas_min

        exposure_mas_max = self.exposure_mas_max

        slice_thickness_mm_min = self.slice_thickness_mm_min

        slice_thickness_mm_max = self.slice_thickness_mm_max

        pixel_spacing_mm_min = self.pixel_spacing_mm_min

        pixel_spacing_mm_max = self.pixel_spacing_mm_max

        rows_min = self.rows_min

        rows_max = self.rows_max

        columns_min = self.columns_min

        columns_max = self.columns_max

        n_slices_min = self.n_slices_min

        n_slices_max = self.n_slices_max

        shape_mesh_volume_min = self.shape_mesh_volume_min

        shape_mesh_volume_max = self.shape_mesh_volume_max

        shape_voxel_volume_min = self.shape_voxel_volume_min

        shape_voxel_volume_max = self.shape_voxel_volume_max

        shape_surface_area_min = self.shape_surface_area_min

        shape_surface_area_max = self.shape_surface_area_max

        shape_sphericity_min = self.shape_sphericity_min

        shape_sphericity_max = self.shape_sphericity_max

        shape_compactness_1_min = self.shape_compactness_1_min

        shape_compactness_1_max = self.shape_compactness_1_max

        shape_compactness_2_min = self.shape_compactness_2_min

        shape_compactness_2_max = self.shape_compactness_2_max

        shape_maximum_3_d_diameter_min = self.shape_maximum_3_d_diameter_min

        shape_maximum_3_d_diameter_max = self.shape_maximum_3_d_diameter_max

        shape_major_axis_length_min = self.shape_major_axis_length_min

        shape_major_axis_length_max = self.shape_major_axis_length_max

        shape_minor_axis_length_min = self.shape_minor_axis_length_min

        shape_minor_axis_length_max = self.shape_minor_axis_length_max

        shape_least_axis_length_min = self.shape_least_axis_length_min

        shape_least_axis_length_max = self.shape_least_axis_length_max

        shape_elongation_min = self.shape_elongation_min

        shape_elongation_max = self.shape_elongation_max

        shape_flatness_min = self.shape_flatness_min

        shape_flatness_max = self.shape_flatness_max

        first_energy_min = self.first_energy_min

        first_energy_max = self.first_energy_max

        first_total_energy_min = self.first_total_energy_min

        first_total_energy_max = self.first_total_energy_max

        first_entropy_min = self.first_entropy_min

        first_entropy_max = self.first_entropy_max

        first_minimum_min = self.first_minimum_min

        first_minimum_max = self.first_minimum_max

        first_10_th_percentile_min = self.first_10_th_percentile_min

        first_10_th_percentile_max = self.first_10_th_percentile_max

        first_90_th_percentile_min = self.first_90_th_percentile_min

        first_90_th_percentile_max = self.first_90_th_percentile_max

        first_maximum_min = self.first_maximum_min

        first_maximum_max = self.first_maximum_max

        first_mean_min = self.first_mean_min

        first_mean_max = self.first_mean_max

        first_median_min = self.first_median_min

        first_median_max = self.first_median_max

        first_interquartile_range_min = self.first_interquartile_range_min

        first_interquartile_range_max = self.first_interquartile_range_max

        first_range_min = self.first_range_min

        first_range_max = self.first_range_max

        first_mean_absolute_deviation_min = self.first_mean_absolute_deviation_min

        first_mean_absolute_deviation_max = self.first_mean_absolute_deviation_max

        first_robust_mean_absolute_deviation_min = self.first_robust_mean_absolute_deviation_min

        first_robust_mean_absolute_deviation_max = self.first_robust_mean_absolute_deviation_max

        first_root_mean_squared_min = self.first_root_mean_squared_min

        first_root_mean_squared_max = self.first_root_mean_squared_max

        first_skewness_min = self.first_skewness_min

        first_skewness_max = self.first_skewness_max

        first_kurtosis_min = self.first_kurtosis_min

        first_kurtosis_max = self.first_kurtosis_max

        first_variance_min = self.first_variance_min

        first_variance_max = self.first_variance_max

        first_uniformity_min = self.first_uniformity_min

        first_uniformity_max = self.first_uniformity_max

        glcm_autocorrelation_min = self.glcm_autocorrelation_min

        glcm_autocorrelation_max = self.glcm_autocorrelation_max

        glcm_cluster_prominence_min = self.glcm_cluster_prominence_min

        glcm_cluster_prominence_max = self.glcm_cluster_prominence_max

        glcm_cluster_shade_min = self.glcm_cluster_shade_min

        glcm_cluster_shade_max = self.glcm_cluster_shade_max

        glcm_cluster_tendency_min = self.glcm_cluster_tendency_min

        glcm_cluster_tendency_max = self.glcm_cluster_tendency_max

        glcm_contrast_min = self.glcm_contrast_min

        glcm_contrast_max = self.glcm_contrast_max

        glcm_correlation_min = self.glcm_correlation_min

        glcm_correlation_max = self.glcm_correlation_max

        glcm_difference_average_min = self.glcm_difference_average_min

        glcm_difference_average_max = self.glcm_difference_average_max

        glcm_difference_entropy_min = self.glcm_difference_entropy_min

        glcm_difference_entropy_max = self.glcm_difference_entropy_max

        glcm_difference_variance_min = self.glcm_difference_variance_min

        glcm_difference_variance_max = self.glcm_difference_variance_max

        glcm_id_min = self.glcm_id_min

        glcm_id_max = self.glcm_id_max

        glcm_idm_min = self.glcm_idm_min

        glcm_idm_max = self.glcm_idm_max

        glcm_idmn_min = self.glcm_idmn_min

        glcm_idmn_max = self.glcm_idmn_max

        glcm_idn_min = self.glcm_idn_min

        glcm_idn_max = self.glcm_idn_max

        glcm_imc_1_min = self.glcm_imc_1_min

        glcm_imc_1_max = self.glcm_imc_1_max

        glcm_imc_2_min = self.glcm_imc_2_min

        glcm_imc_2_max = self.glcm_imc_2_max

        glcm_inverse_variance_min = self.glcm_inverse_variance_min

        glcm_inverse_variance_max = self.glcm_inverse_variance_max

        glcm_joint_average_min = self.glcm_joint_average_min

        glcm_joint_average_max = self.glcm_joint_average_max

        glcm_joint_energy_min = self.glcm_joint_energy_min

        glcm_joint_energy_max = self.glcm_joint_energy_max

        glcm_joint_entropy_min = self.glcm_joint_entropy_min

        glcm_joint_entropy_max = self.glcm_joint_entropy_max

        glcm_max_probabilities_min = self.glcm_max_probabilities_min

        glcm_max_probabilities_max = self.glcm_max_probabilities_max

        glcm_sum_average_min = self.glcm_sum_average_min

        glcm_sum_average_max = self.glcm_sum_average_max

        glcm_sum_entropy_min = self.glcm_sum_entropy_min

        glcm_sum_entropy_max = self.glcm_sum_entropy_max

        glcm_sum_squares_min = self.glcm_sum_squares_min

        glcm_sum_squares_max = self.glcm_sum_squares_max

        glrlm_gray_level_non_uniformity_min = self.glrlm_gray_level_non_uniformity_min

        glrlm_gray_level_non_uniformity_max = self.glrlm_gray_level_non_uniformity_max

        glrlm_gray_level_non_uniformity_normalized_min = self.glrlm_gray_level_non_uniformity_normalized_min

        glrlm_gray_level_non_uniformity_normalized_max = self.glrlm_gray_level_non_uniformity_normalized_max

        glrlm_gray_level_variance_min = self.glrlm_gray_level_variance_min

        glrlm_gray_level_variance_max = self.glrlm_gray_level_variance_max

        glrlm_high_gray_level_run_emphasis_min = self.glrlm_high_gray_level_run_emphasis_min

        glrlm_high_gray_level_run_emphasis_max = self.glrlm_high_gray_level_run_emphasis_max

        glrlm_long_run_emphasis_min = self.glrlm_long_run_emphasis_min

        glrlm_long_run_emphasis_max = self.glrlm_long_run_emphasis_max

        glrlm_long_run_high_gray_level_emphasis_min = self.glrlm_long_run_high_gray_level_emphasis_min

        glrlm_long_run_high_gray_level_emphasis_max = self.glrlm_long_run_high_gray_level_emphasis_max

        glrlm_long_run_low_gray_level_emphasis_min = self.glrlm_long_run_low_gray_level_emphasis_min

        glrlm_long_run_low_gray_level_emphasis_max = self.glrlm_long_run_low_gray_level_emphasis_max

        glrlm_low_gray_level_run_emphasis_min = self.glrlm_low_gray_level_run_emphasis_min

        glrlm_low_gray_level_run_emphasis_max = self.glrlm_low_gray_level_run_emphasis_max

        glrlm_run_entropy_min = self.glrlm_run_entropy_min

        glrlm_run_entropy_max = self.glrlm_run_entropy_max

        glrlm_run_length_non_uniformity_min = self.glrlm_run_length_non_uniformity_min

        glrlm_run_length_non_uniformity_max = self.glrlm_run_length_non_uniformity_max

        glrlm_run_length_non_uniformity_normalized_min = self.glrlm_run_length_non_uniformity_normalized_min

        glrlm_run_length_non_uniformity_normalized_max = self.glrlm_run_length_non_uniformity_normalized_max

        glrlm_run_percentage_min = self.glrlm_run_percentage_min

        glrlm_run_percentage_max = self.glrlm_run_percentage_max

        glrlm_run_variance_min = self.glrlm_run_variance_min

        glrlm_run_variance_max = self.glrlm_run_variance_max

        glrlm_short_run_emphasis_min = self.glrlm_short_run_emphasis_min

        glrlm_short_run_emphasis_max = self.glrlm_short_run_emphasis_max

        glrlm_short_run_high_gray_level_emphasis_min = self.glrlm_short_run_high_gray_level_emphasis_min

        glrlm_short_run_high_gray_level_emphasis_max = self.glrlm_short_run_high_gray_level_emphasis_max

        glrlm_short_run_low_gray_level_emphasis_min = self.glrlm_short_run_low_gray_level_emphasis_min

        glrlm_short_run_low_gray_level_emphasis_max = self.glrlm_short_run_low_gray_level_emphasis_max

        glszm_gray_level_non_uniformity_min = self.glszm_gray_level_non_uniformity_min

        glszm_gray_level_non_uniformity_max = self.glszm_gray_level_non_uniformity_max

        glszm_gray_level_non_uniformity_normalized_min = self.glszm_gray_level_non_uniformity_normalized_min

        glszm_gray_level_non_uniformity_normalized_max = self.glszm_gray_level_non_uniformity_normalized_max

        glszm_gray_level_variance_min = self.glszm_gray_level_variance_min

        glszm_gray_level_variance_max = self.glszm_gray_level_variance_max

        glszm_high_gray_level_zone_emphasis_min = self.glszm_high_gray_level_zone_emphasis_min

        glszm_high_gray_level_zone_emphasis_max = self.glszm_high_gray_level_zone_emphasis_max

        glszm_large_area_emphasis_min = self.glszm_large_area_emphasis_min

        glszm_large_area_emphasis_max = self.glszm_large_area_emphasis_max

        glszm_large_area_high_gray_level_emphasis_min = self.glszm_large_area_high_gray_level_emphasis_min

        glszm_large_area_high_gray_level_emphasis_max = self.glszm_large_area_high_gray_level_emphasis_max

        glszm_large_area_low_gray_level_emphasis_min = self.glszm_large_area_low_gray_level_emphasis_min

        glszm_large_area_low_gray_level_emphasis_max = self.glszm_large_area_low_gray_level_emphasis_max

        glszm_low_gray_level_zone_emphasis_min = self.glszm_low_gray_level_zone_emphasis_min

        glszm_low_gray_level_zone_emphasis_max = self.glszm_low_gray_level_zone_emphasis_max

        glszm_size_zone_non_uniformity_min = self.glszm_size_zone_non_uniformity_min

        glszm_size_zone_non_uniformity_max = self.glszm_size_zone_non_uniformity_max

        glszm_size_zone_non_uniformity_normalized_min = self.glszm_size_zone_non_uniformity_normalized_min

        glszm_size_zone_non_uniformity_normalized_max = self.glszm_size_zone_non_uniformity_normalized_max

        glszm_small_area_emphasis_min = self.glszm_small_area_emphasis_min

        glszm_small_area_emphasis_max = self.glszm_small_area_emphasis_max

        glszm_small_area_high_gray_level_emphasis_min = self.glszm_small_area_high_gray_level_emphasis_min

        glszm_small_area_high_gray_level_emphasis_max = self.glszm_small_area_high_gray_level_emphasis_max

        glszm_small_area_low_gray_level_emphasis_min = self.glszm_small_area_low_gray_level_emphasis_min

        glszm_small_area_low_gray_level_emphasis_max = self.glszm_small_area_low_gray_level_emphasis_max

        glszm_zone_entropy_min = self.glszm_zone_entropy_min

        glszm_zone_entropy_max = self.glszm_zone_entropy_max

        glszm_zone_percentage_min = self.glszm_zone_percentage_min

        glszm_zone_percentage_max = self.glszm_zone_percentage_max

        glszm_zone_variance_min = self.glszm_zone_variance_min

        glszm_zone_variance_max = self.glszm_zone_variance_max

        ngtdm_busyness_min = self.ngtdm_busyness_min

        ngtdm_busyness_max = self.ngtdm_busyness_max

        ngtdm_coarseness_min = self.ngtdm_coarseness_min

        ngtdm_coarseness_max = self.ngtdm_coarseness_max

        ngtdm_complexity_min = self.ngtdm_complexity_min

        ngtdm_complexity_max = self.ngtdm_complexity_max

        ngtdm_contrast_min = self.ngtdm_contrast_min

        ngtdm_contrast_max = self.ngtdm_contrast_max

        ngtdm_strength_min = self.ngtdm_strength_min

        ngtdm_strength_max = self.ngtdm_strength_max

        gldm_dependence_entropy_min = self.gldm_dependence_entropy_min

        gldm_dependence_entropy_max = self.gldm_dependence_entropy_max

        gldm_dependence_non_uniformity_min = self.gldm_dependence_non_uniformity_min

        gldm_dependence_non_uniformity_max = self.gldm_dependence_non_uniformity_max

        gldm_dependence_non_uniformity_normalized_min = self.gldm_dependence_non_uniformity_normalized_min

        gldm_dependence_non_uniformity_normalized_max = self.gldm_dependence_non_uniformity_normalized_max

        gldm_dependence_variance_min = self.gldm_dependence_variance_min

        gldm_dependence_variance_max = self.gldm_dependence_variance_max

        gldm_gray_level_non_uniformity_min = self.gldm_gray_level_non_uniformity_min

        gldm_gray_level_non_uniformity_max = self.gldm_gray_level_non_uniformity_max

        gldm_gray_level_variance_min = self.gldm_gray_level_variance_min

        gldm_gray_level_variance_max = self.gldm_gray_level_variance_max

        gldm_high_gray_level_emphasis_min = self.gldm_high_gray_level_emphasis_min

        gldm_high_gray_level_emphasis_max = self.gldm_high_gray_level_emphasis_max

        gldm_large_dependence_emphasis_min = self.gldm_large_dependence_emphasis_min

        gldm_large_dependence_emphasis_max = self.gldm_large_dependence_emphasis_max

        gldm_large_dependence_high_gray_level_emphasis_min = self.gldm_large_dependence_high_gray_level_emphasis_min

        gldm_large_dependence_high_gray_level_emphasis_max = self.gldm_large_dependence_high_gray_level_emphasis_max

        gldm_large_dependence_low_gray_level_emphasis_min = self.gldm_large_dependence_low_gray_level_emphasis_min

        gldm_large_dependence_low_gray_level_emphasis_max = self.gldm_large_dependence_low_gray_level_emphasis_max

        gldm_low_gray_level_emphasis_min = self.gldm_low_gray_level_emphasis_min

        gldm_low_gray_level_emphasis_max = self.gldm_low_gray_level_emphasis_max

        gldm_small_dependence_emphasis_min = self.gldm_small_dependence_emphasis_min

        gldm_small_dependence_emphasis_max = self.gldm_small_dependence_emphasis_max

        gldm_small_dependence_high_gray_level_emphasis_min = self.gldm_small_dependence_high_gray_level_emphasis_min

        gldm_small_dependence_high_gray_level_emphasis_max = self.gldm_small_dependence_high_gray_level_emphasis_max

        gldm_small_dependence_low_gray_level_emphasis_min = self.gldm_small_dependence_low_gray_level_emphasis_min

        gldm_small_dependence_low_gray_level_emphasis_max = self.gldm_small_dependence_low_gray_level_emphasis_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if sex is not UNSET:
            field_dict["sex"] = sex
        if convolution_kernel is not UNSET:
            field_dict["convolutionKernel"] = convolution_kernel
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if manufacturer_model is not UNSET:
            field_dict["manufacturerModel"] = manufacturer_model
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if has_segmentation is not UNSET:
            field_dict["hasSegmentation"] = has_segmentation
        if age_years_min is not UNSET:
            field_dict["ageYearsMin"] = age_years_min
        if age_years_max is not UNSET:
            field_dict["ageYearsMax"] = age_years_max
        if study_date_min is not UNSET:
            field_dict["studyDateMin"] = study_date_min
        if study_date_max is not UNSET:
            field_dict["studyDateMax"] = study_date_max
        if kvp_min is not UNSET:
            field_dict["kvpMin"] = kvp_min
        if kvp_max is not UNSET:
            field_dict["kvpMax"] = kvp_max
        if exposure_mas_min is not UNSET:
            field_dict["exposureMasMin"] = exposure_mas_min
        if exposure_mas_max is not UNSET:
            field_dict["exposureMasMax"] = exposure_mas_max
        if slice_thickness_mm_min is not UNSET:
            field_dict["sliceThicknessMmMin"] = slice_thickness_mm_min
        if slice_thickness_mm_max is not UNSET:
            field_dict["sliceThicknessMmMax"] = slice_thickness_mm_max
        if pixel_spacing_mm_min is not UNSET:
            field_dict["pixelSpacingMmMin"] = pixel_spacing_mm_min
        if pixel_spacing_mm_max is not UNSET:
            field_dict["pixelSpacingMmMax"] = pixel_spacing_mm_max
        if rows_min is not UNSET:
            field_dict["rowsMin"] = rows_min
        if rows_max is not UNSET:
            field_dict["rowsMax"] = rows_max
        if columns_min is not UNSET:
            field_dict["columnsMin"] = columns_min
        if columns_max is not UNSET:
            field_dict["columnsMax"] = columns_max
        if n_slices_min is not UNSET:
            field_dict["nSlicesMin"] = n_slices_min
        if n_slices_max is not UNSET:
            field_dict["nSlicesMax"] = n_slices_max
        if shape_mesh_volume_min is not UNSET:
            field_dict["shapeMeshVolumeMin"] = shape_mesh_volume_min
        if shape_mesh_volume_max is not UNSET:
            field_dict["shapeMeshVolumeMax"] = shape_mesh_volume_max
        if shape_voxel_volume_min is not UNSET:
            field_dict["shapeVoxelVolumeMin"] = shape_voxel_volume_min
        if shape_voxel_volume_max is not UNSET:
            field_dict["shapeVoxelVolumeMax"] = shape_voxel_volume_max
        if shape_surface_area_min is not UNSET:
            field_dict["shapeSurfaceAreaMin"] = shape_surface_area_min
        if shape_surface_area_max is not UNSET:
            field_dict["shapeSurfaceAreaMax"] = shape_surface_area_max
        if shape_sphericity_min is not UNSET:
            field_dict["shapeSphericityMin"] = shape_sphericity_min
        if shape_sphericity_max is not UNSET:
            field_dict["shapeSphericityMax"] = shape_sphericity_max
        if shape_compactness_1_min is not UNSET:
            field_dict["shapeCompactness1Min"] = shape_compactness_1_min
        if shape_compactness_1_max is not UNSET:
            field_dict["shapeCompactness1Max"] = shape_compactness_1_max
        if shape_compactness_2_min is not UNSET:
            field_dict["shapeCompactness2Min"] = shape_compactness_2_min
        if shape_compactness_2_max is not UNSET:
            field_dict["shapeCompactness2Max"] = shape_compactness_2_max
        if shape_maximum_3_d_diameter_min is not UNSET:
            field_dict["shapeMaximum3dDiameterMin"] = shape_maximum_3_d_diameter_min
        if shape_maximum_3_d_diameter_max is not UNSET:
            field_dict["shapeMaximum3dDiameterMax"] = shape_maximum_3_d_diameter_max
        if shape_major_axis_length_min is not UNSET:
            field_dict["shapeMajorAxisLengthMin"] = shape_major_axis_length_min
        if shape_major_axis_length_max is not UNSET:
            field_dict["shapeMajorAxisLengthMax"] = shape_major_axis_length_max
        if shape_minor_axis_length_min is not UNSET:
            field_dict["shapeMinorAxisLengthMin"] = shape_minor_axis_length_min
        if shape_minor_axis_length_max is not UNSET:
            field_dict["shapeMinorAxisLengthMax"] = shape_minor_axis_length_max
        if shape_least_axis_length_min is not UNSET:
            field_dict["shapeLeastAxisLengthMin"] = shape_least_axis_length_min
        if shape_least_axis_length_max is not UNSET:
            field_dict["shapeLeastAxisLengthMax"] = shape_least_axis_length_max
        if shape_elongation_min is not UNSET:
            field_dict["shapeElongationMin"] = shape_elongation_min
        if shape_elongation_max is not UNSET:
            field_dict["shapeElongationMax"] = shape_elongation_max
        if shape_flatness_min is not UNSET:
            field_dict["shapeFlatnessMin"] = shape_flatness_min
        if shape_flatness_max is not UNSET:
            field_dict["shapeFlatnessMax"] = shape_flatness_max
        if first_energy_min is not UNSET:
            field_dict["firstEnergyMin"] = first_energy_min
        if first_energy_max is not UNSET:
            field_dict["firstEnergyMax"] = first_energy_max
        if first_total_energy_min is not UNSET:
            field_dict["firstTotalEnergyMin"] = first_total_energy_min
        if first_total_energy_max is not UNSET:
            field_dict["firstTotalEnergyMax"] = first_total_energy_max
        if first_entropy_min is not UNSET:
            field_dict["firstEntropyMin"] = first_entropy_min
        if first_entropy_max is not UNSET:
            field_dict["firstEntropyMax"] = first_entropy_max
        if first_minimum_min is not UNSET:
            field_dict["firstMinimumMin"] = first_minimum_min
        if first_minimum_max is not UNSET:
            field_dict["firstMinimumMax"] = first_minimum_max
        if first_10_th_percentile_min is not UNSET:
            field_dict["first10thPercentileMin"] = first_10_th_percentile_min
        if first_10_th_percentile_max is not UNSET:
            field_dict["first10thPercentileMax"] = first_10_th_percentile_max
        if first_90_th_percentile_min is not UNSET:
            field_dict["first90thPercentileMin"] = first_90_th_percentile_min
        if first_90_th_percentile_max is not UNSET:
            field_dict["first90thPercentileMax"] = first_90_th_percentile_max
        if first_maximum_min is not UNSET:
            field_dict["firstMaximumMin"] = first_maximum_min
        if first_maximum_max is not UNSET:
            field_dict["firstMaximumMax"] = first_maximum_max
        if first_mean_min is not UNSET:
            field_dict["firstMeanMin"] = first_mean_min
        if first_mean_max is not UNSET:
            field_dict["firstMeanMax"] = first_mean_max
        if first_median_min is not UNSET:
            field_dict["firstMedianMin"] = first_median_min
        if first_median_max is not UNSET:
            field_dict["firstMedianMax"] = first_median_max
        if first_interquartile_range_min is not UNSET:
            field_dict["firstInterquartileRangeMin"] = first_interquartile_range_min
        if first_interquartile_range_max is not UNSET:
            field_dict["firstInterquartileRangeMax"] = first_interquartile_range_max
        if first_range_min is not UNSET:
            field_dict["firstRangeMin"] = first_range_min
        if first_range_max is not UNSET:
            field_dict["firstRangeMax"] = first_range_max
        if first_mean_absolute_deviation_min is not UNSET:
            field_dict["firstMeanAbsoluteDeviationMin"] = first_mean_absolute_deviation_min
        if first_mean_absolute_deviation_max is not UNSET:
            field_dict["firstMeanAbsoluteDeviationMax"] = first_mean_absolute_deviation_max
        if first_robust_mean_absolute_deviation_min is not UNSET:
            field_dict["firstRobustMeanAbsoluteDeviationMin"] = first_robust_mean_absolute_deviation_min
        if first_robust_mean_absolute_deviation_max is not UNSET:
            field_dict["firstRobustMeanAbsoluteDeviationMax"] = first_robust_mean_absolute_deviation_max
        if first_root_mean_squared_min is not UNSET:
            field_dict["firstRootMeanSquaredMin"] = first_root_mean_squared_min
        if first_root_mean_squared_max is not UNSET:
            field_dict["firstRootMeanSquaredMax"] = first_root_mean_squared_max
        if first_skewness_min is not UNSET:
            field_dict["firstSkewnessMin"] = first_skewness_min
        if first_skewness_max is not UNSET:
            field_dict["firstSkewnessMax"] = first_skewness_max
        if first_kurtosis_min is not UNSET:
            field_dict["firstKurtosisMin"] = first_kurtosis_min
        if first_kurtosis_max is not UNSET:
            field_dict["firstKurtosisMax"] = first_kurtosis_max
        if first_variance_min is not UNSET:
            field_dict["firstVarianceMin"] = first_variance_min
        if first_variance_max is not UNSET:
            field_dict["firstVarianceMax"] = first_variance_max
        if first_uniformity_min is not UNSET:
            field_dict["firstUniformityMin"] = first_uniformity_min
        if first_uniformity_max is not UNSET:
            field_dict["firstUniformityMax"] = first_uniformity_max
        if glcm_autocorrelation_min is not UNSET:
            field_dict["glcmAutocorrelationMin"] = glcm_autocorrelation_min
        if glcm_autocorrelation_max is not UNSET:
            field_dict["glcmAutocorrelationMax"] = glcm_autocorrelation_max
        if glcm_cluster_prominence_min is not UNSET:
            field_dict["glcmClusterProminenceMin"] = glcm_cluster_prominence_min
        if glcm_cluster_prominence_max is not UNSET:
            field_dict["glcmClusterProminenceMax"] = glcm_cluster_prominence_max
        if glcm_cluster_shade_min is not UNSET:
            field_dict["glcmClusterShadeMin"] = glcm_cluster_shade_min
        if glcm_cluster_shade_max is not UNSET:
            field_dict["glcmClusterShadeMax"] = glcm_cluster_shade_max
        if glcm_cluster_tendency_min is not UNSET:
            field_dict["glcmClusterTendencyMin"] = glcm_cluster_tendency_min
        if glcm_cluster_tendency_max is not UNSET:
            field_dict["glcmClusterTendencyMax"] = glcm_cluster_tendency_max
        if glcm_contrast_min is not UNSET:
            field_dict["glcmContrastMin"] = glcm_contrast_min
        if glcm_contrast_max is not UNSET:
            field_dict["glcmContrastMax"] = glcm_contrast_max
        if glcm_correlation_min is not UNSET:
            field_dict["glcmCorrelationMin"] = glcm_correlation_min
        if glcm_correlation_max is not UNSET:
            field_dict["glcmCorrelationMax"] = glcm_correlation_max
        if glcm_difference_average_min is not UNSET:
            field_dict["glcmDifferenceAverageMin"] = glcm_difference_average_min
        if glcm_difference_average_max is not UNSET:
            field_dict["glcmDifferenceAverageMax"] = glcm_difference_average_max
        if glcm_difference_entropy_min is not UNSET:
            field_dict["glcmDifferenceEntropyMin"] = glcm_difference_entropy_min
        if glcm_difference_entropy_max is not UNSET:
            field_dict["glcmDifferenceEntropyMax"] = glcm_difference_entropy_max
        if glcm_difference_variance_min is not UNSET:
            field_dict["glcmDifferenceVarianceMin"] = glcm_difference_variance_min
        if glcm_difference_variance_max is not UNSET:
            field_dict["glcmDifferenceVarianceMax"] = glcm_difference_variance_max
        if glcm_id_min is not UNSET:
            field_dict["glcmIdMin"] = glcm_id_min
        if glcm_id_max is not UNSET:
            field_dict["glcmIdMax"] = glcm_id_max
        if glcm_idm_min is not UNSET:
            field_dict["glcmIdmMin"] = glcm_idm_min
        if glcm_idm_max is not UNSET:
            field_dict["glcmIdmMax"] = glcm_idm_max
        if glcm_idmn_min is not UNSET:
            field_dict["glcmIdmnMin"] = glcm_idmn_min
        if glcm_idmn_max is not UNSET:
            field_dict["glcmIdmnMax"] = glcm_idmn_max
        if glcm_idn_min is not UNSET:
            field_dict["glcmIdnMin"] = glcm_idn_min
        if glcm_idn_max is not UNSET:
            field_dict["glcmIdnMax"] = glcm_idn_max
        if glcm_imc_1_min is not UNSET:
            field_dict["glcmImc1Min"] = glcm_imc_1_min
        if glcm_imc_1_max is not UNSET:
            field_dict["glcmImc1Max"] = glcm_imc_1_max
        if glcm_imc_2_min is not UNSET:
            field_dict["glcmImc2Min"] = glcm_imc_2_min
        if glcm_imc_2_max is not UNSET:
            field_dict["glcmImc2Max"] = glcm_imc_2_max
        if glcm_inverse_variance_min is not UNSET:
            field_dict["glcmInverseVarianceMin"] = glcm_inverse_variance_min
        if glcm_inverse_variance_max is not UNSET:
            field_dict["glcmInverseVarianceMax"] = glcm_inverse_variance_max
        if glcm_joint_average_min is not UNSET:
            field_dict["glcmJointAverageMin"] = glcm_joint_average_min
        if glcm_joint_average_max is not UNSET:
            field_dict["glcmJointAverageMax"] = glcm_joint_average_max
        if glcm_joint_energy_min is not UNSET:
            field_dict["glcmJointEnergyMin"] = glcm_joint_energy_min
        if glcm_joint_energy_max is not UNSET:
            field_dict["glcmJointEnergyMax"] = glcm_joint_energy_max
        if glcm_joint_entropy_min is not UNSET:
            field_dict["glcmJointEntropyMin"] = glcm_joint_entropy_min
        if glcm_joint_entropy_max is not UNSET:
            field_dict["glcmJointEntropyMax"] = glcm_joint_entropy_max
        if glcm_max_probabilities_min is not UNSET:
            field_dict["glcmMaxProbabilitiesMin"] = glcm_max_probabilities_min
        if glcm_max_probabilities_max is not UNSET:
            field_dict["glcmMaxProbabilitiesMax"] = glcm_max_probabilities_max
        if glcm_sum_average_min is not UNSET:
            field_dict["glcmSumAverageMin"] = glcm_sum_average_min
        if glcm_sum_average_max is not UNSET:
            field_dict["glcmSumAverageMax"] = glcm_sum_average_max
        if glcm_sum_entropy_min is not UNSET:
            field_dict["glcmSumEntropyMin"] = glcm_sum_entropy_min
        if glcm_sum_entropy_max is not UNSET:
            field_dict["glcmSumEntropyMax"] = glcm_sum_entropy_max
        if glcm_sum_squares_min is not UNSET:
            field_dict["glcmSumSquaresMin"] = glcm_sum_squares_min
        if glcm_sum_squares_max is not UNSET:
            field_dict["glcmSumSquaresMax"] = glcm_sum_squares_max
        if glrlm_gray_level_non_uniformity_min is not UNSET:
            field_dict["glrlmGrayLevelNonUniformityMin"] = glrlm_gray_level_non_uniformity_min
        if glrlm_gray_level_non_uniformity_max is not UNSET:
            field_dict["glrlmGrayLevelNonUniformityMax"] = glrlm_gray_level_non_uniformity_max
        if glrlm_gray_level_non_uniformity_normalized_min is not UNSET:
            field_dict["glrlmGrayLevelNonUniformityNormalizedMin"] = glrlm_gray_level_non_uniformity_normalized_min
        if glrlm_gray_level_non_uniformity_normalized_max is not UNSET:
            field_dict["glrlmGrayLevelNonUniformityNormalizedMax"] = glrlm_gray_level_non_uniformity_normalized_max
        if glrlm_gray_level_variance_min is not UNSET:
            field_dict["glrlmGrayLevelVarianceMin"] = glrlm_gray_level_variance_min
        if glrlm_gray_level_variance_max is not UNSET:
            field_dict["glrlmGrayLevelVarianceMax"] = glrlm_gray_level_variance_max
        if glrlm_high_gray_level_run_emphasis_min is not UNSET:
            field_dict["glrlmHighGrayLevelRunEmphasisMin"] = glrlm_high_gray_level_run_emphasis_min
        if glrlm_high_gray_level_run_emphasis_max is not UNSET:
            field_dict["glrlmHighGrayLevelRunEmphasisMax"] = glrlm_high_gray_level_run_emphasis_max
        if glrlm_long_run_emphasis_min is not UNSET:
            field_dict["glrlmLongRunEmphasisMin"] = glrlm_long_run_emphasis_min
        if glrlm_long_run_emphasis_max is not UNSET:
            field_dict["glrlmLongRunEmphasisMax"] = glrlm_long_run_emphasis_max
        if glrlm_long_run_high_gray_level_emphasis_min is not UNSET:
            field_dict["glrlmLongRunHighGrayLevelEmphasisMin"] = glrlm_long_run_high_gray_level_emphasis_min
        if glrlm_long_run_high_gray_level_emphasis_max is not UNSET:
            field_dict["glrlmLongRunHighGrayLevelEmphasisMax"] = glrlm_long_run_high_gray_level_emphasis_max
        if glrlm_long_run_low_gray_level_emphasis_min is not UNSET:
            field_dict["glrlmLongRunLowGrayLevelEmphasisMin"] = glrlm_long_run_low_gray_level_emphasis_min
        if glrlm_long_run_low_gray_level_emphasis_max is not UNSET:
            field_dict["glrlmLongRunLowGrayLevelEmphasisMax"] = glrlm_long_run_low_gray_level_emphasis_max
        if glrlm_low_gray_level_run_emphasis_min is not UNSET:
            field_dict["glrlmLowGrayLevelRunEmphasisMin"] = glrlm_low_gray_level_run_emphasis_min
        if glrlm_low_gray_level_run_emphasis_max is not UNSET:
            field_dict["glrlmLowGrayLevelRunEmphasisMax"] = glrlm_low_gray_level_run_emphasis_max
        if glrlm_run_entropy_min is not UNSET:
            field_dict["glrlmRunEntropyMin"] = glrlm_run_entropy_min
        if glrlm_run_entropy_max is not UNSET:
            field_dict["glrlmRunEntropyMax"] = glrlm_run_entropy_max
        if glrlm_run_length_non_uniformity_min is not UNSET:
            field_dict["glrlmRunLengthNonUniformityMin"] = glrlm_run_length_non_uniformity_min
        if glrlm_run_length_non_uniformity_max is not UNSET:
            field_dict["glrlmRunLengthNonUniformityMax"] = glrlm_run_length_non_uniformity_max
        if glrlm_run_length_non_uniformity_normalized_min is not UNSET:
            field_dict["glrlmRunLengthNonUniformityNormalizedMin"] = glrlm_run_length_non_uniformity_normalized_min
        if glrlm_run_length_non_uniformity_normalized_max is not UNSET:
            field_dict["glrlmRunLengthNonUniformityNormalizedMax"] = glrlm_run_length_non_uniformity_normalized_max
        if glrlm_run_percentage_min is not UNSET:
            field_dict["glrlmRunPercentageMin"] = glrlm_run_percentage_min
        if glrlm_run_percentage_max is not UNSET:
            field_dict["glrlmRunPercentageMax"] = glrlm_run_percentage_max
        if glrlm_run_variance_min is not UNSET:
            field_dict["glrlmRunVarianceMin"] = glrlm_run_variance_min
        if glrlm_run_variance_max is not UNSET:
            field_dict["glrlmRunVarianceMax"] = glrlm_run_variance_max
        if glrlm_short_run_emphasis_min is not UNSET:
            field_dict["glrlmShortRunEmphasisMin"] = glrlm_short_run_emphasis_min
        if glrlm_short_run_emphasis_max is not UNSET:
            field_dict["glrlmShortRunEmphasisMax"] = glrlm_short_run_emphasis_max
        if glrlm_short_run_high_gray_level_emphasis_min is not UNSET:
            field_dict["glrlmShortRunHighGrayLevelEmphasisMin"] = glrlm_short_run_high_gray_level_emphasis_min
        if glrlm_short_run_high_gray_level_emphasis_max is not UNSET:
            field_dict["glrlmShortRunHighGrayLevelEmphasisMax"] = glrlm_short_run_high_gray_level_emphasis_max
        if glrlm_short_run_low_gray_level_emphasis_min is not UNSET:
            field_dict["glrlmShortRunLowGrayLevelEmphasisMin"] = glrlm_short_run_low_gray_level_emphasis_min
        if glrlm_short_run_low_gray_level_emphasis_max is not UNSET:
            field_dict["glrlmShortRunLowGrayLevelEmphasisMax"] = glrlm_short_run_low_gray_level_emphasis_max
        if glszm_gray_level_non_uniformity_min is not UNSET:
            field_dict["glszmGrayLevelNonUniformityMin"] = glszm_gray_level_non_uniformity_min
        if glszm_gray_level_non_uniformity_max is not UNSET:
            field_dict["glszmGrayLevelNonUniformityMax"] = glszm_gray_level_non_uniformity_max
        if glszm_gray_level_non_uniformity_normalized_min is not UNSET:
            field_dict["glszmGrayLevelNonUniformityNormalizedMin"] = glszm_gray_level_non_uniformity_normalized_min
        if glszm_gray_level_non_uniformity_normalized_max is not UNSET:
            field_dict["glszmGrayLevelNonUniformityNormalizedMax"] = glszm_gray_level_non_uniformity_normalized_max
        if glszm_gray_level_variance_min is not UNSET:
            field_dict["glszmGrayLevelVarianceMin"] = glszm_gray_level_variance_min
        if glszm_gray_level_variance_max is not UNSET:
            field_dict["glszmGrayLevelVarianceMax"] = glszm_gray_level_variance_max
        if glszm_high_gray_level_zone_emphasis_min is not UNSET:
            field_dict["glszmHighGrayLevelZoneEmphasisMin"] = glszm_high_gray_level_zone_emphasis_min
        if glszm_high_gray_level_zone_emphasis_max is not UNSET:
            field_dict["glszmHighGrayLevelZoneEmphasisMax"] = glszm_high_gray_level_zone_emphasis_max
        if glszm_large_area_emphasis_min is not UNSET:
            field_dict["glszmLargeAreaEmphasisMin"] = glszm_large_area_emphasis_min
        if glszm_large_area_emphasis_max is not UNSET:
            field_dict["glszmLargeAreaEmphasisMax"] = glszm_large_area_emphasis_max
        if glszm_large_area_high_gray_level_emphasis_min is not UNSET:
            field_dict["glszmLargeAreaHighGrayLevelEmphasisMin"] = glszm_large_area_high_gray_level_emphasis_min
        if glszm_large_area_high_gray_level_emphasis_max is not UNSET:
            field_dict["glszmLargeAreaHighGrayLevelEmphasisMax"] = glszm_large_area_high_gray_level_emphasis_max
        if glszm_large_area_low_gray_level_emphasis_min is not UNSET:
            field_dict["glszmLargeAreaLowGrayLevelEmphasisMin"] = glszm_large_area_low_gray_level_emphasis_min
        if glszm_large_area_low_gray_level_emphasis_max is not UNSET:
            field_dict["glszmLargeAreaLowGrayLevelEmphasisMax"] = glszm_large_area_low_gray_level_emphasis_max
        if glszm_low_gray_level_zone_emphasis_min is not UNSET:
            field_dict["glszmLowGrayLevelZoneEmphasisMin"] = glszm_low_gray_level_zone_emphasis_min
        if glszm_low_gray_level_zone_emphasis_max is not UNSET:
            field_dict["glszmLowGrayLevelZoneEmphasisMax"] = glszm_low_gray_level_zone_emphasis_max
        if glszm_size_zone_non_uniformity_min is not UNSET:
            field_dict["glszmSizeZoneNonUniformityMin"] = glszm_size_zone_non_uniformity_min
        if glszm_size_zone_non_uniformity_max is not UNSET:
            field_dict["glszmSizeZoneNonUniformityMax"] = glszm_size_zone_non_uniformity_max
        if glszm_size_zone_non_uniformity_normalized_min is not UNSET:
            field_dict["glszmSizeZoneNonUniformityNormalizedMin"] = glszm_size_zone_non_uniformity_normalized_min
        if glszm_size_zone_non_uniformity_normalized_max is not UNSET:
            field_dict["glszmSizeZoneNonUniformityNormalizedMax"] = glszm_size_zone_non_uniformity_normalized_max
        if glszm_small_area_emphasis_min is not UNSET:
            field_dict["glszmSmallAreaEmphasisMin"] = glszm_small_area_emphasis_min
        if glszm_small_area_emphasis_max is not UNSET:
            field_dict["glszmSmallAreaEmphasisMax"] = glszm_small_area_emphasis_max
        if glszm_small_area_high_gray_level_emphasis_min is not UNSET:
            field_dict["glszmSmallAreaHighGrayLevelEmphasisMin"] = glszm_small_area_high_gray_level_emphasis_min
        if glszm_small_area_high_gray_level_emphasis_max is not UNSET:
            field_dict["glszmSmallAreaHighGrayLevelEmphasisMax"] = glszm_small_area_high_gray_level_emphasis_max
        if glszm_small_area_low_gray_level_emphasis_min is not UNSET:
            field_dict["glszmSmallAreaLowGrayLevelEmphasisMin"] = glszm_small_area_low_gray_level_emphasis_min
        if glszm_small_area_low_gray_level_emphasis_max is not UNSET:
            field_dict["glszmSmallAreaLowGrayLevelEmphasisMax"] = glszm_small_area_low_gray_level_emphasis_max
        if glszm_zone_entropy_min is not UNSET:
            field_dict["glszmZoneEntropyMin"] = glszm_zone_entropy_min
        if glszm_zone_entropy_max is not UNSET:
            field_dict["glszmZoneEntropyMax"] = glszm_zone_entropy_max
        if glszm_zone_percentage_min is not UNSET:
            field_dict["glszmZonePercentageMin"] = glszm_zone_percentage_min
        if glszm_zone_percentage_max is not UNSET:
            field_dict["glszmZonePercentageMax"] = glszm_zone_percentage_max
        if glszm_zone_variance_min is not UNSET:
            field_dict["glszmZoneVarianceMin"] = glszm_zone_variance_min
        if glszm_zone_variance_max is not UNSET:
            field_dict["glszmZoneVarianceMax"] = glszm_zone_variance_max
        if ngtdm_busyness_min is not UNSET:
            field_dict["ngtdmBusynessMin"] = ngtdm_busyness_min
        if ngtdm_busyness_max is not UNSET:
            field_dict["ngtdmBusynessMax"] = ngtdm_busyness_max
        if ngtdm_coarseness_min is not UNSET:
            field_dict["ngtdmCoarsenessMin"] = ngtdm_coarseness_min
        if ngtdm_coarseness_max is not UNSET:
            field_dict["ngtdmCoarsenessMax"] = ngtdm_coarseness_max
        if ngtdm_complexity_min is not UNSET:
            field_dict["ngtdmComplexityMin"] = ngtdm_complexity_min
        if ngtdm_complexity_max is not UNSET:
            field_dict["ngtdmComplexityMax"] = ngtdm_complexity_max
        if ngtdm_contrast_min is not UNSET:
            field_dict["ngtdmContrastMin"] = ngtdm_contrast_min
        if ngtdm_contrast_max is not UNSET:
            field_dict["ngtdmContrastMax"] = ngtdm_contrast_max
        if ngtdm_strength_min is not UNSET:
            field_dict["ngtdmStrengthMin"] = ngtdm_strength_min
        if ngtdm_strength_max is not UNSET:
            field_dict["ngtdmStrengthMax"] = ngtdm_strength_max
        if gldm_dependence_entropy_min is not UNSET:
            field_dict["gldmDependenceEntropyMin"] = gldm_dependence_entropy_min
        if gldm_dependence_entropy_max is not UNSET:
            field_dict["gldmDependenceEntropyMax"] = gldm_dependence_entropy_max
        if gldm_dependence_non_uniformity_min is not UNSET:
            field_dict["gldmDependenceNonUniformityMin"] = gldm_dependence_non_uniformity_min
        if gldm_dependence_non_uniformity_max is not UNSET:
            field_dict["gldmDependenceNonUniformityMax"] = gldm_dependence_non_uniformity_max
        if gldm_dependence_non_uniformity_normalized_min is not UNSET:
            field_dict["gldmDependenceNonUniformityNormalizedMin"] = gldm_dependence_non_uniformity_normalized_min
        if gldm_dependence_non_uniformity_normalized_max is not UNSET:
            field_dict["gldmDependenceNonUniformityNormalizedMax"] = gldm_dependence_non_uniformity_normalized_max
        if gldm_dependence_variance_min is not UNSET:
            field_dict["gldmDependenceVarianceMin"] = gldm_dependence_variance_min
        if gldm_dependence_variance_max is not UNSET:
            field_dict["gldmDependenceVarianceMax"] = gldm_dependence_variance_max
        if gldm_gray_level_non_uniformity_min is not UNSET:
            field_dict["gldmGrayLevelNonUniformityMin"] = gldm_gray_level_non_uniformity_min
        if gldm_gray_level_non_uniformity_max is not UNSET:
            field_dict["gldmGrayLevelNonUniformityMax"] = gldm_gray_level_non_uniformity_max
        if gldm_gray_level_variance_min is not UNSET:
            field_dict["gldmGrayLevelVarianceMin"] = gldm_gray_level_variance_min
        if gldm_gray_level_variance_max is not UNSET:
            field_dict["gldmGrayLevelVarianceMax"] = gldm_gray_level_variance_max
        if gldm_high_gray_level_emphasis_min is not UNSET:
            field_dict["gldmHighGrayLevelEmphasisMin"] = gldm_high_gray_level_emphasis_min
        if gldm_high_gray_level_emphasis_max is not UNSET:
            field_dict["gldmHighGrayLevelEmphasisMax"] = gldm_high_gray_level_emphasis_max
        if gldm_large_dependence_emphasis_min is not UNSET:
            field_dict["gldmLargeDependenceEmphasisMin"] = gldm_large_dependence_emphasis_min
        if gldm_large_dependence_emphasis_max is not UNSET:
            field_dict["gldmLargeDependenceEmphasisMax"] = gldm_large_dependence_emphasis_max
        if gldm_large_dependence_high_gray_level_emphasis_min is not UNSET:
            field_dict["gldmLargeDependenceHighGrayLevelEmphasisMin"] = (
                gldm_large_dependence_high_gray_level_emphasis_min
            )
        if gldm_large_dependence_high_gray_level_emphasis_max is not UNSET:
            field_dict["gldmLargeDependenceHighGrayLevelEmphasisMax"] = (
                gldm_large_dependence_high_gray_level_emphasis_max
            )
        if gldm_large_dependence_low_gray_level_emphasis_min is not UNSET:
            field_dict["gldmLargeDependenceLowGrayLevelEmphasisMin"] = gldm_large_dependence_low_gray_level_emphasis_min
        if gldm_large_dependence_low_gray_level_emphasis_max is not UNSET:
            field_dict["gldmLargeDependenceLowGrayLevelEmphasisMax"] = gldm_large_dependence_low_gray_level_emphasis_max
        if gldm_low_gray_level_emphasis_min is not UNSET:
            field_dict["gldmLowGrayLevelEmphasisMin"] = gldm_low_gray_level_emphasis_min
        if gldm_low_gray_level_emphasis_max is not UNSET:
            field_dict["gldmLowGrayLevelEmphasisMax"] = gldm_low_gray_level_emphasis_max
        if gldm_small_dependence_emphasis_min is not UNSET:
            field_dict["gldmSmallDependenceEmphasisMin"] = gldm_small_dependence_emphasis_min
        if gldm_small_dependence_emphasis_max is not UNSET:
            field_dict["gldmSmallDependenceEmphasisMax"] = gldm_small_dependence_emphasis_max
        if gldm_small_dependence_high_gray_level_emphasis_min is not UNSET:
            field_dict["gldmSmallDependenceHighGrayLevelEmphasisMin"] = (
                gldm_small_dependence_high_gray_level_emphasis_min
            )
        if gldm_small_dependence_high_gray_level_emphasis_max is not UNSET:
            field_dict["gldmSmallDependenceHighGrayLevelEmphasisMax"] = (
                gldm_small_dependence_high_gray_level_emphasis_max
            )
        if gldm_small_dependence_low_gray_level_emphasis_min is not UNSET:
            field_dict["gldmSmallDependenceLowGrayLevelEmphasisMin"] = gldm_small_dependence_low_gray_level_emphasis_min
        if gldm_small_dependence_low_gray_level_emphasis_max is not UNSET:
            field_dict["gldmSmallDependenceLowGrayLevelEmphasisMax"] = gldm_small_dependence_low_gray_level_emphasis_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _dataset_id = d.pop("datasetId", UNSET)
        dataset_id: UUID | Unset
        if isinstance(_dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = UUID(_dataset_id)

        sex = d.pop("sex", UNSET)

        convolution_kernel = d.pop("convolutionKernel", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        manufacturer_model = d.pop("manufacturerModel", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        has_segmentation = d.pop("hasSegmentation", UNSET)

        age_years_min = d.pop("ageYearsMin", UNSET)

        age_years_max = d.pop("ageYearsMax", UNSET)

        _study_date_min = d.pop("studyDateMin", UNSET)
        study_date_min: datetime.date | Unset
        if isinstance(_study_date_min, Unset):
            study_date_min = UNSET
        else:
            study_date_min = isoparse(_study_date_min).date()

        _study_date_max = d.pop("studyDateMax", UNSET)
        study_date_max: datetime.date | Unset
        if isinstance(_study_date_max, Unset):
            study_date_max = UNSET
        else:
            study_date_max = isoparse(_study_date_max).date()

        kvp_min = d.pop("kvpMin", UNSET)

        kvp_max = d.pop("kvpMax", UNSET)

        exposure_mas_min = d.pop("exposureMasMin", UNSET)

        exposure_mas_max = d.pop("exposureMasMax", UNSET)

        slice_thickness_mm_min = d.pop("sliceThicknessMmMin", UNSET)

        slice_thickness_mm_max = d.pop("sliceThicknessMmMax", UNSET)

        pixel_spacing_mm_min = d.pop("pixelSpacingMmMin", UNSET)

        pixel_spacing_mm_max = d.pop("pixelSpacingMmMax", UNSET)

        rows_min = d.pop("rowsMin", UNSET)

        rows_max = d.pop("rowsMax", UNSET)

        columns_min = d.pop("columnsMin", UNSET)

        columns_max = d.pop("columnsMax", UNSET)

        n_slices_min = d.pop("nSlicesMin", UNSET)

        n_slices_max = d.pop("nSlicesMax", UNSET)

        shape_mesh_volume_min = d.pop("shapeMeshVolumeMin", UNSET)

        shape_mesh_volume_max = d.pop("shapeMeshVolumeMax", UNSET)

        shape_voxel_volume_min = d.pop("shapeVoxelVolumeMin", UNSET)

        shape_voxel_volume_max = d.pop("shapeVoxelVolumeMax", UNSET)

        shape_surface_area_min = d.pop("shapeSurfaceAreaMin", UNSET)

        shape_surface_area_max = d.pop("shapeSurfaceAreaMax", UNSET)

        shape_sphericity_min = d.pop("shapeSphericityMin", UNSET)

        shape_sphericity_max = d.pop("shapeSphericityMax", UNSET)

        shape_compactness_1_min = d.pop("shapeCompactness1Min", UNSET)

        shape_compactness_1_max = d.pop("shapeCompactness1Max", UNSET)

        shape_compactness_2_min = d.pop("shapeCompactness2Min", UNSET)

        shape_compactness_2_max = d.pop("shapeCompactness2Max", UNSET)

        shape_maximum_3_d_diameter_min = d.pop("shapeMaximum3dDiameterMin", UNSET)

        shape_maximum_3_d_diameter_max = d.pop("shapeMaximum3dDiameterMax", UNSET)

        shape_major_axis_length_min = d.pop("shapeMajorAxisLengthMin", UNSET)

        shape_major_axis_length_max = d.pop("shapeMajorAxisLengthMax", UNSET)

        shape_minor_axis_length_min = d.pop("shapeMinorAxisLengthMin", UNSET)

        shape_minor_axis_length_max = d.pop("shapeMinorAxisLengthMax", UNSET)

        shape_least_axis_length_min = d.pop("shapeLeastAxisLengthMin", UNSET)

        shape_least_axis_length_max = d.pop("shapeLeastAxisLengthMax", UNSET)

        shape_elongation_min = d.pop("shapeElongationMin", UNSET)

        shape_elongation_max = d.pop("shapeElongationMax", UNSET)

        shape_flatness_min = d.pop("shapeFlatnessMin", UNSET)

        shape_flatness_max = d.pop("shapeFlatnessMax", UNSET)

        first_energy_min = d.pop("firstEnergyMin", UNSET)

        first_energy_max = d.pop("firstEnergyMax", UNSET)

        first_total_energy_min = d.pop("firstTotalEnergyMin", UNSET)

        first_total_energy_max = d.pop("firstTotalEnergyMax", UNSET)

        first_entropy_min = d.pop("firstEntropyMin", UNSET)

        first_entropy_max = d.pop("firstEntropyMax", UNSET)

        first_minimum_min = d.pop("firstMinimumMin", UNSET)

        first_minimum_max = d.pop("firstMinimumMax", UNSET)

        first_10_th_percentile_min = d.pop("first10thPercentileMin", UNSET)

        first_10_th_percentile_max = d.pop("first10thPercentileMax", UNSET)

        first_90_th_percentile_min = d.pop("first90thPercentileMin", UNSET)

        first_90_th_percentile_max = d.pop("first90thPercentileMax", UNSET)

        first_maximum_min = d.pop("firstMaximumMin", UNSET)

        first_maximum_max = d.pop("firstMaximumMax", UNSET)

        first_mean_min = d.pop("firstMeanMin", UNSET)

        first_mean_max = d.pop("firstMeanMax", UNSET)

        first_median_min = d.pop("firstMedianMin", UNSET)

        first_median_max = d.pop("firstMedianMax", UNSET)

        first_interquartile_range_min = d.pop("firstInterquartileRangeMin", UNSET)

        first_interquartile_range_max = d.pop("firstInterquartileRangeMax", UNSET)

        first_range_min = d.pop("firstRangeMin", UNSET)

        first_range_max = d.pop("firstRangeMax", UNSET)

        first_mean_absolute_deviation_min = d.pop("firstMeanAbsoluteDeviationMin", UNSET)

        first_mean_absolute_deviation_max = d.pop("firstMeanAbsoluteDeviationMax", UNSET)

        first_robust_mean_absolute_deviation_min = d.pop("firstRobustMeanAbsoluteDeviationMin", UNSET)

        first_robust_mean_absolute_deviation_max = d.pop("firstRobustMeanAbsoluteDeviationMax", UNSET)

        first_root_mean_squared_min = d.pop("firstRootMeanSquaredMin", UNSET)

        first_root_mean_squared_max = d.pop("firstRootMeanSquaredMax", UNSET)

        first_skewness_min = d.pop("firstSkewnessMin", UNSET)

        first_skewness_max = d.pop("firstSkewnessMax", UNSET)

        first_kurtosis_min = d.pop("firstKurtosisMin", UNSET)

        first_kurtosis_max = d.pop("firstKurtosisMax", UNSET)

        first_variance_min = d.pop("firstVarianceMin", UNSET)

        first_variance_max = d.pop("firstVarianceMax", UNSET)

        first_uniformity_min = d.pop("firstUniformityMin", UNSET)

        first_uniformity_max = d.pop("firstUniformityMax", UNSET)

        glcm_autocorrelation_min = d.pop("glcmAutocorrelationMin", UNSET)

        glcm_autocorrelation_max = d.pop("glcmAutocorrelationMax", UNSET)

        glcm_cluster_prominence_min = d.pop("glcmClusterProminenceMin", UNSET)

        glcm_cluster_prominence_max = d.pop("glcmClusterProminenceMax", UNSET)

        glcm_cluster_shade_min = d.pop("glcmClusterShadeMin", UNSET)

        glcm_cluster_shade_max = d.pop("glcmClusterShadeMax", UNSET)

        glcm_cluster_tendency_min = d.pop("glcmClusterTendencyMin", UNSET)

        glcm_cluster_tendency_max = d.pop("glcmClusterTendencyMax", UNSET)

        glcm_contrast_min = d.pop("glcmContrastMin", UNSET)

        glcm_contrast_max = d.pop("glcmContrastMax", UNSET)

        glcm_correlation_min = d.pop("glcmCorrelationMin", UNSET)

        glcm_correlation_max = d.pop("glcmCorrelationMax", UNSET)

        glcm_difference_average_min = d.pop("glcmDifferenceAverageMin", UNSET)

        glcm_difference_average_max = d.pop("glcmDifferenceAverageMax", UNSET)

        glcm_difference_entropy_min = d.pop("glcmDifferenceEntropyMin", UNSET)

        glcm_difference_entropy_max = d.pop("glcmDifferenceEntropyMax", UNSET)

        glcm_difference_variance_min = d.pop("glcmDifferenceVarianceMin", UNSET)

        glcm_difference_variance_max = d.pop("glcmDifferenceVarianceMax", UNSET)

        glcm_id_min = d.pop("glcmIdMin", UNSET)

        glcm_id_max = d.pop("glcmIdMax", UNSET)

        glcm_idm_min = d.pop("glcmIdmMin", UNSET)

        glcm_idm_max = d.pop("glcmIdmMax", UNSET)

        glcm_idmn_min = d.pop("glcmIdmnMin", UNSET)

        glcm_idmn_max = d.pop("glcmIdmnMax", UNSET)

        glcm_idn_min = d.pop("glcmIdnMin", UNSET)

        glcm_idn_max = d.pop("glcmIdnMax", UNSET)

        glcm_imc_1_min = d.pop("glcmImc1Min", UNSET)

        glcm_imc_1_max = d.pop("glcmImc1Max", UNSET)

        glcm_imc_2_min = d.pop("glcmImc2Min", UNSET)

        glcm_imc_2_max = d.pop("glcmImc2Max", UNSET)

        glcm_inverse_variance_min = d.pop("glcmInverseVarianceMin", UNSET)

        glcm_inverse_variance_max = d.pop("glcmInverseVarianceMax", UNSET)

        glcm_joint_average_min = d.pop("glcmJointAverageMin", UNSET)

        glcm_joint_average_max = d.pop("glcmJointAverageMax", UNSET)

        glcm_joint_energy_min = d.pop("glcmJointEnergyMin", UNSET)

        glcm_joint_energy_max = d.pop("glcmJointEnergyMax", UNSET)

        glcm_joint_entropy_min = d.pop("glcmJointEntropyMin", UNSET)

        glcm_joint_entropy_max = d.pop("glcmJointEntropyMax", UNSET)

        glcm_max_probabilities_min = d.pop("glcmMaxProbabilitiesMin", UNSET)

        glcm_max_probabilities_max = d.pop("glcmMaxProbabilitiesMax", UNSET)

        glcm_sum_average_min = d.pop("glcmSumAverageMin", UNSET)

        glcm_sum_average_max = d.pop("glcmSumAverageMax", UNSET)

        glcm_sum_entropy_min = d.pop("glcmSumEntropyMin", UNSET)

        glcm_sum_entropy_max = d.pop("glcmSumEntropyMax", UNSET)

        glcm_sum_squares_min = d.pop("glcmSumSquaresMin", UNSET)

        glcm_sum_squares_max = d.pop("glcmSumSquaresMax", UNSET)

        glrlm_gray_level_non_uniformity_min = d.pop("glrlmGrayLevelNonUniformityMin", UNSET)

        glrlm_gray_level_non_uniformity_max = d.pop("glrlmGrayLevelNonUniformityMax", UNSET)

        glrlm_gray_level_non_uniformity_normalized_min = d.pop("glrlmGrayLevelNonUniformityNormalizedMin", UNSET)

        glrlm_gray_level_non_uniformity_normalized_max = d.pop("glrlmGrayLevelNonUniformityNormalizedMax", UNSET)

        glrlm_gray_level_variance_min = d.pop("glrlmGrayLevelVarianceMin", UNSET)

        glrlm_gray_level_variance_max = d.pop("glrlmGrayLevelVarianceMax", UNSET)

        glrlm_high_gray_level_run_emphasis_min = d.pop("glrlmHighGrayLevelRunEmphasisMin", UNSET)

        glrlm_high_gray_level_run_emphasis_max = d.pop("glrlmHighGrayLevelRunEmphasisMax", UNSET)

        glrlm_long_run_emphasis_min = d.pop("glrlmLongRunEmphasisMin", UNSET)

        glrlm_long_run_emphasis_max = d.pop("glrlmLongRunEmphasisMax", UNSET)

        glrlm_long_run_high_gray_level_emphasis_min = d.pop("glrlmLongRunHighGrayLevelEmphasisMin", UNSET)

        glrlm_long_run_high_gray_level_emphasis_max = d.pop("glrlmLongRunHighGrayLevelEmphasisMax", UNSET)

        glrlm_long_run_low_gray_level_emphasis_min = d.pop("glrlmLongRunLowGrayLevelEmphasisMin", UNSET)

        glrlm_long_run_low_gray_level_emphasis_max = d.pop("glrlmLongRunLowGrayLevelEmphasisMax", UNSET)

        glrlm_low_gray_level_run_emphasis_min = d.pop("glrlmLowGrayLevelRunEmphasisMin", UNSET)

        glrlm_low_gray_level_run_emphasis_max = d.pop("glrlmLowGrayLevelRunEmphasisMax", UNSET)

        glrlm_run_entropy_min = d.pop("glrlmRunEntropyMin", UNSET)

        glrlm_run_entropy_max = d.pop("glrlmRunEntropyMax", UNSET)

        glrlm_run_length_non_uniformity_min = d.pop("glrlmRunLengthNonUniformityMin", UNSET)

        glrlm_run_length_non_uniformity_max = d.pop("glrlmRunLengthNonUniformityMax", UNSET)

        glrlm_run_length_non_uniformity_normalized_min = d.pop("glrlmRunLengthNonUniformityNormalizedMin", UNSET)

        glrlm_run_length_non_uniformity_normalized_max = d.pop("glrlmRunLengthNonUniformityNormalizedMax", UNSET)

        glrlm_run_percentage_min = d.pop("glrlmRunPercentageMin", UNSET)

        glrlm_run_percentage_max = d.pop("glrlmRunPercentageMax", UNSET)

        glrlm_run_variance_min = d.pop("glrlmRunVarianceMin", UNSET)

        glrlm_run_variance_max = d.pop("glrlmRunVarianceMax", UNSET)

        glrlm_short_run_emphasis_min = d.pop("glrlmShortRunEmphasisMin", UNSET)

        glrlm_short_run_emphasis_max = d.pop("glrlmShortRunEmphasisMax", UNSET)

        glrlm_short_run_high_gray_level_emphasis_min = d.pop("glrlmShortRunHighGrayLevelEmphasisMin", UNSET)

        glrlm_short_run_high_gray_level_emphasis_max = d.pop("glrlmShortRunHighGrayLevelEmphasisMax", UNSET)

        glrlm_short_run_low_gray_level_emphasis_min = d.pop("glrlmShortRunLowGrayLevelEmphasisMin", UNSET)

        glrlm_short_run_low_gray_level_emphasis_max = d.pop("glrlmShortRunLowGrayLevelEmphasisMax", UNSET)

        glszm_gray_level_non_uniformity_min = d.pop("glszmGrayLevelNonUniformityMin", UNSET)

        glszm_gray_level_non_uniformity_max = d.pop("glszmGrayLevelNonUniformityMax", UNSET)

        glszm_gray_level_non_uniformity_normalized_min = d.pop("glszmGrayLevelNonUniformityNormalizedMin", UNSET)

        glszm_gray_level_non_uniformity_normalized_max = d.pop("glszmGrayLevelNonUniformityNormalizedMax", UNSET)

        glszm_gray_level_variance_min = d.pop("glszmGrayLevelVarianceMin", UNSET)

        glszm_gray_level_variance_max = d.pop("glszmGrayLevelVarianceMax", UNSET)

        glszm_high_gray_level_zone_emphasis_min = d.pop("glszmHighGrayLevelZoneEmphasisMin", UNSET)

        glszm_high_gray_level_zone_emphasis_max = d.pop("glszmHighGrayLevelZoneEmphasisMax", UNSET)

        glszm_large_area_emphasis_min = d.pop("glszmLargeAreaEmphasisMin", UNSET)

        glszm_large_area_emphasis_max = d.pop("glszmLargeAreaEmphasisMax", UNSET)

        glszm_large_area_high_gray_level_emphasis_min = d.pop("glszmLargeAreaHighGrayLevelEmphasisMin", UNSET)

        glszm_large_area_high_gray_level_emphasis_max = d.pop("glszmLargeAreaHighGrayLevelEmphasisMax", UNSET)

        glszm_large_area_low_gray_level_emphasis_min = d.pop("glszmLargeAreaLowGrayLevelEmphasisMin", UNSET)

        glszm_large_area_low_gray_level_emphasis_max = d.pop("glszmLargeAreaLowGrayLevelEmphasisMax", UNSET)

        glszm_low_gray_level_zone_emphasis_min = d.pop("glszmLowGrayLevelZoneEmphasisMin", UNSET)

        glszm_low_gray_level_zone_emphasis_max = d.pop("glszmLowGrayLevelZoneEmphasisMax", UNSET)

        glszm_size_zone_non_uniformity_min = d.pop("glszmSizeZoneNonUniformityMin", UNSET)

        glszm_size_zone_non_uniformity_max = d.pop("glszmSizeZoneNonUniformityMax", UNSET)

        glszm_size_zone_non_uniformity_normalized_min = d.pop("glszmSizeZoneNonUniformityNormalizedMin", UNSET)

        glszm_size_zone_non_uniformity_normalized_max = d.pop("glszmSizeZoneNonUniformityNormalizedMax", UNSET)

        glszm_small_area_emphasis_min = d.pop("glszmSmallAreaEmphasisMin", UNSET)

        glszm_small_area_emphasis_max = d.pop("glszmSmallAreaEmphasisMax", UNSET)

        glszm_small_area_high_gray_level_emphasis_min = d.pop("glszmSmallAreaHighGrayLevelEmphasisMin", UNSET)

        glszm_small_area_high_gray_level_emphasis_max = d.pop("glszmSmallAreaHighGrayLevelEmphasisMax", UNSET)

        glszm_small_area_low_gray_level_emphasis_min = d.pop("glszmSmallAreaLowGrayLevelEmphasisMin", UNSET)

        glszm_small_area_low_gray_level_emphasis_max = d.pop("glszmSmallAreaLowGrayLevelEmphasisMax", UNSET)

        glszm_zone_entropy_min = d.pop("glszmZoneEntropyMin", UNSET)

        glszm_zone_entropy_max = d.pop("glszmZoneEntropyMax", UNSET)

        glszm_zone_percentage_min = d.pop("glszmZonePercentageMin", UNSET)

        glszm_zone_percentage_max = d.pop("glszmZonePercentageMax", UNSET)

        glszm_zone_variance_min = d.pop("glszmZoneVarianceMin", UNSET)

        glszm_zone_variance_max = d.pop("glszmZoneVarianceMax", UNSET)

        ngtdm_busyness_min = d.pop("ngtdmBusynessMin", UNSET)

        ngtdm_busyness_max = d.pop("ngtdmBusynessMax", UNSET)

        ngtdm_coarseness_min = d.pop("ngtdmCoarsenessMin", UNSET)

        ngtdm_coarseness_max = d.pop("ngtdmCoarsenessMax", UNSET)

        ngtdm_complexity_min = d.pop("ngtdmComplexityMin", UNSET)

        ngtdm_complexity_max = d.pop("ngtdmComplexityMax", UNSET)

        ngtdm_contrast_min = d.pop("ngtdmContrastMin", UNSET)

        ngtdm_contrast_max = d.pop("ngtdmContrastMax", UNSET)

        ngtdm_strength_min = d.pop("ngtdmStrengthMin", UNSET)

        ngtdm_strength_max = d.pop("ngtdmStrengthMax", UNSET)

        gldm_dependence_entropy_min = d.pop("gldmDependenceEntropyMin", UNSET)

        gldm_dependence_entropy_max = d.pop("gldmDependenceEntropyMax", UNSET)

        gldm_dependence_non_uniformity_min = d.pop("gldmDependenceNonUniformityMin", UNSET)

        gldm_dependence_non_uniformity_max = d.pop("gldmDependenceNonUniformityMax", UNSET)

        gldm_dependence_non_uniformity_normalized_min = d.pop("gldmDependenceNonUniformityNormalizedMin", UNSET)

        gldm_dependence_non_uniformity_normalized_max = d.pop("gldmDependenceNonUniformityNormalizedMax", UNSET)

        gldm_dependence_variance_min = d.pop("gldmDependenceVarianceMin", UNSET)

        gldm_dependence_variance_max = d.pop("gldmDependenceVarianceMax", UNSET)

        gldm_gray_level_non_uniformity_min = d.pop("gldmGrayLevelNonUniformityMin", UNSET)

        gldm_gray_level_non_uniformity_max = d.pop("gldmGrayLevelNonUniformityMax", UNSET)

        gldm_gray_level_variance_min = d.pop("gldmGrayLevelVarianceMin", UNSET)

        gldm_gray_level_variance_max = d.pop("gldmGrayLevelVarianceMax", UNSET)

        gldm_high_gray_level_emphasis_min = d.pop("gldmHighGrayLevelEmphasisMin", UNSET)

        gldm_high_gray_level_emphasis_max = d.pop("gldmHighGrayLevelEmphasisMax", UNSET)

        gldm_large_dependence_emphasis_min = d.pop("gldmLargeDependenceEmphasisMin", UNSET)

        gldm_large_dependence_emphasis_max = d.pop("gldmLargeDependenceEmphasisMax", UNSET)

        gldm_large_dependence_high_gray_level_emphasis_min = d.pop("gldmLargeDependenceHighGrayLevelEmphasisMin", UNSET)

        gldm_large_dependence_high_gray_level_emphasis_max = d.pop("gldmLargeDependenceHighGrayLevelEmphasisMax", UNSET)

        gldm_large_dependence_low_gray_level_emphasis_min = d.pop("gldmLargeDependenceLowGrayLevelEmphasisMin", UNSET)

        gldm_large_dependence_low_gray_level_emphasis_max = d.pop("gldmLargeDependenceLowGrayLevelEmphasisMax", UNSET)

        gldm_low_gray_level_emphasis_min = d.pop("gldmLowGrayLevelEmphasisMin", UNSET)

        gldm_low_gray_level_emphasis_max = d.pop("gldmLowGrayLevelEmphasisMax", UNSET)

        gldm_small_dependence_emphasis_min = d.pop("gldmSmallDependenceEmphasisMin", UNSET)

        gldm_small_dependence_emphasis_max = d.pop("gldmSmallDependenceEmphasisMax", UNSET)

        gldm_small_dependence_high_gray_level_emphasis_min = d.pop("gldmSmallDependenceHighGrayLevelEmphasisMin", UNSET)

        gldm_small_dependence_high_gray_level_emphasis_max = d.pop("gldmSmallDependenceHighGrayLevelEmphasisMax", UNSET)

        gldm_small_dependence_low_gray_level_emphasis_min = d.pop("gldmSmallDependenceLowGrayLevelEmphasisMin", UNSET)

        gldm_small_dependence_low_gray_level_emphasis_max = d.pop("gldmSmallDependenceLowGrayLevelEmphasisMax", UNSET)

        image_filter = cls(
            dataset_id=dataset_id,
            sex=sex,
            convolution_kernel=convolution_kernel,
            manufacturer=manufacturer,
            manufacturer_model=manufacturer_model,
            software_version=software_version,
            has_segmentation=has_segmentation,
            age_years_min=age_years_min,
            age_years_max=age_years_max,
            study_date_min=study_date_min,
            study_date_max=study_date_max,
            kvp_min=kvp_min,
            kvp_max=kvp_max,
            exposure_mas_min=exposure_mas_min,
            exposure_mas_max=exposure_mas_max,
            slice_thickness_mm_min=slice_thickness_mm_min,
            slice_thickness_mm_max=slice_thickness_mm_max,
            pixel_spacing_mm_min=pixel_spacing_mm_min,
            pixel_spacing_mm_max=pixel_spacing_mm_max,
            rows_min=rows_min,
            rows_max=rows_max,
            columns_min=columns_min,
            columns_max=columns_max,
            n_slices_min=n_slices_min,
            n_slices_max=n_slices_max,
            shape_mesh_volume_min=shape_mesh_volume_min,
            shape_mesh_volume_max=shape_mesh_volume_max,
            shape_voxel_volume_min=shape_voxel_volume_min,
            shape_voxel_volume_max=shape_voxel_volume_max,
            shape_surface_area_min=shape_surface_area_min,
            shape_surface_area_max=shape_surface_area_max,
            shape_sphericity_min=shape_sphericity_min,
            shape_sphericity_max=shape_sphericity_max,
            shape_compactness_1_min=shape_compactness_1_min,
            shape_compactness_1_max=shape_compactness_1_max,
            shape_compactness_2_min=shape_compactness_2_min,
            shape_compactness_2_max=shape_compactness_2_max,
            shape_maximum_3_d_diameter_min=shape_maximum_3_d_diameter_min,
            shape_maximum_3_d_diameter_max=shape_maximum_3_d_diameter_max,
            shape_major_axis_length_min=shape_major_axis_length_min,
            shape_major_axis_length_max=shape_major_axis_length_max,
            shape_minor_axis_length_min=shape_minor_axis_length_min,
            shape_minor_axis_length_max=shape_minor_axis_length_max,
            shape_least_axis_length_min=shape_least_axis_length_min,
            shape_least_axis_length_max=shape_least_axis_length_max,
            shape_elongation_min=shape_elongation_min,
            shape_elongation_max=shape_elongation_max,
            shape_flatness_min=shape_flatness_min,
            shape_flatness_max=shape_flatness_max,
            first_energy_min=first_energy_min,
            first_energy_max=first_energy_max,
            first_total_energy_min=first_total_energy_min,
            first_total_energy_max=first_total_energy_max,
            first_entropy_min=first_entropy_min,
            first_entropy_max=first_entropy_max,
            first_minimum_min=first_minimum_min,
            first_minimum_max=first_minimum_max,
            first_10_th_percentile_min=first_10_th_percentile_min,
            first_10_th_percentile_max=first_10_th_percentile_max,
            first_90_th_percentile_min=first_90_th_percentile_min,
            first_90_th_percentile_max=first_90_th_percentile_max,
            first_maximum_min=first_maximum_min,
            first_maximum_max=first_maximum_max,
            first_mean_min=first_mean_min,
            first_mean_max=first_mean_max,
            first_median_min=first_median_min,
            first_median_max=first_median_max,
            first_interquartile_range_min=first_interquartile_range_min,
            first_interquartile_range_max=first_interquartile_range_max,
            first_range_min=first_range_min,
            first_range_max=first_range_max,
            first_mean_absolute_deviation_min=first_mean_absolute_deviation_min,
            first_mean_absolute_deviation_max=first_mean_absolute_deviation_max,
            first_robust_mean_absolute_deviation_min=first_robust_mean_absolute_deviation_min,
            first_robust_mean_absolute_deviation_max=first_robust_mean_absolute_deviation_max,
            first_root_mean_squared_min=first_root_mean_squared_min,
            first_root_mean_squared_max=first_root_mean_squared_max,
            first_skewness_min=first_skewness_min,
            first_skewness_max=first_skewness_max,
            first_kurtosis_min=first_kurtosis_min,
            first_kurtosis_max=first_kurtosis_max,
            first_variance_min=first_variance_min,
            first_variance_max=first_variance_max,
            first_uniformity_min=first_uniformity_min,
            first_uniformity_max=first_uniformity_max,
            glcm_autocorrelation_min=glcm_autocorrelation_min,
            glcm_autocorrelation_max=glcm_autocorrelation_max,
            glcm_cluster_prominence_min=glcm_cluster_prominence_min,
            glcm_cluster_prominence_max=glcm_cluster_prominence_max,
            glcm_cluster_shade_min=glcm_cluster_shade_min,
            glcm_cluster_shade_max=glcm_cluster_shade_max,
            glcm_cluster_tendency_min=glcm_cluster_tendency_min,
            glcm_cluster_tendency_max=glcm_cluster_tendency_max,
            glcm_contrast_min=glcm_contrast_min,
            glcm_contrast_max=glcm_contrast_max,
            glcm_correlation_min=glcm_correlation_min,
            glcm_correlation_max=glcm_correlation_max,
            glcm_difference_average_min=glcm_difference_average_min,
            glcm_difference_average_max=glcm_difference_average_max,
            glcm_difference_entropy_min=glcm_difference_entropy_min,
            glcm_difference_entropy_max=glcm_difference_entropy_max,
            glcm_difference_variance_min=glcm_difference_variance_min,
            glcm_difference_variance_max=glcm_difference_variance_max,
            glcm_id_min=glcm_id_min,
            glcm_id_max=glcm_id_max,
            glcm_idm_min=glcm_idm_min,
            glcm_idm_max=glcm_idm_max,
            glcm_idmn_min=glcm_idmn_min,
            glcm_idmn_max=glcm_idmn_max,
            glcm_idn_min=glcm_idn_min,
            glcm_idn_max=glcm_idn_max,
            glcm_imc_1_min=glcm_imc_1_min,
            glcm_imc_1_max=glcm_imc_1_max,
            glcm_imc_2_min=glcm_imc_2_min,
            glcm_imc_2_max=glcm_imc_2_max,
            glcm_inverse_variance_min=glcm_inverse_variance_min,
            glcm_inverse_variance_max=glcm_inverse_variance_max,
            glcm_joint_average_min=glcm_joint_average_min,
            glcm_joint_average_max=glcm_joint_average_max,
            glcm_joint_energy_min=glcm_joint_energy_min,
            glcm_joint_energy_max=glcm_joint_energy_max,
            glcm_joint_entropy_min=glcm_joint_entropy_min,
            glcm_joint_entropy_max=glcm_joint_entropy_max,
            glcm_max_probabilities_min=glcm_max_probabilities_min,
            glcm_max_probabilities_max=glcm_max_probabilities_max,
            glcm_sum_average_min=glcm_sum_average_min,
            glcm_sum_average_max=glcm_sum_average_max,
            glcm_sum_entropy_min=glcm_sum_entropy_min,
            glcm_sum_entropy_max=glcm_sum_entropy_max,
            glcm_sum_squares_min=glcm_sum_squares_min,
            glcm_sum_squares_max=glcm_sum_squares_max,
            glrlm_gray_level_non_uniformity_min=glrlm_gray_level_non_uniformity_min,
            glrlm_gray_level_non_uniformity_max=glrlm_gray_level_non_uniformity_max,
            glrlm_gray_level_non_uniformity_normalized_min=glrlm_gray_level_non_uniformity_normalized_min,
            glrlm_gray_level_non_uniformity_normalized_max=glrlm_gray_level_non_uniformity_normalized_max,
            glrlm_gray_level_variance_min=glrlm_gray_level_variance_min,
            glrlm_gray_level_variance_max=glrlm_gray_level_variance_max,
            glrlm_high_gray_level_run_emphasis_min=glrlm_high_gray_level_run_emphasis_min,
            glrlm_high_gray_level_run_emphasis_max=glrlm_high_gray_level_run_emphasis_max,
            glrlm_long_run_emphasis_min=glrlm_long_run_emphasis_min,
            glrlm_long_run_emphasis_max=glrlm_long_run_emphasis_max,
            glrlm_long_run_high_gray_level_emphasis_min=glrlm_long_run_high_gray_level_emphasis_min,
            glrlm_long_run_high_gray_level_emphasis_max=glrlm_long_run_high_gray_level_emphasis_max,
            glrlm_long_run_low_gray_level_emphasis_min=glrlm_long_run_low_gray_level_emphasis_min,
            glrlm_long_run_low_gray_level_emphasis_max=glrlm_long_run_low_gray_level_emphasis_max,
            glrlm_low_gray_level_run_emphasis_min=glrlm_low_gray_level_run_emphasis_min,
            glrlm_low_gray_level_run_emphasis_max=glrlm_low_gray_level_run_emphasis_max,
            glrlm_run_entropy_min=glrlm_run_entropy_min,
            glrlm_run_entropy_max=glrlm_run_entropy_max,
            glrlm_run_length_non_uniformity_min=glrlm_run_length_non_uniformity_min,
            glrlm_run_length_non_uniformity_max=glrlm_run_length_non_uniformity_max,
            glrlm_run_length_non_uniformity_normalized_min=glrlm_run_length_non_uniformity_normalized_min,
            glrlm_run_length_non_uniformity_normalized_max=glrlm_run_length_non_uniformity_normalized_max,
            glrlm_run_percentage_min=glrlm_run_percentage_min,
            glrlm_run_percentage_max=glrlm_run_percentage_max,
            glrlm_run_variance_min=glrlm_run_variance_min,
            glrlm_run_variance_max=glrlm_run_variance_max,
            glrlm_short_run_emphasis_min=glrlm_short_run_emphasis_min,
            glrlm_short_run_emphasis_max=glrlm_short_run_emphasis_max,
            glrlm_short_run_high_gray_level_emphasis_min=glrlm_short_run_high_gray_level_emphasis_min,
            glrlm_short_run_high_gray_level_emphasis_max=glrlm_short_run_high_gray_level_emphasis_max,
            glrlm_short_run_low_gray_level_emphasis_min=glrlm_short_run_low_gray_level_emphasis_min,
            glrlm_short_run_low_gray_level_emphasis_max=glrlm_short_run_low_gray_level_emphasis_max,
            glszm_gray_level_non_uniformity_min=glszm_gray_level_non_uniformity_min,
            glszm_gray_level_non_uniformity_max=glszm_gray_level_non_uniformity_max,
            glszm_gray_level_non_uniformity_normalized_min=glszm_gray_level_non_uniformity_normalized_min,
            glszm_gray_level_non_uniformity_normalized_max=glszm_gray_level_non_uniformity_normalized_max,
            glszm_gray_level_variance_min=glszm_gray_level_variance_min,
            glszm_gray_level_variance_max=glszm_gray_level_variance_max,
            glszm_high_gray_level_zone_emphasis_min=glszm_high_gray_level_zone_emphasis_min,
            glszm_high_gray_level_zone_emphasis_max=glszm_high_gray_level_zone_emphasis_max,
            glszm_large_area_emphasis_min=glszm_large_area_emphasis_min,
            glszm_large_area_emphasis_max=glszm_large_area_emphasis_max,
            glszm_large_area_high_gray_level_emphasis_min=glszm_large_area_high_gray_level_emphasis_min,
            glszm_large_area_high_gray_level_emphasis_max=glszm_large_area_high_gray_level_emphasis_max,
            glszm_large_area_low_gray_level_emphasis_min=glszm_large_area_low_gray_level_emphasis_min,
            glszm_large_area_low_gray_level_emphasis_max=glszm_large_area_low_gray_level_emphasis_max,
            glszm_low_gray_level_zone_emphasis_min=glszm_low_gray_level_zone_emphasis_min,
            glszm_low_gray_level_zone_emphasis_max=glszm_low_gray_level_zone_emphasis_max,
            glszm_size_zone_non_uniformity_min=glszm_size_zone_non_uniformity_min,
            glszm_size_zone_non_uniformity_max=glszm_size_zone_non_uniformity_max,
            glszm_size_zone_non_uniformity_normalized_min=glszm_size_zone_non_uniformity_normalized_min,
            glszm_size_zone_non_uniformity_normalized_max=glszm_size_zone_non_uniformity_normalized_max,
            glszm_small_area_emphasis_min=glszm_small_area_emphasis_min,
            glszm_small_area_emphasis_max=glszm_small_area_emphasis_max,
            glszm_small_area_high_gray_level_emphasis_min=glszm_small_area_high_gray_level_emphasis_min,
            glszm_small_area_high_gray_level_emphasis_max=glszm_small_area_high_gray_level_emphasis_max,
            glszm_small_area_low_gray_level_emphasis_min=glszm_small_area_low_gray_level_emphasis_min,
            glszm_small_area_low_gray_level_emphasis_max=glszm_small_area_low_gray_level_emphasis_max,
            glszm_zone_entropy_min=glszm_zone_entropy_min,
            glszm_zone_entropy_max=glszm_zone_entropy_max,
            glszm_zone_percentage_min=glszm_zone_percentage_min,
            glszm_zone_percentage_max=glszm_zone_percentage_max,
            glszm_zone_variance_min=glszm_zone_variance_min,
            glszm_zone_variance_max=glszm_zone_variance_max,
            ngtdm_busyness_min=ngtdm_busyness_min,
            ngtdm_busyness_max=ngtdm_busyness_max,
            ngtdm_coarseness_min=ngtdm_coarseness_min,
            ngtdm_coarseness_max=ngtdm_coarseness_max,
            ngtdm_complexity_min=ngtdm_complexity_min,
            ngtdm_complexity_max=ngtdm_complexity_max,
            ngtdm_contrast_min=ngtdm_contrast_min,
            ngtdm_contrast_max=ngtdm_contrast_max,
            ngtdm_strength_min=ngtdm_strength_min,
            ngtdm_strength_max=ngtdm_strength_max,
            gldm_dependence_entropy_min=gldm_dependence_entropy_min,
            gldm_dependence_entropy_max=gldm_dependence_entropy_max,
            gldm_dependence_non_uniformity_min=gldm_dependence_non_uniformity_min,
            gldm_dependence_non_uniformity_max=gldm_dependence_non_uniformity_max,
            gldm_dependence_non_uniformity_normalized_min=gldm_dependence_non_uniformity_normalized_min,
            gldm_dependence_non_uniformity_normalized_max=gldm_dependence_non_uniformity_normalized_max,
            gldm_dependence_variance_min=gldm_dependence_variance_min,
            gldm_dependence_variance_max=gldm_dependence_variance_max,
            gldm_gray_level_non_uniformity_min=gldm_gray_level_non_uniformity_min,
            gldm_gray_level_non_uniformity_max=gldm_gray_level_non_uniformity_max,
            gldm_gray_level_variance_min=gldm_gray_level_variance_min,
            gldm_gray_level_variance_max=gldm_gray_level_variance_max,
            gldm_high_gray_level_emphasis_min=gldm_high_gray_level_emphasis_min,
            gldm_high_gray_level_emphasis_max=gldm_high_gray_level_emphasis_max,
            gldm_large_dependence_emphasis_min=gldm_large_dependence_emphasis_min,
            gldm_large_dependence_emphasis_max=gldm_large_dependence_emphasis_max,
            gldm_large_dependence_high_gray_level_emphasis_min=gldm_large_dependence_high_gray_level_emphasis_min,
            gldm_large_dependence_high_gray_level_emphasis_max=gldm_large_dependence_high_gray_level_emphasis_max,
            gldm_large_dependence_low_gray_level_emphasis_min=gldm_large_dependence_low_gray_level_emphasis_min,
            gldm_large_dependence_low_gray_level_emphasis_max=gldm_large_dependence_low_gray_level_emphasis_max,
            gldm_low_gray_level_emphasis_min=gldm_low_gray_level_emphasis_min,
            gldm_low_gray_level_emphasis_max=gldm_low_gray_level_emphasis_max,
            gldm_small_dependence_emphasis_min=gldm_small_dependence_emphasis_min,
            gldm_small_dependence_emphasis_max=gldm_small_dependence_emphasis_max,
            gldm_small_dependence_high_gray_level_emphasis_min=gldm_small_dependence_high_gray_level_emphasis_min,
            gldm_small_dependence_high_gray_level_emphasis_max=gldm_small_dependence_high_gray_level_emphasis_max,
            gldm_small_dependence_low_gray_level_emphasis_min=gldm_small_dependence_low_gray_level_emphasis_min,
            gldm_small_dependence_low_gray_level_emphasis_max=gldm_small_dependence_low_gray_level_emphasis_max,
        )

        image_filter.additional_properties = d
        return image_filter

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
