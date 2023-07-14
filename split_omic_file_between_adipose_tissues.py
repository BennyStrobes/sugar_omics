import numpy as np 
import os
import sys
import pdb






#####################
# Command line args
#####################
input_omics_file = sys.argv[1]
sample_file = sys.argv[2]
output_omics_file = sys.argv[3]


# First, extract sample names
sample_names = np.loadtxt(sample_file,dtype=str,delimiter='\t')[1:,0]
# Convert sample names to dictionary
sample_names_dicti = {}
for sample_name in sample_names:
	if sample_name in sample_names_dicti:
		print('assumption eroror')
		pdb.set_trace()
	sample_names_dicti[sample_name] = 1



f = open(input_omics_file)
t = open(output_omics_file,'w')
head_count = 0
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	row_header = data[0]
	row_info = np.asarray(data[1:])
	if head_count == 0:
		head_count = head_count + 1
		row_indices = []
		for ii, row_ele in enumerate(row_info):
			if row_ele in sample_names_dicti:
				row_indices.append(ii)
		row_indices = np.asarray(row_indices)
		# Error check
		if np.array_equal(row_info[row_indices],sample_names) == False:
			print('assumption eroror')
			pdb.set_trace()
		t.write(row_header + '\t' + '\t'.join(row_info[row_indices]) + '\n')
		continue
	tmp = row_info[row_indices].astype(float)
	if np.var(tmp) == 0.0:
		print('skipping gene cause it has 0 variance')
		continue
	t.write(row_header + '\t' + '\t'.join(row_info[row_indices]) + '\n')
f.close()
t.close()