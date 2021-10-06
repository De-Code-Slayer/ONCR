from flask.helpers import make_response
from app import app, auth, session, request, url_for, redirect, Resource, api, reqparse
from app.user.controllers.places_controller import create_new_place, read_place, update_place

class places(Resource):
    def post(self):

         self.args = request.json
         place = create_new_place(self.args)
         return place

    def get(self):
        self.args = request.json
        print(self.args)
        if self.args == "None":

           place = read_place(self.args, method="all")
           return place
        else:
            place = read_place(self.args)
            return place
    
    def put(self):
        self.args = request.json
        update_data = update_place(self.args)
        return update_data








api.add_resource(places, '/api/user/places', endpoint="places")