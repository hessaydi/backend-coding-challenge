from flask import Flask , render_template, request, redirect
from flask_restful import reqparse, abort, Api, Resource
from helpers import langs
import json
# app = Flask(__name__)
app = Flask(__name__)
api = Api(app)

class Repos(Resource):
    def get(self):
        return langs()

api.add_resource(Repos, '/')

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
