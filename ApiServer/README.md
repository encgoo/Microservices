# API server
This is a Flask server that severs the RESTful API.

## Run as standalone
python3 api_server.py

### Test
Use this curl command to test

```curl -X -H "Content-Type: application/json" POST http://localhost:7000/sen_emo -d '{"sentence": "Mary has a little lamb"}'``` 

## Docker Container

### Build
Use

```docker build -t sentiment-api .```

### Run docker container
_NOTE_: Important. You need to run the [LogicServer](../LogicServer/README.md) docker container first before 
you can start this container. Because it depends on the IP of the
logic server container.

After you started the container for the LogicServer, get its IP. Then use it below

Run

```docker run -d -p 7000:7000 -e LOGIC_SERVER='_logic_server_ip:5000' sentiment-api```
### Verify

```curl -X POST -H "Content-Type: application/json" http://localhost:7000/sen_emo -d '{"sentence":"Mary has a little lamb"}'```

