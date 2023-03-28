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
