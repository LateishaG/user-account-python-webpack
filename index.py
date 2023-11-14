from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html>\
        <head>\
            <title>Python Test</title>\
            <script src='/static/bundle.js' defer></script>\
            <link rel='stylesheet' href='/static/styles.css' />\
            <meta name='viewport' content='initial-scale=1, width=device-width' />\
        </head>\
        <body>\
            <div id='root'></div>\
        </body>\
        </html>"