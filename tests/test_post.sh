#!/bin/bash

URL="https://cryptobox-bboortz.c9users.io/api/file"

curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": \"value-$RANDOM\" }" "$URL"
#curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": { \"key-$RANDOM\": \"value-$RANDOM\" } }" ${URL}
#curl --insecure -H "Content-Type: application/json" -X GET "$URL"

