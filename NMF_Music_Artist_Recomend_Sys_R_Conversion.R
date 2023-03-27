
setwd("place your directory path here if needed")

# Load required library
install.packages("tidyverse")
library(tidyverse)


# Import the CSV file
my_data <- read.csv("sparse5-trained.csv")

# Set selecting_artist to "Jack Johnson" in title case
selecting_artist <- "Jack Johnson" %>% str_to_title()

# Select the row corresponding to the selecting_artist from the my_data
artist <- my_data[my_data$X == selecting_artist, -1]

# Getting only the numeric data on the dataframe
data_num <- my_data[, -1]

# Conversion to matrix
artist_matrix <- as.matrix(artist)
data_num_matrix <- as.matrix(data_num)
data_num_matrix <- unname(data_num_matrix)

artist_matrix_t <- t(artist_matrix)

# Multiply the two matrices
recommendation_matrix <- data_num_matrix %*% artist_matrix_t

# Convert recommendation_matrix to a data frame
recommendation_df <- data.frame(recommendation_matrix)

# Append names to recommendation_df
names <- my_data[,1]
new_data <- data.frame(artist_names = names)
recommendation_df <- cbind(new_data, recommendation_df)

# Select the top 11 recommendations
top_recommendations <- recommendation_df %>%
  arrange(desc(.[,2])) %>%
  head(11)

# Print the top 11 recommendations with names
print(top_recommendations)

