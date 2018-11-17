from flask import Flask, request
from flask_restplus import Api, Resource

# ==============================================================
# Flask REST API for Testing
# ==============================================================

app = Flask(__name__)
api = Api(app,
          prefix='/v1',
          version='1.0',
          title='Flask REST API Testing',
          description='A REST API to validate the test harness, FlaskTestingRestApiClient',
          catch_all_404s=True)

test_ns = api.namespace('testing', description='Testing operations')


@test_ns.route('/goodbye/<tag>')
class GoodbyeTester(Resource):
    """ Hello Tester.

    Store a "hello" message, show it, & delete it!
    """

    def delete(self, tag):
        return {"message": "goodbye"}, 204


@test_ns.route('/hello')
class HelloTester(Resource):
    """ Hello Tester.

    Store a "hello" message, show it, & delete it!
    """

    def get(self):
        hello_message = 'hello tester'
        return {"message": hello_message}, 200

    def post(self):
        hello_message = request.json.get('message', None)
        return {"message": hello_message}, 201


if __name__ == '__main__':
    app.run(debug=True)
