from flask import Flask
from flask_restful import Resource, Api
import json
import codecs
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
UNIVERSITY_PATH = os.path.join(APP_ROOT, "university.json")
BUS_PATH = os.path.join(APP_ROOT, "bus.json")
FOOD_PATH = os.path.join(APP_ROOT, "food.json")

app = Flask(__name__)
api = Api(app)

class UniversityListRes(Resource):
    def get(self):
        with codecs.open(UNIVERSITY_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)


class FoodListRes(Resource):
    def get(self):
        with codecs.open(FOOD_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)


class BusListRes(Resource):
    def get(self):
        with codecs.open(BUS_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(UniversityListRes, "/api/university")
api.add_resource(FoodListRes, "/api/food")
api.add_resource(BusListRes, "/api/bus")


if __name__ == '__main__':
    app.run(port=2612)
