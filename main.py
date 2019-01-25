from flask import Flask
from flask import render_template
from flask import request
from random import shuffle
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/hiragana')
def hiragana():
    return render_template("hiragana.html")

@app.route('/katakana')
def katakana():
    return render_template("katakana.html")

@app.route('/n5')
def n5():
    return render_template("n5.html")

@app.route('/n5_start', methods=['POST'])
def n5_start():
    kanji_list = [
        {"symbol": "耳", "hiragana": "みみ", "english": "ear"},
        {"symbol": "水", "hiragana": "みず", "english": "water"},
        {"symbol": "火", "hiragana": "か", "english": "fire"}
    ]

    if request.method == 'POST':
        if request.form['order_radios'] == "random":
            shuffle(kanji_list)
    
    return json.dumps(kanji_list)
    

