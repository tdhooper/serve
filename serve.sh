#!/bin/bash
DIR="$(cd ../../../; pwd)"
HOST=localhost
PORT=4433
echo "Serving $DIR from https://$HOST:$PORT"
python serve.py $DIR $HOST $PORT
