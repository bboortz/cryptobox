#!/bin/sh

export ENV=DEV
export API_PORT=8081

export PORT=8081
./api/app_api.py &

export PORT=8080
./frontend/app_frontend.py
