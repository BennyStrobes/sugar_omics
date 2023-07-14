

sample_structure_input_file="$1"
protein_input_file="$2"
phosphosite_input_file="$3"
results_dir="$4"



#########################################
# Clean and process sample structure file
#########################################
processed_sample_structure_file=${results_dir}"sample_structure.txt"
python3 clean_and_process_sample_structure_file.py $sample_structure_input_file $processed_sample_structure_file

# Split sample structure file between adipose tissue
processed_sq_sample_structure_file=${results_dir}"sample_structure_sq.txt"
processed_om_sample_structure_file=${results_dir}"sample_structure_om.txt"
python3 split_sample_structure_file_between_adipose_tissues.py $processed_sample_structure_file $processed_sq_sample_structure_file $processed_om_sample_structure_file



#########################################
# Clean and process protein input file
#########################################
processed_protein_file=${results_dir}"protein_log2.txt"
python3 clean_and_process_protein_data.py $protein_input_file $processed_protein_file $processed_sample_structure_file

# Split file into sq and om
processed_protein_sq_file=${results_dir}"protein_log2_sq.txt"
python3 split_omic_file_between_adipose_tissues.py $processed_protein_file $processed_sq_sample_structure_file $processed_protein_sq_file
processed_protein_om_file=${results_dir}"protein_log2_om.txt"
python3 split_omic_file_between_adipose_tissues.py $processed_protein_file $processed_om_sample_structure_file $processed_protein_om_file




#########################################
# Clean and process phosphosite input file
#########################################
processed_phosphosite_file=${results_dir}"phosphosite_log2.txt"
python3 clean_and_process_phosphosite_data.py $phosphosite_input_file $processed_phosphosite_file $processed_sample_structure_file

# Split file into sq and om
processed_phosphosite_sq_file=${results_dir}"phosphosite_log2_sq.txt"
python3 split_omic_file_between_adipose_tissues.py $processed_phosphosite_file $processed_sq_sample_structure_file $processed_phosphosite_sq_file
processed_phosphosite_om_file=${results_dir}"phosphosite_log2_om.txt"
python3 split_omic_file_between_adipose_tissues.py $processed_phosphosite_file $processed_om_sample_structure_file $processed_phosphosite_om_file



