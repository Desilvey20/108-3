from flask import Flask
from about_me import me
from mock_data import catalog 
import json

app = Flask('funguycollective')

@app.route("/", methods=['GET'])
def home():
    return "This is the home page"

#create an about endpoint and show your name
@app.route("/about")
def about():
    return me["first"] + " " + me["last"]

@app.route("/myaddress")
def address():
    return f'{me["address"]["street"]} {me["address"]["number"]}'





@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

#make an endpoint to send back how many products we have in the catalog
@app.route("/api/catalog/count", methods=["GET"])
def get_count():

    #here... count how many products are in the list catalog
    counts = len(catalog)

    return json.dumps(counts)#return the value


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    return json.dumps(id)


app.run(debug=True)