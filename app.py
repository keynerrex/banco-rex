from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()


def create_app(app):
    csrf.init_app(app)

    @app.route('/Inicio')
    def home():
        return 'Bienvenido a Caja Rex', 200

    @app.errorhandler(404)
    def page_not_found(error):
        return 'Pagina no encontrada', 404
    return app


if __name__ == '__main__':
    app = create_app(app)

    app.run(host='0.0.0.0', port='8080', debug=True)
