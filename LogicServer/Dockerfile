# Use python3 as parent image
FROM python:3.5-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install --trusted-host pypi.python.org textblob && \
    python -m textblob.download_corpora
EXPOSE 5000
CMD ["python", "sentiment.py"]