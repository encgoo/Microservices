# Web Service

This is a  Flask server that provides static webservice.

## Run as standalone
Use 

```python3 app.py```

It is serving at point 9000

Use http://localhost:9000/emo_sen to access the web service.

## Build docker image
Run

```docker build -t sentiment-web .```

_Note_ because we are going to run minkube, so we keep all the docker images local.

## Run the container
### Start
```docker run -d -p 9000:9000 sentiment-web```

### Verify
Use

```docker ps -a``` to check that sentiment-web is running

Use http://localhost:9000/emo_sen to access the web service. Alse take note of the container id.

### Stop
Use

```docker stop _container_id``` to stop the container. You just need to type the first several chars 
of the container id (enough to distinguish).
