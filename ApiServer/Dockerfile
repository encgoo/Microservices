# Use python3 as parent image
FROM python:3.5-slim
WORKDIR /app
ENV LOGIC_SERVER http://localhost:5000
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install --trusted-host pypi.python.org requests
CMD ["python", "api_server.py"]