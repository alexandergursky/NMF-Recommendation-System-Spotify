
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.preprocessing import MaxAbsScaler, Normalizer
from sklearn.pipeline import make_pipeline
from joblib import Parallel, delayed
import datetime

start_time = datetime.datetime.now()

master_df = pd.read_csv('spotify-sparse5.csv')

# Extracting a list of artist names, I will need this later on after sparse has gone through the pipeline.
artist_list = master_df['artistname'].values.tolist()

# Reindexed
data_reindex_df = master_df.set_index('artistname')

# Model
scaler = MaxAbsScaler()
nmf = NMF(n_components=60, random_state=1, max_iter=200, alpha_W=10, alpha_H=100) # GENERALIZED UNDERSTANDING OF ALPHAS, NOT ACTUAL: alpha_W does columns, alpha_H does observations.
norm = Normalizer()
pipeline = make_pipeline(scaler, nmf, norm)

# n_components substute to get all the features: data_reindex_df.shape[1]

# Therefore, a higher alpha_W value will result in fewer artists 
# being associated with each user (i.e., each user is less likely to listen to many artists), 
# while a higher alpha_H value will result in each artist 
# being associated with fewer users (i.e., each artist is less likely to be listened to by many users).

# In the context of an artist recommendation system, setting a super low alpha_W and a super high alpha_H would put 
# a stronger emphasis on the artists with more plays in the data, rather than trying to capture more subtle relationships between artists. 
# This may result in recommendations that are more biased towards the most popular artists in the dataset, 
# rather than providing more diverse and potentially personalized recommendations.
# On the other hand, setting a super high alpha_W and a super low alpha_H would put a stronger emphasis on capturing 
# the subtle relationships between artists, which may result in more diverse and potentially personalized recommendations. 
# However, it may also make the model more sensitive to noise in the data, and may result in recommendations that are less 
# representative of the overall listening patterns in the dataset.


# alpha_W=1 increased the accuracy of recomended artist alot. 
# alpha_W=10 made "Glass Animals" have 4 artist at 100%, this is bad.
# alpha_H=10 did not really do anything diffrent when i had that at 10 and alpha_W at 1.
# alpha_W=100, alpha_H=1 fixed the "Glass Animals" issue. It looks a bit better.
# alpha_W=100, alpha_H=100 made the recomended artist % go down which is good. They are all super high currently like each one is 0.99997 and stuff.
# alpha_W=1000, alpha_H=1000 made "Gucci Mane" have e-15 results, very bad. I noticed that the higher alpha_W made  the recomended artist go down in accuracy by .0001 this is good.  
# alpha_W=10000, alpha_H=10000 made every artist produce the same recomendations.
# sparse5: n_components=1264, random_state=1, max_iter=200, alpha_W=10, alpha_H=100 was not bad, even though genres are supposed to be 2069

# Define a function to compute NMF on a subset of the data
def compute_nmf(start, end):
    subset_df = data_reindex_df.iloc[start:end]
    return pipeline.fit_transform(subset_df)

# Split the data into chunks
num_chunks = 8 # change this to the number of nodes you want to use, local is same as jobs. lets try that.
chunk_size = len(data_reindex_df) // num_chunks
chunks = [(i*chunk_size, (i+1)*chunk_size) for i in range(num_chunks)]
if chunks[-1][1] < len(data_reindex_df):
    chunks[-1] = (chunks[-1][0], len(data_reindex_df))

# Compute NMF on each chunk in parallel
# n_jobs= CPU's threadded
results = Parallel(n_jobs=8)(
    delayed(compute_nmf)(start, end) for start, end in chunks)

# Concatenate the results into a single array
scal_nmf_norm = np.concatenate(results, axis=0)

# Conversion to a df and appending the artist list as the index so I can queue the results
scal_nmf_norm_df = pd.DataFrame(scal_nmf_norm, index=artist_list)

# This is for exporting the model
scal_nmf_norm_df.to_csv('sparse5.1-trained.csv')


end_time = datetime.datetime.now()

elapsed_time = end_time - start_time

print("Elapsed time: {} seconds ({} minutes, {} hours)".format(elapsed_time.seconds, elapsed_time.seconds // 60, elapsed_time.seconds // 3600))


# use the spotify-genres.py file to get the number of genres, use this as the components number. then play with the alphas.