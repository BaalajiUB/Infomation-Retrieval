# Infomation-Retrieval

#### 1 Data ingestion and Solr setup

  About 100,000 tweets (exclusive of retweets and duplicates) from 5 major ciites in the world in 5 different languages on 5 common topics across a period of a month are collected using Twitter REST API and is pre-processed i.e... emoticons, emojies, hashtags, mentions and URLs are removed from main data payload and they are stored as seperate properties along with other properties like the category of the tweet, language and location and is transformed and stored as JSON dumps using python programming language. This code can automatically go to sleep if the rate limit is exceeded and resumes tweet collection after 15 minutes which is the cooldown period for the tweeter REST API.

The created JSON dumps are pushed into a Solr core for indexing using the tweet JSON structure used for the JSON creation as the schema. The stopwords removal and stemming are done in Solr by modifying its schema.xml file before loading data for indexing.
Using Solr UI, the top 10 words used and top 10 hashtags are identified from all the data collected and the data is sliced and diced using Solr query interface.

Programming language: Python

#### 2 Boolean Query and Inverted Index

  Given the Lucene index of the MedPub corpus, a postings list is created as linked list of term: document ids. The created postings list is used to implement TAAT (Term-at-a-time) and DAAT (Document-at-a-time) boolean query processing with "Skip-pointers" to reduce the run-time. Then for various queries, the number of comparisons made using TAAT and DAAT are recorded and compared. 
Note: No in-built functions used for intersection and union of the posting lists.

Programming language: Java

