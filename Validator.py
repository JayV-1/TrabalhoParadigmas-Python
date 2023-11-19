# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:14:08 2023

@author: João Vitor
"""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)