from index import app;
from whitenoise import WhiteNoise

def create_app():

    #wrap whitenoise around flask app to serve static files
    app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")

    return app