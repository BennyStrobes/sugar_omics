###############
# Ben Strober
###############

# Analysis of sugar related protein and phosphosite treatmeant responses for Jordan



############################
# Working directory
############################
working_directory="/Users/bes710/Dropbox/Research/sugar_omics_data/"


#############################
# Input data
#############################
# root
input_data_dir=${working_directory}"input_data/"

# Sample structure file shared by Jordan on 7/13/23
# Originally called 'Ben SODA Data.xlsx', and saved as tsv
sample_structure_input_file=${input_data_dir}"sample_data.txt"

# log transformed protein data originally shared by Jordan on 7/12/23
# Originally table "Proteins-Log2 w annotation" in 'SODA_Proteomics_Analysis.xlsx', and saved as tsv
protein_input_file=${input_data_dir}"protein_log2.txt"

# log transformed phosphosite data originally shared by Jordan on 7/12/23
# Originally table "Phos-Log2 w annotation" in 'SODA_Proteomics_Analysis.xlsx', and saved as tsv
phosphosite_input_file=${input_data_dir}"phosphosites_log2.txt"



#############################
# Output directories
#############################
# Clean input data and save to processed input data
processed_input_data_dir=${working_directory}"processed_data/"

# Results of analysis
results_dir=${working_directory}"results/"



#############################
# Analysis
#############################

############################
# Clean and process input data
if false; then
sh process_input_data.sh $sample_structure_input_file $protein_input_file $phosphosite_input_file $processed_input_data_dir
fi




############################
# Run differential expression analysis

# Parameters to iterate over
tissue_versions=( "sq" "om")
omics_versions=("protein" "phosphosite")
test_versions=("fructose_glucose" "steotosis_non_steotosis" "1_2" "3_4" "1_3" "2_4" "FFA")


for tissue_version in "${tissue_versions[@]}"; do
for omic_version in "${omics_versions[@]}"; do
for test_version in "${test_versions[@]}"; do

	# Input data
	sample_structure_file=${processed_input_data_dir}"sample_structure_"${tissue_version}".txt"
	omic_data_file=${processed_input_data_dir}${omic_version}"_log2_"${tissue_version}".txt"
	# Analysis output root
	analysis_output_root=${results_dir}${test_version}"_test_"${tissue_version}"_tissue_"${omic_version}"_omics"

	sh run_differential_omics_analysis.sh ${test_version} ${sample_structure_file} ${omic_data_file} ${analysis_output_root}

done
done
done


