# Infomation-Retrieval

About 100,000 tweets from 5 major ciites in the world in 5 different languages on 5 common topics are collected using Twitter REST API and is pre-processed i.e... emoticons, emojies, hashtags, mentions and URLs are removed from main data payload and they are stored as seperate properties along with other properties like the category of the tweet, language and location and is transformed and stored as JSON dumps using python programming language. This code can automatically go to sleep if the rate limit is exceeded and resumes tweet collection after 15 minutes which is the cooldown period for the tweeter REST API.

The created JSON dumps are pushed into a Solr core for indexing using the tweet JSON structure used for the JSON creation as the schema.
Using Solr, the top 10 words used and top 10 hashtags are identified from all the data collected and the data is sliced and diced using Solr query interface.
