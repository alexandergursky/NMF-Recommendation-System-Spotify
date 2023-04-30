# NMF_Recommendation_System
## How Spotify Uses Decomposition Algorithms for Song Recommendations
NMF is a dimensional reduction method and effective for document/feature clustering, because a term-document matrix is high-dimensional and sparse. 
The initial matrix of the NMF algorithm is regarded as a clustering result. The trained model contains 7703 artists and 1121 users. Training the model took 40 minutes on 8 CPU cores clocking an average of 4.20GHz. Spotify and Apple Music both use the concept of collaborative filtering to recommend you artist and songs that are based on users with a similar listening history as you. Other companies use these recomendation systems as well, such as Amazon, Walmart, and really any business partaking in e-commerce. Recomendation systems are what is used under the hood of your customer/user experiance when you are checking out on Amazon and you see the pop-up of more products with the caption "Other users who purchased X also purchased Y, would you like to add Y to your cart?". This project uses the algorithm Non-Negative Matrix Factorization (NMF).
<br><br>
![Screenshot](nmf-function.PNG)
<br><br>
### Libraries Utilized
- Scikit-learn: pip3 install scikit-learn
- Pandas: pip3 install pandas
- Numpy: pip3 install pandas
- Multiprocessing: pip3 install multiprocessing

### How To Use
I have included the trained model for demonstration purposes, if you would like the raw data in order to follow along 
with my cleaning and wrangling process, please reach out to me and I would be glad to distribute that. The data comes from Spotify's API, my raw data contains over 2.3 billion observations by 4 features, so naturally it is a huge file that can not be uploaded to GitHub (file is a 1.2Gb CSV file). 
<br><br>
("nmf-quick-run.py" is the recommended method)  
To use it, open one of the 3 files listed below: <br>
- "Spotify_NMF_Final.ipynb"
- "NMF_Music_Artist_Recomend_Sys_R_Conversion.R"
- "nmf-quick-run.py" <br>
<br>
Then run the cell, line, or script which loads the model. Lastly select the artist of your choosing.
Please reach out for any further inquiries. 

### Examples
![Screenshot](example1.PNG)
![Screenshot](example2.PNG)
![Screenshot](example3.PNG)
![Screenshot](example4.PNG)
![Screenshot](example5.PNG)
---
## IMPORTANT UPDATES (4/29/2023)
- Trained a more advanced iter (sparse10) on a super computer cluster
- Sparse10 now preserves all users for better results during decomposition
- Fixed time complexity issue, reason: setting components to features was incorrect. I needed to set the components to a "cluster" amount of sorts, similar to k-means. Before I was setting the components to the count of users, algorithm was not decomposing properly as a result of this.
- Included more files to the repository (files that are current and support the updated fixes, main cleaning file is now "artist-cleaning.ipynb", main HPC cluster files are "talon-nmf-sparse91.py" and "nmf-run-sparse911.sh", NMF testing is now "jupyter-metric-testing.ipynb", and misc.).
- Fixed awful compressing size of the data and recomendation system, solution: clean the data more efficiently, and properly allocate the "n_components=" arg. You will notice that the files uploaded are no longer the sizes that I claim in the briefing which is great.
  
The new iter was trained on **Georgia Southern Universities** HPC super computer cluster using 32-cores with 4G of RAM allocated to each core, timing around 6-8mins to train the model. The most up-to-date version of the recommendation system is to run "sparse10-trained.csv".
