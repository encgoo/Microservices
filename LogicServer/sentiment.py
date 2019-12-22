#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encgoo@gmail.com
#

import csv
from textblob import TextBlob
from flask import Flask, request, jsonify


class Emoji:
    def __init__(self):
        self.emoji_sen = {}
        self.compute_sentiment()

    def compute_sentiment(self):
        line_count = 0
        infile = open("Emoji_Sentiment_Data_v1.0.csv", "r")
        if infile:
            csv_reader = csv.reader(infile, delimiter=',')
            for row in csv_reader:
                if line_count > 0:
                    emoji = row[1]
                    pos = int(row[4])
                    neu = int(row[6])
                    neg = int(row[5])

                    polarity = (pos - neg) / (pos + neg + neu)

                    self.emoji_sen[emoji] = polarity

                line_count += 1
    def get_emoji(self, polarity):
        min_diff = 2
        emojo = None
        emo_polarity = polarity
        for emo in self.emoji_sen:
            diff = abs(self.emoji_sen[emo] - polarity)
            if diff < min_diff:
                emo_polarity = self.emoji_sen[emo]
                min_diff = diff
                emojo = emo
        return {
            "emojo": emojo,
            "polarity": emo_polarity
        }

app = Flask(__name__)
emoji = Emoji()


@app.route("/sentiment", methods=["POST"])
def sentiment():
    sentence = request.get_json().get("sentence", None)
    polarity = 0.0
    if sentence:
        polarity = TextBlob(sentence).sentences[0].polarity
    ret = {
        "sentence": sentence,
        "polarity": polarity
    }
    return jsonify(ret)


@app.route("/emoji", methods=["POST"])
def get_emo():
    global emoji
    polarity = request.get_json().get("polarity", 0)
    return jsonify(emoji.get_emoji(polarity))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
