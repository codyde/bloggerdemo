from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from flask_assets import Bundle, Environment
import os
import sys
import subprocess
import json

app = Flask(__name__)
app.secret_key = "super secret key"

env = Environment(app)
js = Bundle('js/clarity-icons.min.js', 'js/clarity-icons-api.js',
            'js/clarity-icons-element.js', 'js/custom-elements.min.js')
env.register('js_all', js)
css = Bundle('css/clarity-ui-dark.min.css', 'css/clarity-icons.min.css')
env.register('css_all', css)

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
