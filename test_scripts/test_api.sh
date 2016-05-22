#!/bin/bash

set -i


if [ -z "$URL" ]; then
    URL="http://localhost:8081/api/file"
fi

curl --fail --insecure -H "Content-Type: application/json" -X POST --data "{\"key\": \"value-$RANDOM\" }" "$URL"
echo
curl --fail --insecure -H "Content-Type: text/plain" -X POST --data "content=value-$RANDOM" "$URL"
echo
curl --fail --insecure -X POST --data "content=value-$RANDOM" "$URL"
echo
curl --fail --insecure -H "Content-Type: application/json" -X GET "$URL/0"
echo
curl --fail --insecure -H "Content-Type: text/plain" -X GET "$URL/1"
echo
curl --fail --insecure -X GET "$URL/2"
echo

