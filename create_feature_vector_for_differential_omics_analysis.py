import numpy as np 
import os
import sys
import pdb


def extract_fructose_glucose_feature_vector(sample_structure_file):
	fv = []
	f = open(sample_structure_file)
	head_count = 0
	for line in f:
		line = line.rstrip()
		data = line.split('\t')
		# Skip header
		if head_count == 0:
			head_count = head_count + 1
			continue
		if data[4] == 'Glucose':
			fv.append(1.0)
		else:
			# error check
			if data[4] != 'Fructose':
				print('assumption eroror')
				pdb.set_trace()
			fv.append(0.0)
	f.close()
	return np.asarray(fv)

def extract_ffa_feature_vector(sample_structure_file):
	fv = []
	f = open(sample_structure_file)
	head_count = 0
	for line in f:
		line = line.rstrip()
		data = line.split('\t')
		# Skip header
		if head_count == 0:
			head_count = head_count + 1
			continue
		fv.append(float(data[5]))
	f.close()
	return np.asarray(fv)

def extract_steonosis_non_steonosis_feature_vector(sample_structure_file):
	fv = []
	f = open(sample_structure_file)
	head_count = 0
	for line in f:
		line = line.rstrip()
		data = line.split('\t')
		# Skip header
		if head_count == 0:
			head_count = head_count + 1
			continue
		if data[3] == 'Steatosis':
			fv.append(1.0)
		else:
			# error check
			if data[3] != 'No Steatosis':
				print('assumption eroror')
				pdb.set_trace()
			fv.append(0.0)
	f.close()
	return np.asarray(fv)


def extract_category_comparison_feature_vector(sample_structure_file, cat1, cat2):
	fv = []
	f = open(sample_structure_file)
	head_count = 0
	for line in f:
		line = line.rstrip()
		data = line.split('\t')
		# Skip header
		if head_count == 0:
			head_count = head_count + 1
			continue
		if data[2] == cat1:
			fv.append(1.0)
		elif data[2] == cat2:
			fv.append(0.0)
		else:
			fv.append(np.nan)
	f.close()
	return np.asarray(fv)




####################
# Command line args
####################
test_version = sys.argv[1]
sample_structure_file = sys.argv[2]
feature_vector_file = sys.argv[3]

# Extract feature vector
if test_version == 'fructose_glucose':
	feature_vector = extract_fructose_glucose_feature_vector(sample_structure_file)
elif test_version == 'steotosis_non_steotosis':
	feature_vector = extract_steonosis_non_steonosis_feature_vector(sample_structure_file)
elif test_version == '1_2':
	feature_vector = extract_category_comparison_feature_vector(sample_structure_file, '1', '2')
elif test_version == '3_4':
	feature_vector = extract_category_comparison_feature_vector(sample_structure_file, '3', '4')
elif test_version == '1_3':
	feature_vector = extract_category_comparison_feature_vector(sample_structure_file, '1', '3')
elif test_version == '2_4':
	feature_vector = extract_category_comparison_feature_vector(sample_structure_file, '2', '4')
elif test_version == 'FFA':
	feature_vector = extract_ffa_feature_vector(sample_structure_file)
else:
	print('test version ' + test_version + ' not currently implemented error')
	pdb.set_trace()


# Save feature vector to output file
np.savetxt(feature_vector_file, feature_vector, fmt="%s", delimiter='\n')
