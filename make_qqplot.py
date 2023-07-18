import numpy as np 
import os
import sys
import pdb
import pandas as pd
import seaborn as sns







# Command line args
association_results_file = sys.argv[1]
visualization_output_root = sys.argv[2]



# Load in association results
association_results = np.loadtxt(association_results_file,dtype=str,delimiter='\t', comments='***')
# Get pvalues
pvalues = association_results[1:,3].astype(float)
# Sort pvalues
sorted_pvalues = np.sort(pvalues)

# Get null pvalues
null_pvalues = np.random.uniform(size=len(pvalues))
# Sorted
sorted_null_pvalues = np.sort(null_pvalues)



# Creat pandas df qq plot data
qq_plot_data = {'-log10pvalue': -np.log10(sorted_pvalues), '-log10nullpvalue': -np.log10(sorted_null_pvalues)}
qq_plot_df = pd.DataFrame(data=qq_plot_data)

# Fir diagonal
maxy = np.max(np.hstack((-np.log10(sorted_pvalues),-np.log10(sorted_null_pvalues) )))


scatter = sns.scatterplot(data=qq_plot_df, x="-log10nullpvalue", y="-log10pvalue", linewidth=0)
scatter.plot([0,np.max(maxy)], [0,np.max(maxy)], color='black')
fig = scatter.get_figure()
fig.savefig(visualization_output_root + '_qq_plot.pdf') 
