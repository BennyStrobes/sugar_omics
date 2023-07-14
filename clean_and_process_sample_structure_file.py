import numpy as np 
import os
import sys
import pdb







###################
# Command line args
####################
input_file = sys.argv[1]
output_file = sys.argv[2]

# stream input file and do some processing
f = open(input_file)
info = []
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	# Error checking
	if len(data) != 33:
		print('assumption eroror')
	# Quick fixes
	if data[0] == 'Sample ID':
		data[0] = 'Sample_id'
	if data[0] == 'Adipose Depot':
		data[0] = 'Tissue'
	if data[0] == 'Group #':
		data[0] = 'Group'
	if data[0] == 'Steatosis':
		data[0] = 'Steatosis_indicator'
	if data[0] == 'FFA Suppression':
		data[0] = 'FFA_supression'
	# Save to array
	info.append(data)
f.close()

# make 2d array and transpose
output_mat = np.transpose(np.asarray(info))

# Save to file
np.savetxt(output_file, output_mat, fmt="%s", delimiter='\t')