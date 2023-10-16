from flask import Flask
import router.router as Routers
app = Flask(__name__)

app.register_blueprint(Routers.routers)


if __name__ == '__main__':
    app.run(debug=True)