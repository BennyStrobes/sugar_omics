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
# Open output file handle
t = open(output_file,'w')
t.write(header + '\t' + 'FDR\n')

num_genes = len(assoc_res)
# Sort assoc_res list
assoc_res.sort(key=lambda x: x[0])

# BH correction
kk = 1
for gene_tuple in assoc_res:
	bf_pvalue = gene_tuple[0]
	fdr = num_genes*bf_pvalue/kk 
	kk = kk + 1
	line = gene_tuple[1]
	# Print to output file
	t.write(line + '\t' + str(fdr) + '\n')
t.close()








