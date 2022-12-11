#! /usr/bin/env bash

set -ex

docker-compose stop
docker-compose up -d
python server/src/sagewhale.py
