#!/bin/sh

export ENV=DEV

export PORT=8081
./app_api.py &

export PORT=8080
./app_frontend.py
