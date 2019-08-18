from flask import Flask
import flask
import flask_restplus

# import TelegramClient

app = Flask(__name__, template_folder='./app/templates')

api = flask_restplus.Api(app, default='Default')

___chats = []

ns = api.namespace('api', description='Operations related to blog categories')


@ns.route('/chats/')
class CategoryCollection(flask_restplus.Resource):
    def get(self):
        """Returns list of blog categories."""
        return {}

    @api.response(201, 'Category successfully created.')
    def post(self):
        """Creates a new blog category."""
        return {}


@ns.route('/<int:id>/')
@api.response(404, 'Category not found.')
class CategoryItem(flask_restplus.Resource):
    def get(self, id):
        """Returns details of a category."""
        return {'id': id, 'dg': 'gh'}

    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """Updates a blog category."""
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """Deletes blog category."""
        return None, 204


def start(port: int = None, debug: bool = None):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    start()
