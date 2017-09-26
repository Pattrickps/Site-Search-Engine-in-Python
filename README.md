# Site-Search-Engine-in-Python
Steps for making a website search engine is similar to making a search engine like google, only difference is that seed page remains the home page of your website. 
# Approach and steps towards the project :
## 1. Web Crawling :
A web crawler (also known as a web spider or web robot) is a program or automated script which browses the World Wide Web in a methodical, automated manner. A web crawler can be simply made using the “ urllib “ library in the python. The input url gives the page source ( html ), in bytes format which can be converted into strings. Now we search for information data like in tags <l>, <p>  avoiding tags like <button> etc. We index all this data. We also the search for link within the page in <a href></a href> tags to crawl to other pages linked to it. This method of collecting relevant information is called parsing.

## 2. Indexing :
Search engine indexing collects, parses, and stores data to facilitate fast and accurate information retrieval. Index design incorporates interdisciplinary concepts from linguistics, cognitive psychology, mathematics, informatics, and computer science. An alternate name for the process in the context of search engines designed to find web pages on the Internet is web indexing.
an inverted index (also referred to as postings file or inverted file) is an index data structure storing a mapping from content, such as words or numbers, to its locations in a database file, or in a document or a set of documents (named in contrast to a Forward Index, which maps from documents to content). The purpose of an inverted index is to allow fast full text searches, at a cost of increased processing when a document is added to the database.
There are two main variants of inverted indexes: A record-level inverted index (or inverted file index or just inverted file) contains a list of references to documents for each word. A word-level inverted index (or full inverted index or inverted list) additionally contains the positions of each word within a document. The latter form offers more functionality (like phrase searches), but needs more processing power and space to be created.

We have implemented record-level inverted index in our project. We parsed our crawled webpages. This is basically the dictionary, in which it contains the keywords and the links in which those keywords were found.

## 3.)Building the Hash Table :
A hash table (hash map) is a data structure used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

# Tools and Platforms Used :
As mentioned in the beginning we used simple Python 2.7.12 IDLE for our testing and development. 

