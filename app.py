from flask import Flask
from database import db
from flask_migrate import Migrate
from models import Usuario, Pedido, Pizza
from modulos.usuarios.usuarios import bp_usuario
from modulos.pizzas.pizzas import bp_pizza
from modulos.pedidos.pedidos import bp_pedido

app = Flask(__name__)
app.config['SECRET_KEY'] = "QualquerCoisaSecreta"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(bp_usuario, url_prefix='/usuarios')
app.register_blueprint(bp_pizza, url_prefix='/pizzas')
app.register_blueprint(bp_pedido, url_prefix='/pedidos')