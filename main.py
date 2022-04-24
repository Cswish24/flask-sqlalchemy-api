from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from user import UserRegister
from security import authenticate, identity
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = "balls"
api = Api(app)

# items = []

jwt = JWT(app, authenticate, identity) # creates /auth endpoint, makes wrapper work

#Item and Item list moved to item py, therefore imports jwt_required request, requestparser, and Resource moved


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=6000, debug=True)
