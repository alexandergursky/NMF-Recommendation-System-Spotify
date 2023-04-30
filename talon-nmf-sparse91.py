
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.preprocessing import MaxAbsScaler, Normalizer
from sklearn.pipeline import make_pipeline
from joblib import Parallel, delayed
import datetime

start_time = datetime.datetime.now()

master_df = pd.read_csv('spotify-sparse9.csv')

# Extracting a list of artist names, I will need this later on after sparse has gone through the pipeline.
artist_list = master_df['artistname'].values.tolist()

# Reindexed
data_reindex_df = master_df.set_index('artistname')

# Model
scaler = MaxAbsScaler()

nmf = NMF(
    n_components= 800,
    random_state= 1,
    max_iter= 1000,
    alpha_W= 0,     # Row level
    alpha_H= 10,    # Component/column level
    l1_ratio= 0.5
)

norm = Normalizer()

pipeline = make_pipeline(scaler, nmf, norm)

# Define a function to compute NMF on a subset of the data
def compute_nmf(start, end):
    subset_df = data_reindex_df.iloc[start:end]
    return pipeline.fit_transform(subset_df)

# Split the data into chunks
num_chunks = 32 # change this to the number of nodes you want to use, local is same as jobs. lets try that.
chunk_size = len(data_reindex_df) // num_chunks
chunks = [(i*chunk_size, (i+1)*chunk_size) for i in range(num_chunks)]
if chunks[-1][1] < len(data_reindex_df):
    chunks[-1] = (chunks[-1][0], len(data_reindex_df))

# Compute NMF on each chunk in parallel
# n_jobs= CPU's threadded
results = Parallel(n_jobs=32)(
    delayed(compute_nmf)(start, end) for start, end in chunks)

# Concatenate the results into a single array
scal_nmf_norm = np.concatenate(results, axis=0)

# Conversion to a df and appending the artist list as the index so I can queue the results
scal_nmf_norm_df = pd.DataFrame(scal_nmf_norm, index=artist_list)

# This is for exporting the model
scal_nmf_norm_df.to_csv('sparse9.1-trained.csv')


end_time = datetime.datetime.now()

elapsed_time = end_time - start_time

print("Elapsed time: {} seconds ({} minutes, {} hours)".format(elapsed_time.seconds, elapsed_time.seconds // 60, elapsed_time.seconds // 3600))