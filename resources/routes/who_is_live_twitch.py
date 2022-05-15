from flask_restful import Resource


class WhoIsLiveTwitch(Resource):
    @classmethod
    def get(cls):
        return {"sucess": True}
