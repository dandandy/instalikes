#!/usr/bin/env bash
set -euo pipefail

docker-compose up -d --remove-orphans

until nc -vzw 2 localhost 4444; do sleep 5; done

export SERVER=http://localhost:4444/wd/hub

docker pull barbarbar/instalike
docker run --network=host -e USER -e PASSWORD -e SERVER barbarbar/instalike

docker-compose down
