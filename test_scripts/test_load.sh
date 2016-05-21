#!/bin/bash

set -i


if [ -z "$URL" ]; then
    URL="http://localhost:8080/api/file"
fi

for i in {1..1000}; do
	curl --fail --insecure -H "Content-Type: application/json" -X POST --data "{\"key\": \"value-$RANDOM\" }" "$URL"
	echo
done
