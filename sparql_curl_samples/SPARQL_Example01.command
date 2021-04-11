#!/bin/bash

MY_DIRNAME=$(dirname $0)
cd $MY_DIRNAME

QUERY='query=select ?o ?oLabel ?prop ?propLabel 
where {

wd:Q2374463 wdt:P31|wdt:P279 ?o ; ?p ?o .
?prop wikibase:directClaim ?p .
SERVICE wikibase:label { bd:serviceParam wikibase:language "ja" }

}'

Output='Accept: text/csv'
Endpoint='https://query.wikidata.org/sparql'
curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_01A.txt

Output='Accept: text/tab-separated-values'
curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_01B.txt

Output='Accept: application/sparql-results+json'
curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_01C.txt

Output='Accept: application/sparql-results+xml'
curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_01D.txt

exit
