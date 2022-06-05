from flask import Flask, request, render_template, send_from_directory
from main.views import catalog_blueprint, logging
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(catalog_blueprint)
app.register_blueprint(loader_blueprint)

if __name__ == "__main__":
    app.run()
