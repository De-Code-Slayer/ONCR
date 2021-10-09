from flask.helpers import make_response
from app import app, auth, session, request, url_for, redirect, Resource, api, reqparse
from app.houses.controllers.houses_controllers import create_new_house, read_house, update_house

class houses(Resource):
    def post(self):
         self.args = request.json
         house = create_new_house(self.args)
         return house

    def get(self):
        self.args = request.json
        print(self.args)
        if self.args == "None":

           place = read_house(self.args, method="all")
           return place
        else:
            place = read_house(self.args)
            return place
    
    def put(self):
        self.args = request.json
        update_data = update_house(self.args)
        return update_data








api.add_resource(houses, '/api/user/houses', endpoint="houses")