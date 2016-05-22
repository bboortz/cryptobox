#!/bin/sh

export ENV=DEV

export PORT=8081
./api/app_api.py &

export PORT=8080
./frontend/app_frontend.py
