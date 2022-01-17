from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)

@api.route('/api/helloworld')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)