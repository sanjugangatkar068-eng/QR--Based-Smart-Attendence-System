from flask import Flask, render_template, request, jsonify
import qrcode
import os
import uuid

app = Flask(__name__)