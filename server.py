from flask import Flask, request
import flask_restplus
from flask_restplus import fields
from pyrogram import Client

import TelegramClient
import utils

app = Flask(__name__, template_folder='./app/templates')

api = flask_restplus.Api(app)

___chats = []

testModeleSendMes = api.model("Message", {'text': fields.String(min_length=1, max_length=200)})

ns = api.namespace('api/chats', description='Управление чатами')

telegram_client = None


@ns.route('/')
class Chats(flask_restplus.Resource):
    createChatModelReq = api.model("Create chat",
                                   {'title': fields.String(min_length=1, max_length=128, description="Название чата"),
                                    'users': fields.List(fields.String(min_length=1),
                                                         description='Можно передать в строке логины или id участников строго в формате String'),
                                    'description': fields.String(min_length=1, max_length=255,
                                                                 description='Описание группы')})
    createChatModelAns = api.model("Create chat answer", {'chat_id': fields.Integer(), 'title': fields.String()})

    @api.response(201, 'Чат успешно создан')
    @api.expect(createChatModelReq)
    @ns.marshal_with(createChatModelAns)
    @utils.error_handler_for_http_answer
    def post(self):
        """Создание чата"""
        global telegram_client

        data = request.json
        ans = telegram_client.create_chat(data['title'], data['description'], data['users'])
        return {'chat_id': ans['id'], 'title': data['title']}, 201


@ns.route('/-<int:chat_id>/users/<string:user_id>/')
class ChatsUsers(flask_restplus.Resource):
    @api.response(201, "Пользователь добавлен")
    @utils.error_handler_for_http_answer
    def post(self, chat_id, user_id):
        """Добавление пользователя в чат"""
        global telegram_client
        try:
            user_id = int(user_id)
        except:
            user_id = user_id

        ans = telegram_client.add_members(0 - chat_id,
                                          user_id)  # 0 - chat_id потому что у чатов отрицательные id, а в функцию передается положительное id (>0)
        return ans, 201

    @api.response(204, "Пользователь удален")
    @utils.error_handler_for_http_answer
    def delete(self, chat_id, user_id):
        """Удаление пользователя из чата"""
        ans = telegram_client.kick_members(0 - chat_id, user_id)
        return True, 204


@ns.route('/-<int:chat_id>/message/')
class ChatMessage(flask_restplus.Resource):
    sendMessageInChatModelReq = api.model("Send message", {'text': fields.String(min_length=1, max_length=4096)})
    sendMessageInChatModelAns = api.model("Send message ans",
                                          {'chat_id': fields.Integer(), 'message_id': fields.Integer()})

    @api.response(201, "Сообщение отправлено")
    @api.expect(sendMessageInChatModelReq)
    @api.marshal_with(sendMessageInChatModelAns)
    @utils.error_handler_for_http_answer
    def post(self, chat_id):
        """Отправка сообщения"""
        global telegram_client

        data = request.json
        ans = telegram_client.send_message(0 - chat_id, data['text'])
        return {'chat_id': ans.chat.id, 'message_id': ans.message_id}, 201


@ns.route('/-<int:chat_id>/pin/')
class FixingChatMessage(flask_restplus.Resource):
    """Закрепление или открепление сообщения"""
    pinMessageReq = api.model("Pin message", {'message_id': fields.Integer()})

    @api.response(200, 'Сообщение было закреплено')
    @api.expect(pinMessageReq)
    @utils.error_handler_for_http_answer
    def post(self, chat_id):
        """Закрепление сообщения"""
        data = request.json
        ans = telegram_client.pin_message(0 - chat_id, data['message_id'])
        return ans, 200

    @api.response(204, "Сообщение было откреплено")
    @utils.error_handler_for_http_answer
    def delete(self, chat_id):
        telegram_client.unpin_message(0 - chat_id)
        return True, 204


@ns.route("/-<int:chat_id>/admins/<string:user_id>")
class ChatAdmins(flask_restplus.Resource):
    @api.response(201, "Админ добавлен")
    @utils.error_handler_for_http_answer
    def post(self, chat_id, user_id):
        """Добавление админ в чат"""
        global telegram_client
        try:
            user_id = int(user_id)
        except:
            user_id = user_id

        telegram_client.add_admin(0 - chat_id, user_id)
        return True, 201


def start(port: int = None, debug: bool = None):
    _config = utils.get_config()
    with Client('anon', _config['api_id'], _config['api_hash']) as client:
        global telegram_client

        telegram_client = TelegramClient.TelegramAPI(client)
        app.run(port=port, debug=debug)


if __name__ == '__main__':
    start()
