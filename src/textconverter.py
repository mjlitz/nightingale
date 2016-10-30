"""
Program to convert the text into an abcjs output music/midi file
"""
import os
import json
from flask import Flask, request

textconverter = Flask(__name__)

@app.route('/is_running', methods=['POST'])
def isRunning():
        process_name = request.values.get('name', None)

def parse_text():
    with open('data.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
        return data

if __name__ == "__main__":
        textconverter.run()
