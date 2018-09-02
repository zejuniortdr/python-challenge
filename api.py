from flask import Flask, request
from flask_restful import Resource, Api
from tree import loaddata

app = Flask(__name__)
api = Api(app)

T = loaddata()


class Autocomplete(Resource):
    def get(self):
        q = request.args.get('q', default='', type=str)
        limit = request.args.get('limit', default=5, type=int)
        return {'patients': T.search(q, limit)}


api.add_resource(Autocomplete, '/autocomplete/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
