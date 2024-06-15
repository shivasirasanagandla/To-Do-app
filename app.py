# app.py
import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView
from keycloak import KeycloakOpenID
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

keycloak_openid = KeycloakOpenID(server_url="https://keycloak-server/auth/",
                                 client_id="21CS002421",
                                 realm_name="shiva_2421",
                                 client_secret_key=os.getenv('KEYCLOAK_CLIENT_SECRET'))

from schema import schema

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
