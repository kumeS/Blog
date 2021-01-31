#!/bin/bash

MY_DIRNAME=$(dirname $0)
cd $MY_DIRNAME

item='"猫種"@ja'

QUERY='query=select distinct ?neko ?nekoLabel ?image 
where {

?s rdfs:label '$item' . 
?neko wdt:P31|wdt:P279 ?s .
?neko wdt:P18 ?image . 

SERVICE wikibase:label { bd:serviceParam wikibase:language "ja,en" }

}'

Output='Accept: text/csv'
Endpoint='https://query.wikidata.org/sparql'

curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_02.txt

exit

