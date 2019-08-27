# Infomation-Retrieval

About 100,000 tweets from 5 major ciites in the world in 5 different languages on 5 common topics are collected using Twitter REST API and is pre-processed i.e... stopwords, emoticons, emojies, stemming and extraction of hashtags are URL are performed on the input data and is transformed and stored as JSON files using python programming language.

The created JSON files are pushed into Solr for indexing using the JSON structure as the schema.
Using Solr, the top 10 words used and top 10 hashtags are identified from all the data collected.
