import numpy as np 
import os
import sys
import pdb
import statsmodels.api as sm

def run_association_test(feature_vector, omics_values):
	# Fix nan values
	if np.sum(np.isnan(feature_vector)):
		valid_indices = np.isnan(feature_vector) == False
		feature_vector = feature_vector[valid_indices]
		omics_values = omics_values[valid_indices]

	# Run regression analysis
	X = sm.add_constant(feature_vector)
	est = sm.OLS(omics_values, X).fit()

	# Extract summary statistics
	beta = est.params[1]
	beta_se = est.bse[1]
	pvalue = est.pvalues[1]

	return beta, beta_se, pvalue


##########################
# Command line arguements
##########################
feature_vector_file = sys.argv[1]
omic_data_file = sys.argv[2]
output_file = sys.argv[3]

# Load in feature vector
feature_vector = np.loadtxt(feature_vector_file)


# Open output file handle and print header
t = open(output_file,'w')
t.write('test_id\tbeta\tbeta_standard_error\tpvalue\n')

# Loop through omic data file
f = open(omic_data_file)
head_count = 0
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	# skip header
	if head_count == 0:
		head_count = head_count + 1
		continue
	# Run analysis for a specfic test
	test_name = data[0]
	omics_values = np.asarray(data[1:]).astype(float)

	# Quick error check
	if len(omics_values) != len(feature_vector):
		print('assumption eroror')
		pdb.set_trace()


	# Run association test
	beta, beta_se, pvalue = run_association_test(feature_vector, omics_values)

	# Print results to output file
	t.write(test_name + '\t' + str(beta) + '\t' + str(beta_se) + '\t' + str(pvalue) + '\n')


# Close file handles
f.close()
t.close()



