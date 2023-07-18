import numpy as np 
import os
import sys
import pdb







#######################
# Command line args
#######################
input_file = sys.argv[1]
output_file = sys.argv[2]

# Load in input data
assoc_res = []
head_count = 0
f = open(input_file)
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	if head_count == 0:
		head_count = head_count + 1
		header = line
		continue
	pvalue = float(data[3])
	assoc_res.append((pvalue, line))
f.close()

# Run Benjamin Hochberg FDR correction


num_genes = len(assoc_res)
# Sort assoc_res list
assoc_res.sort(key=lambda x: x[0])

# BH correction
kk = 1
fdrs = []
for gene_tuple in assoc_res:
	bf_pvalue = gene_tuple[0]
	fdr = num_genes*bf_pvalue/kk 
	kk = kk + 1
	line = gene_tuple[1]
	# Print to output file
	fdrs.append(fdr)
fdrs = np.asarray(fdrs)

prev_min_value = 100000000000000000000000.0  # Infinite
for position in np.flip(np.arange(len(fdrs))):
	curr_value = fdrs[position]
	if prev_min_value < curr_value:
		fdrs[position] = prev_min_value
	else:
		prev_min_value = curr_value




# Open output file handle
t = open(output_file,'w')
t.write(header + '\t' + 'FDR\n')
for itera, gene_tuple in enumerate(assoc_res):
	line = gene_tuple[1]
	fdr = fdrs[itera]

	t.write(line + '\t' + str(fdr) + '\n')
t.close()








