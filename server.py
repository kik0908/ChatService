from flask import Flask, request
import flask
import flask_restplus
from flask_restplus import fields
from pyrogram import Client

import TelegramClient
import utils

from time import time

# import TelegramClient

app = Flask(__name__, template_folder='./app/templates')

api = flask_restplus.Api(app)

___chats = []

testModeleSendMes = api.model("Message", {'text': fields.String(min_length=1, max_length=200)})
createChatModel = api.model("Create chat",
                            {'title': fields.String(min_length=1, max_length=40, description="Название чата"),
                             'users': fields.List(fields.String,
                                                  description='Можно передать в строке логины или id участников строго в формате String')})

ns = api.namespace('api/chats', description='Управление чатами')

telegram_client: TelegramClient.TelegramAPI = TelegramClient.TelegramAPI(None)


@ns.route('/')
class CategoryCollection(flask_restplus.Resource):
    def get(self):  # доделать
        """Возвращает все чаты"""
        return {}

    @api.response(201, 'Чат успешно создан')
    @api.expect(createChatModel)
    @utils.error_handler
    def post(self):
        global telegram_client

        data = request.json
        telegram_client.create_chat(data['title'], data['users'])
        return True, 201


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
    _config = utils.get_config()
    with Client('anon', _config['api_id'], _config['api_hash']) as client:
        global telegram_client

        telegram_client = TelegramClient.TelegramAPI(client)
        app.run(port=port, debug=debug)


if __name__ == '__main__':
    start()
