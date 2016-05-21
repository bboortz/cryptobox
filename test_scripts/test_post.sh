#!/bin/bash

set -i


if [ -z "$URL" ]; then
    URL="http://localhost:8080/api/file"
fi

curl --fail --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": \"value-$RANDOM\" }" "$URL"
curl --fail --insecure -H "Content-Type: text/plain" -X POST --data "content=value-$RANDOM" "$URL"
curl --fail --insecure -X POST --data "content=value-$RANDOM" "$URL"
curl --fail --insecure -H "Content-Type: application/json" -X GET "$URL/0"
curl --fail --insecure -H "Content-Type: text/plain" -X GET "$URL/1"
curl --fail --insecure -X GET "$URL/2"

