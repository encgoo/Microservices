#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encgoo@gmail.com
from flask import Flask, request, render_template, flash, jsonify, Response

app = Flask(__name__)


@app.route("/emo_sen", methods=["GET"])
def emo_sen():
    return render_template("sentiment.html")

@app.route("/")
def home():
    resp = Response("")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__=="__main__":
    app.run(host="0.0.0.0", port=9000)
