import numpy as np 
import os
import sys
import pdb



#############
# input data
#############
input_file = sys.argv[1]
output_file = sys.argv[2]
processed_sample_structure_file = sys.argv[3]


# First, extract sample names
sample_names = np.loadtxt(processed_sample_structure_file,dtype=str,delimiter='\t')[1:,0]

f = open(input_file)
t = open(output_file,'w')
used_genes = {}
head_count = 0
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	# Quick error checking 
	#if len(data) != 53:
		#print('assumpiton eroor')
		#pdb.set_trace()
	# Deal with header seperately
	if head_count == 0:
		head_count = head_count + 1

		first_16_samples = data[26:(26+16)]
		second_16_samples = np.asarray(data[44:(44+16)])
		data_samples = np.hstack((first_16_samples, second_16_samples))
		# Error checking
		for ii, data_sample in enumerate(data_samples):
			sample_name = sample_names[ii]
			if data_sample.split('Phos')[0] + 'scaled' != sample_name:
				print('assumption eroro')
				pdb.set_trace()

		t.write('phosphosite_id\t' + '\t'.join(sample_names) + '\n')
		head_count = head_count + 1
		continue
	# Deal with rest of lines
	gene_name = data[0] + ':' + data[1] + ':' + data[2]
	first_16_samples = data[26:(26+16)]
	second_16_samples = np.asarray(data[44:(44+16)])

	# QUick error check
	if gene_name in used_genes:
		print('repeat')
		pdb.set_trace()
	used_genes[gene_name] =1

	expr = np.hstack((first_16_samples, second_16_samples))

	# More error checking
	tmp = expr.astype(float)
	if np.sum(np.isnan(tmp)) != 0.0:
		print('skipped phosphosite because it had nans')
		continue
	if np.var(tmp) == 0.0 or np.isnan(np.var(tmp)):
		print('skippeed because 0 variance across samples')
		continue
	t.write(gene_name + '\t' + '\t'.join(expr) + '\n')
f.close()
t.close()

