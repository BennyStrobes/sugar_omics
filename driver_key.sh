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
sh process_input_data.sh $sample_structure_input_file $protein_input_file $phosphosite_input_file $processed_input_data_dir
