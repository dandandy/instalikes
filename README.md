# Instalike

First start the selenium server by running `docker-compose up`

The set your instagram email address and password on your host environment `export USER=xxxxxx && export PASSWORD=xxxxxx && export SERVER=http://localhost:4444/wd/hub`

Then run the app with `docker run --network=host -e USER -e PASSWORD -e SERVER barbarbar/instalike`
