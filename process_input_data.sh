

sample_structure_input_file="$1"
protein_input_file="$2"
phosphosite_input_file="$3"
results_dir="$4"



#############
# Clean and process sample structure file
processed_sample_structure_file=${results_dir}"sample_structure.txt"
python3 clean_and_process_sample_structure_file.py $sample_structure_input_file $processed_sample_structure_file



#############
# Clean and process protein input file
processed_protein_file=${results_dir}"protein_log2.txt"
python3 clean_and_process_protein_data.py $protein_input_file $processed_protein_file $processed_sample_structure_file



#############
# Clean and process phosphosite input file
processed_phosphosite_file=${results_dir}"phosphosite_log2.txt"
python3 clean_and_process_phosphosite_data.py $phosphosite_input_file $processed_phosphosite_file $processed_sample_structure_file
