# Install & load relevant package

install.packages("twitteR")

library(twitteR)

install.packages("plyr")

library(plyr)

# Setup connection with Twitter (/ handshake)
# Instructions Video - https://www.youtube.com/watch?v=lT4Kosc_ers

consumer_key = "zgF5SYjcj32oqAlYxRLUIymC8"

consumer_secret  = "fg131oeAB3yxLh45UCp88RNcnz5bYuFoX1wN5czexK0YH6qVzr"

access_token = "67944954-imQAFSmN9eDT8bCBXlVmvNRu9bYTUM93nKTRyc1Mv"

access_secret = "Hf0SIkfHDjMn3oTPDjmXANEyZRaSpMRmlxOy4I1UNEKKx"

setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)

# Download tweets

RCB_data = searchTwitter("RCB",n=100,lang="en")

head(RCB_data) # See some of the downloaded tweets

# Convert into text
# Instructions Video - https://www.youtube.com/watch?v=adIvt_luO1o

RCB_data_text = laply(RCB_data,function(t)t$getText()) # Note inline definition of function in laply function, a plyr library function

head(RCB_data_text)

# Load positive and negative word dictionaries
# URL - Positive Word Dictionary - http://www.idiap.ch/~apbelis/hlt-course/positive-words.txt
# URL - Negative Word Dictionary - http://ptrckprry.com/course/ssd/data/negative-words.txt

setwd("E:/GL PGPBA/Data Mining/Sentiment_Analysis") # Set Working Directory - this is where the dictionaries are saved

pos = scan("positive-words.txt",what="character",comment.char = ";")

neg = scan("negative-words.txt",what="character",comment.char = ";")

# RUn the Sentiment Analysis Algorithm
# URL - https://github.com/mjhea0/twitter-sentiment-analysis/blob/master/R/sentiment_new.R

source("sentiment.r") # Source the algorithm code

analysis = score.sentiment(RCB_data_text,pos,neg) # Call the algorithm function

table(analysis$score) # Indicates a very positive score - 0 implies neutral, -1 implies negative, 1 & above imply positive

hist(analysis$score) # Do a histogram