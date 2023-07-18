
test_version="$1"
sample_structure_file="$2"
omic_data_file="$3"
analysis_output_root="$4"


# Create feature vector for this test
feature_vector_file=$analysis_output_root"_feature_vector.txt"
python3 create_feature_vector_for_differential_omics_analysis.py $test_version $sample_structure_file $feature_vector_file

# Run omics analysis with feature vector
differential_omics_output_file=${analysis_output_root}"_association_results.txt"
python3 run_differential_omics_analysis.py $feature_vector_file $omic_data_file $differential_omics_output_file



# Add fdr correction
differential_omics_plus_fdr_output_file=${analysis_output_root}"_association_and_fdr_results.txt"
python3 run_fdr_correction.py $differential_omics_output_file $differential_omics_plus_fdr_output_file



# Make qq-plot
visualization_output_root=${analysis_output_root}"_visualization"
python3 make_qqplot.py $differential_omics_plus_fdr_output_file $visualization_output_root


rm $feature_vector_file

