from flask import Flask, request
import flask
import flask_restplus
from flask_restplus import fields

import utils

# import TelegramClient

app = Flask(__name__, template_folder='./app/templates')

api = flask_restplus.Api(app)

___chats = []

testModeleSendMes = api.model("Message", {'text': fields.String(min_length=1, max_length=200)})
createChatModel = api.model("Create chat", {'Название чата': fields.String(min_length=1, max_length=40),
                                            'Описание': fields.String(min_length=1, max_lengh=130),
                                            'Логины участников': fields.List(fields.String,
                                                                             description='Можно передать в строке логины или id участников строго в формате String')})

ns = api.namespace('api/chats', description='Управление чатами')


@ns.route('/')
class CategoryCollection(flask_restplus.Resource):
    def get(self):  # доделать
        """Возвращает все чаты"""
        return {}

    @api.response(201, 'Чат успешно создан')
    @api.expect(createChatModel)
    def post(self):  # доделать
        js_data = request.get_json()
        return {}


@ns.route('/<int:id>/')
@api.response(404, 'Указанный id не найден')
class CategoryItem(flask_restplus.Resource):
    @api.response(200, "Информация возвращена успешно")
    def get(self, id):  # доделать
        """Возвращает детали о чате"""
        return {'id': id}

    @api.response(200, 'Чат удален успешно')
    def delete(self, id):  # доделать
        """Удаляет чат"""
        return None


def start(port: int = None, debug: bool = None):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    start()
