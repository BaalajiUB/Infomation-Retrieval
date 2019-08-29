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

#### 3 Evaluation of IR models

  3 IR models VSM (Vector Space Model), Okapi BM25 and DFR (Divergence from Randomness) are implemented in 3 seperate Solr cores and the top 20 query results are retrieved from each model along with the relevance scores of the retrieved documents. The resultant JSON is converted to TREC_eval (software used to evaluate an IR model) acceptable format.
  TREC_eval is used to get various matrices of the IR model to check its performance. The evaluation measure primarily considered in this project is MAP (Mean Average Precision). To improve performance of the models, the tunable parameters in each model are modified and each model had a final MAP value of 0.7 . Further techniques to improve the performance like query expansion, query boosting, translation (since the queries the models are tested are in 3 different languages) are discussed.
  
  
  #### 4 Tweelytics
   A team project. A web application is created to facilitate users to search the tweets stored and indexed in Solr. It takes in a query and returns the tweets matching the query along with the trending hashtags among the overall tweet collection on entering the web application and on querying, the trending hashtags within the query results. Additional filters like language, geo-location and topic are also provided along with the query. Then a page is included with statistical summary of the distribution of the query results across the features: language, location, date-of-posting and topics.  The project is done using Spring Boot framework. 
My contribution is fetching of the trending hashtags based on the situation and sending it to the UI component and providing the faceted results of the query for visualization of the tweets' demographic distribution.
    
Programming languate: Java
  
