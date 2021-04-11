#!/bin/bash

MY_DIRNAME=$(dirname $0)
cd $MY_DIRNAME

QUERY='query=
PREFIX ic: <http://imi.ipa.go.jp/ns/core/rdf#>
PREFIX dsv: <http://datashelf.jp/ns/dsv#>

select distinct ?s ?o 
where {
?s ?p ic:施設型 .
?s rdfs:label ?o . FILTER regex (?o, "都島区", "i")
}'

Output='Accept: text/csv'
Endpoint='https://data.city.osaka.lg.jp/sparql'

curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_03A.txt

QUERY='query=
PREFIX ic: <http://imi.ipa.go.jp/ns/core/rdf#>
PREFIX dsv: <http://datashelf.jp/ns/dsv#>

select distinct ?s ?o 
where {
?s ?p ic:イベント型 .
?s rdfs:label ?o . FILTER regex (?o, "都島区", "i")
}'

Output='Accept: text/csv'
Endpoint='https://data.city.osaka.lg.jp/sparql'

curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_03B.txt

QUERY='query=
PREFIX ic: <http://imi.ipa.go.jp/ns/core/rdf#>
PREFIX dsv: <http://datashelf.jp/ns/dsv#>

select distinct ?s ?sLabel ?o1 ?o2 ?o3 
where {
?s ?p ic:施設型 . 
?s rdfs:label ?sLabel .
?s ic:種別 "警察・消防/警察・交番" . 
?s ic:住所 / ic:区 ?o1 . 
?s ic:地理座標 / ic:緯度 ?o2 . 
?s ic:地理座標 / ic:経度 ?o3 . 
}'

Output='Accept: text/csv'
Endpoint='https://data.city.osaka.lg.jp/sparql'

curl -H "$Output" --data-urlencode "$QUERY" $Endpoint > test_03C.txt

exit

