import numpy as np 
import os
import sys
import pdb




#####################
# Command line args
#####################
processed_sample_structure_file = sys.argv[1]  # Input file
output_file_sq = sys.argv[2]  # Ouptut file SQ
output_file_om = sys.argv[3]  # Ouput file OM


f = open(processed_sample_structure_file)
t_sq = open(output_file_sq,'w')
t_om = open(output_file_om,'w')

head_count = 0
aa = []
bb = []
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	if head_count == 0:
		head_count = head_count + 1
		t_sq.write(line + '\n')
		t_om.write(line + '\n')
		continue
	if data[0].split('_scal')[0].endswith('SQ'): # SQ
		t_sq.write(line + '\n')
		aa.append(data[0].split('_SQ')[0])
	else:
		t_om.write(line + '\n')
		bb.append(data[0].split('_OM')[0])
f.close()
t_sq.close()
t_om.close()

# Errror checking
aa = np.asarray(aa)
bb = np.asarray(bb)
if np.array_equal(aa,bb) == False:
	print('assumption eororor')
	pdb.set_trace()
