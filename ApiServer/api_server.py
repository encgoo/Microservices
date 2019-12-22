#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encgoo@gmail.com
#

import os
from flask import Flask, request, jsonify, Response, make_response
import requests
import json
import logging

logging.basicConfig(filename="api_server.log", level=logging.DEBUG)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

LOGIC_SERVER = os.environ.get("LOGIC_SERVER", "http://localhost:5000")

#
#   Use env_var to find the other services?
#

@app.route("/sen_emo", methods=["POST", "OPTIONS"])
def sen_emo():
    if request.method == "OPTIONS":
        #
        # Support CORS preflight
        #
        logging.DEBUG("OPTIONS call.")
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = "POST"
        resp.headers['Access-Control-Allow-Headers'] = "Content-Type"
        resp.headers['Allow'] = "POST"
        return resp

    sentence = request.get_json().get("sentence", None)
    logging.debug("Input sentence: {}".format(sentence))

    data = {
        "sentence": sentence
    }
    logging.debug("POSTING to {}/sentiment".format(LOGIC_SERVER))
    resp = requests.post(LOGIC_SERVER + "/sentiment",
                         json=data)
    ret_dict = resp.json()
    polarity = ret_dict.get("polarity", 0.0)

    data_pol = {
        "polarity": polarity
    }
    logging.debug("Get polarity".format(polarity))

    logging.debug("POSTING to {}".format(LOGIC_SERVER))

    resp = requests.post(LOGIC_SERVER + "/emoji",
                         json=data_pol)
    ret_dict = resp.json()
    emojo = ret_dict["emojo"]
    logging.debug("Get emoji: {}".format(emojo))

    ret = {
        "sentence": sentence,
        "polarity": polarity,
        "emojo": emojo
    }
    #
    # Add header to support CORS
    #
    return make_response(json.dumps(ret, ensure_ascii=False), 200,
                         {"Access-Control-Allow-Origin": "*"})
    #return jsonify(ret)

@app.route("/")
def sen_emo_opt():
    resp = Response("")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)