Stage 3: Querying Elasticsearch
-------------------------------------------------

(using 'es' as the Elasticsearch client object as before)

	>>> es.search(index=..., doc_type=..., body=...)

The "body" term is where all the flexibility is. There are a huge number of different modes of searching so do not consider the following to be exhaustive by any means.

**Basic queries:**

Search for matches:

	>>> query = { "query": {"match": {"author": "HALCOMBE"}}}
	>>> es.search(index="book", doc_type="basic", body=query)

Search by prefix:

	>>> query = { "query": {"prefix": {"author": "HAL"}}}
	>>> es.search(index="book", doc_type="basic", body=query)

Search for exact term matches:

	>>> query = { "query": {"term": {"author": "HALCOMBE"}}}
	>>> es.search(index="book", doc_type="basic", body=query)

###Why are my searches failing?###

> String fields can be analyzed (treated as full text, like the body of an email), or not_analyzed (treated as exact values, like an email address or a zip code). Exact values (like numbers, dates, and not_analyzed strings) have the exact value specified in the field added to the inverted index in order to make them searchable.

> By default, however, string fields are analyzed. This means that their values are first passed through an analyzer to produce a list of terms, which are then added to the inverted index.

> There are many ways to analyze text: the default standard analyzer drops most punctuation, breaks up text into individual words, and lower cases them. For instance, the standard analyzer would turn the string “Quick Brown Fox!” into the terms [quick, brown, fox].

> This analysis process makes it possible to search for individual words within a big block of full text.

The *term* query looks for the exact term in the field’s inverted index — it doesn’t know anything about the field’s analyzer. This makes it useful for looking up values in not_analyzed string fields, or in numeric or date fields. When querying full text fields, use the match query instead, which understands how the field has been analyzed.

###Apply a mapping###

	mapping = { "special" :{
      "properties": {
        "sysnum":  { "type": "string", "index": "not_analyzed"},
        "author":  { "type": "multi_field",
            "fields": {
                "author": {"type": "string"},
                "original": {"type" : "string", "index" : "not_analyzed"}
            }
         },
        "title":   {
          "type": "string",
          "analyzer": "standard",
          "store": "true"
        },
        "date":    { "type": "integer" },
        "place":   { "type": "string", "index": "not_analyzed"}
        }
      }
    }

This is a mapping to stop Elasticsearch from analysing certain fields within the book metadata, and enhances the title field. The interesting change is that this mapping indexes the author field twice - once as it had before, and a second time without any analysis. This will allow us to search the name field by term and by exact matches, which is quite helpful here. The author data is from an authorative source, and should be identical between records if the author is the same.

To apply the mapping, you need to create a new blank index and set the mapping at the start:

	>>> es.indices.create(index="special")
	>>> es.indices.put_mapping(index = "special", doc_type = "special", body = mapping)

###Query context and Filter context###

So far, we've seen a few searches that have used a 'query' context. There is also a 'filter' context available as well and it can be a powerful tool.

>Query context
>A query clause used in query context answers the question “How well does this document match this query clause?” Besides deciding whether or not the document matches, the query clause also calculates a _score representing how well the document matches, relative to other documents.

Query context is in effect whenever a query clause is passed to a query parameter, such as the query parameter in the search API.

>Filter context
>In filter context, a query clause answers the question “Does this document match this query clause?” The answer is a simple Yes or No — no scores are calculated. Filter context is mostly used for filtering structured data, e.g.

	Does this timestamp fall into the range 2015 to 2016?
	Is the status field set to "published"?

For example, to search for the books with "Les" in the title, but only return those that were published after (greater than -> 'gte') 1850:

	>>> es.search(index="book", body={"query":{"match":{"title": "Les"}}, "filter": { "range": { "date": { "gte": "1850" }}} })

Or to just filter based on all documents:

	>>> query = {"query": {
                       "filtered": {
                         "query": {
                           "match_all": {
                         }
                       },
                     "filter": {
                       "term": { "date": 1850 }
                       }
                     }
                   }}
	>>> es.search(index="book", body=query)

The Query DSL (Domain Specific Language) is very capable and likewise, requires good documentation to understand well. There are lots of possibilities to explore and the start of the documentation can be found at: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html

**Task 1:**

Load the fixed_data.csv into the 'special' index as previously defined.

**Task 2:**

Search for the following:

Books published in:

 - London
 - Trondhjem
 - Москва
 - Spain

Which books have the above cities in their titles?

**Task 3:**

Open the fixed_data.csv and try to find specific rows by using the query interface alone.

