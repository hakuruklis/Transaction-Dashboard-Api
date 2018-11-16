from pymongo import MongoClient
from bson.json_util import dumps
import pymongo
import json
import pprint


from flask import Flask, jsonify


app = Flask(__name__)



client = pymongo.MongoClient("mongodb+srv://atlasadmin:atlasadmin@transacciones-v8fmm.mongodb.net/test?retryWrites=true")
db = client["Transacciones"]

collection = db["Transacciones"]
response = {}

# @app.route("/api/v1/", methods=['POST','GET'])
# def usuarios():
#     response = {}
#     data = dumps(collection.find_one())
#     response["data"] = data
#     print()
#     return jsonify(response)


# @app.route("/api/v1/<int:usuario>", methods=['POST','GET'])
# def buscarUsuario(usuario):
#     response = {}
#     #data = db.client.find_one({"id_tran":usuario})
#     try:
#         data = dumps(collection.find({"id_tran":usuario}))
#         if data:
#             response["data"] = data
#             pprint.pprint(data)
#         else:
#             response["mensaje"] = "El usuario no existe"
#         return jsonify(response)
#     except:
#         return "Tu internet ta en tuco"



if __name__ == '__main__':
    # app.run(debug=True)


    data = dumps(collection.find_one())
    response["data"] = data
    print(response["data"])