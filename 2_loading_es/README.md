Stage 2: Loading data into Elasticsearch
-------------------------------------------------

Before we start to load data into Elasticsearch, it helps to understand what it is. This document will go through some key points, but there is extensive documentation on the https://www.elastic.co site.

Elasticsearch provides two key capabilities - create and maintain indices based on 'documents', and a powerful search service to query these indices. It holds data in a conceptually similar way to a relational database:

Typical database model:

	+---------+    +---------+    +---------+
	| Database+--> |    Table+--> |      Row|
	+---------+    +---------+    +---------+

Elasticsearch model:

	+---------+    +---------+    +---------+
	|    Index+--> |     Type+--> | Document|
	+---------+    +---------+    +---------+

Like a database, each Document (eg row) needs to have an 'id' value (primary key) that is unique to the index and document type (table) it is in. You use this id to update, fetch and to delete the document from the index.

Unlike a database, it's primary purpose is not to provide the data you provide perfectly. It will build an index based on this data and based on what the data is and how it has been configured and the primary purpose is to provide discovery and analytics on this data.

###Analysis, Tokenising and Stemming###

Indexes are built to facilitate searching and fast-access based on search terms and/or parameters. Often, the search term is a single word, a partial match or even a few terms that might appear in the thing we are looking for. When data is analysed by elasticsearch, it breaks it up and condenses it so that it can quickly respond to search terms. 

The first step is *tokenising*. If we don't tell the service otherwise, it will break up any data by using spaces within the text. For example:

	"Quick brown fox ran" --> "quick", "brown", "fox", "ran"

By default, the next step is to attempt something called *stemming*. Written language is often odd, unusual and full of quirks. Stemming is an attempt to break down words back to a stem, so that searches with natural variations on a word will work. For example:

	"running" -- English Stemmer --> "run"
	"ran" -- English Stemmer --> "run"
	"run" -- English Stemmer --> "run"

Elasticsearch will attempt to do the best it can with the data it is given. It will attempt to tokenise and stem all the fields entered. Obviously, stemming and tokenising is a bad thing for many types of field, such as dates, identifiers and proper nouns (names, etc).

###Mapping###

A 'mapping' is a document that describes how we want elasticsearch to analyse documents in a particular index. In short, we can use a mapping to ensure that dates are treated as dates, people's names are not stemmed, and that text is analysed as we wish.

**Setup:**

There are a few steps required to get set up for working with elasticsearch and python and it is useful to step through them yourself so that you can do it on a different system later on.

Go to https://www.elastic.co/products/elasticsearch and download the latest version of elasticsearch and get the 'TAR' version. Open a terminal and decompress the file. ('tar -xvf elasticsearch-2.2.0.tar.gz')

Once decompressed, move into the directory elasticsearch-2.2.0, and run the following command:

	[foobar] $ ./bin/elasticsearch

It should take a few moments, but once it stops loading you will have an instance of elasticsearch running! Go to http://localhost:9200 to check that you can see something there. You are running elasticsearch within a terminal session, and if the session is closed (ie you close the window), elasticsearch will be closed. 

> This is fine for experimentation and developing ideas but not something recommended for a service you want running all the time. The elasticsearch site has documentation on how to run it on a more permanent basis.

Once you have done that, open a fresh terminal window (without closing the other one) and move to the 2_loading_es directory. In there is a small script that will help you get set up further:

	[foobar] $ bash ./prepare_environment.sh
Stage 2: Loading data into Elasticsearch
-------------------------------------------------

Before we start to load data into Elasticsearch, it helps to understand what it is. This document will go through some key points, but there is extensive documentation on the https://www.elastic.co site.

Elasticsearch provides two key capabilities - create and maintain indices based on 'documents', and a powerful search service to query these indices. It holds data in a conceptually similar way to a relational database:

Typical database model:

	+---------+    +---------+    +---------+
	| Database+--> |    Table+--> |      Row|
	+---------+    +---------+    +---------+

Elasticsearch model:

	+---------+    +---------+    +---------+
	|    Index+--> |     Type+--> | Document|
	+---------+    +---------+    +---------+

Like a database, each Document (eg row) needs to have an 'id' value (primary key) that is unique to the index and document type (table) it is in. You use this id to update, fetch and to delete the document from the index.

Unlike a database, it's primary purpose is not to provide the data you provide perfectly. It will build an index based on this data and based on what the data is and how it has been configured and the primary purpose is to provide discovery and analytics on this data.

###Analysis, Tokenising and Stemming###

Indexes are built to facilitate searching and fast-access based on search terms and/or parameters. Often, the search term is a single word, a partial match or even a few terms that might appear in the thing we are looking for. When data is analysed by elasticsearch, it breaks it up and condenses it so that it can quickly respond to search terms. 

The first step is *tokenising*. If we don't tell the service otherwise, it will break up any data by using spaces within the text. For example:

	"Quick brown fox ran" --> "quick", "brown", "fox", "ran"

By default, the next step is to attempt something called *stemming*. Written language is often odd, unusual and full of quirks. Stemming is an attempt to break down words back to a stem, so that searches with natural variations on a word will work. For example:

	"running" -- English Stemmer --> "run"
	"ran" -- English Stemmer --> "run"
	"run" -- English Stemmer --> "run"

Elasticsearch will attempt to do the best it can with the data it is given. It will attempt to tokenise and stem all the fields entered. Obviously, stemming and tokenising is a bad thing for many types of field, such as dates, identifiers and proper nouns (names, etc).

###Mapping###

A 'mapping' is a document that describes how we want elasticsearch to analyse documents in a particular index. In short, we can use a mapping to ensure that dates are treated as dates, people's names are not stemmed, and that text is analysed as we wish.

**Setup:**

There are a few steps required to get set up for working with elasticsearch and python and it is useful to step through them yourself so that you can do it on a different system later on.

Go to https://www.elastic.co/products/elasticsearch and download the latest version of elasticsearch and get the 'TAR' version. Open a terminal and decompress the file. ('tar -xvf elasticsearch-2.2.0.tar.gz')

Once decompressed, move into the directory elasticsearch-2.2.0, and run the following command:

	[foobar] $ ./bin/elasticsearch

It should take a few moments, but once it stops loading you will have an instance of elasticsearch running! Go to http://localhost:9200 to check that you can see something there. You are running elasticsearch within a terminal session, and if the session is closed (ie you close the window), elasticsearch will be closed. 

> This is fine for experimentation and developing ideas but not something recommended for a service you want running all the time. The elasticsearch site has documentation on how to run it on a more permanent basis.

Once you have done that, open a fresh terminal window (without closing the other one) and move to the 2_loading_es directory. In there is a small script that will help you get set up further:

	[foobar] $ bash ./prepare_environment.sh

Follow the directions to go into the python environment.

###Getting started with python and elasticsearch###

Run a python session and load the elasticsearch client:

	[foobar] $ python
	>>> from elasticsearch import Elasticsearch

NB Capitalisation here is important!

Now we can create a client that will connect to the elasticsearch you have running:

	>>> es = Elasticsearch()

If this succeeds then you will have a connection and can start to index and explore the data.

**Task 1:**

Aim: Loading the fixed_data.csv into elasticsearch by opening the csv, stepping through it line by line using csv.DictReader and indexing each row. 

You will find the code you wrote out for Task 1 of the previous stage very helpful here. You should save a copy in this folder (2_loading_elasticsearch) and edit it to include the two lines required to make an elasticsearch connection.

Instead of 'printing' out each row, you need to index it. You'll need to tell it what index name to store it under ("database"), and what its 'doc_type' is (ie table name). We will call the index "books", and the type "basic". We'll also have to give each one a unique id and so, we'll make that the line number it came from. There is a trick you can use, and the lines you need to write is as follows:

	for idx, row in enumerate(*name of csv DictReader thing*):
	  es.index(index="books", doc_type="basic", id=idx+1, body=row)

(Replace the \*name of csv... etc\* with the variable name you've used)

**Task 2:**

There is another csv in this folder called 'tag_history.tsv'. Make a new copy of the code to load the 'fixed_data.csv' and alter it to load this data. Index the data in an index called "flickr", and doc_type "tag_data". This is a TSV (tab separated values) and only needs a small addition to be able to load it using the DictReader:

csv.DictReader(f, **delimiter="\t"**)

The index line will need the new index and doc_type names added, and you will need to use another column for the source of the id's:

	id=int(row['flickr_id'])

