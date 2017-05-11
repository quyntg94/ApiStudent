from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os
import mlab
from mongoengine import *

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
UNIVERSITY_PATH = os.path.join(APP_ROOT, "university.json")
BUS_PATH = os.path.join(APP_ROOT, "bus.json")
FOOD_PATH = os.path.join(APP_ROOT, "food.json")

app = Flask(__name__)
api = Api(app)
mlab.connect()

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, location="json", help="Name")
parser.add_argument("phone", type=str, location="json", help="Phone")
parser.add_argument("content", type=str, location="json", help="Content")
parser.add_argument("speed", type=int, location="json", help="Speed")
parser.add_argument("accuracy", type=int, location="json", help="Accuracy")


class Feedback(Document):
    name = StringField()
    phone = StringField()
    content = StringField()
    speed = IntField()
    accuracy = IntField()

class FeedbackListRes(Resource):
    def get(self):
        return mlab.list2json(Feedback.objects)

    def post(self):
        args = parser.parse_args()

        name = args["name"]
        phone = args["phone"]
        content = args["content"]
        speed = args["speed"]
        accuracy = args["accuracy"]

        feed_back = Feedback(name=name,
                                phone=phone,
                                content=content,
                                speed=speed,
                                accuracy=accuracy)
        feed_back.save()

        return mlab.item2json(Feedback.objects().with_id(feed_back.id))

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

api.add_resource(FeedbackListRes, "/api/feedback")


if __name__ == '__main__':
    app.run(port=2612)