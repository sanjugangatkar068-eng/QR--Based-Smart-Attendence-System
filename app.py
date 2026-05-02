from flask import Flask, render_template, request, jsonify
import qrcode
import os
import uuid

app = Flask(__name__)

attendance = set() 

# Home Page
@app.route('/')
def home():
         return render_template('index.html')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')
@app.route('/generate_qr')
def generate_qr():
    session_id = str(uuid.uuid4())

img = qrcode.make(session_id)
    img.save("static/qr.png")

