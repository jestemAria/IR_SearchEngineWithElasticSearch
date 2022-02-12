# IR_SearchEngineWithElasticSearch

This is the final project of the Information Retrieval course.  
It uses ElasticSearch as a backend and all data is referred to Hamshahri Corpus.  
**ATTENTION!** Due to the protection of property rights of the corpus, this repository uploaded only 7 docs for the sample.
------
* Professor: Dr. Saeed Rahmani
* February 2022

### About the project
The project will search the documents in the corpus and return the results.  
It works with Persian and Arabic languages because the corpus is in Persian.  
Currently, it does not have any GUI, but a simple command line interface is provided.  

> Before start, you need to install ElasticSearch and the dependencies.  
> 1- Run setup.py to create the index.  
> 2- Head to the index.py to index the docs and insert them to elasticsearch.  
> 3- Run the main.py to start the search engine.

### The project structure flow
* The program will first connect to the ElasticSearch server and create a new index.  
* It will ask you a query, and it will search the index for the query.  
* It will suggest you to complete the query.  
* The given query will be parsed and the words will be tokenized.  
* The words will be corrected if they are not correct in spelling.  
* The TF-IDF algorithm will be applied to the words.  
* The documents that contain the words will be ranked according to their TF-IDF scores.  

### Index mapping table
|Data     |Type         |Index    |Analyzer|Similarity        |
|---------|-------------|---------|--------|------------------|
|DOCID    |text         |False    |None    |None              |
|CAT      |text         |True     |Persian |None              |
|TITLE    |text         |True     |Persian |`text_similarity` |
|TEXT     |text         |True     |Persian |None              | 
