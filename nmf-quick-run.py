
import pandas as pd


# This cell is for importing the already trained model
scal_nmf_norm_df = pd.read_csv('sparse10-trained.csv', index_col='Unnamed: 0')

loop_break = str('nmf-quick-run').lower()

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

while True:
    print('In order to exit the program, type in: nmf-quick-run')
    try:
        # Get user input and convert to lowercase
        selecting_artist = input('Enter Artist: ').lower()

        if selecting_artist == loop_break:
            break

        # Selecting the observation (ignoring case)
        artist = scal_nmf_norm_df.loc[scal_nmf_norm_df.index.str.lower() == selecting_artist.lower()]

        # Check if artist was found
        if artist.empty:
            print('No artist found.')
            continue

        # Scaler-product the observation to the df to get the similarity scores
        recommendation = scal_nmf_norm_df.dot(artist.iloc[0])

        # Display the results
        print(recommendation.nlargest(11))

    except:
        pass
