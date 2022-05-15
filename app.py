from resources.routes.who_is_live_twitch import WhoIsLiveTwitch
from utils import create_app
from flask_restful import Api

app = create_app()
api = Api(app)

api.add_resource(WhoIsLiveTwitch, "/wilt")

if __name__ == '__main__':
    app.run()
