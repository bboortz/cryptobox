#!/bin/bash


if [ -z "$URL" ]; then
	URL="http://localhost:8080/api/file"
fi

curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": \"value-$RANDOM\" }" "$URL"
#curl --insecure -H "Content-Type: application/json" -X POST --data "." "$URL"
#curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": { \"key-$RANDOM\": \"value-$RANDOM\" } }" ${URL}
#curl --insecure -H "Content-Type: application/json" -X GET "$URL"

