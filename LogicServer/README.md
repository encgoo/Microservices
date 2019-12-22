# Logic Server

This is a Flask server that do the following logics:
* Given a sentence, compute its polarity
* Given a polarity, firnd the closest emoji

# Run as standalone
Run

```python3 sentiment.py```

## Test
Use the curl commands in this [folder](curl_test)

# Docker

## Build

Use 

```docker build -t sentiment-logc .```
_Note_: In the [Dockerfile](Dockerfile), we install
textblob, and also run a python command to download 
textblob corpora.

## Run
Run

```docker run -d -p 5050:5000 sentiment-logic```

## Test
Node that we mapped port 5000 of the container to port 5050
now. So do curl as like in [curl_test](curl_test),
but change the port to 5050. 

_Now important point_! Because of the mapping, the logic service 
can be accessed via either
* localhost:5050 or
* _container_ip_:5000

Use this to find the container ip:

```docker inspect _container_id | grep IPAddress```
In our example, the docker is running on 172.17.0.2

This is the information we need to use when
we start the container for the [ApiServer](../ApiServer/README.md).

