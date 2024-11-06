from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("/workspaces/lilis-wohnzimmer/Templates/index.html")