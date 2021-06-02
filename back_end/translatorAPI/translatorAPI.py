from flask import Flask, jsonify, request
from flask_cors import CORS
from requester_broker import requester_broker

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/Login', methods=['GET'], strict_slashes=False)
def get_Login():
    user_ = request.headers["user"]
    pass_ = request.headers["password"]
    req = requester_broker(host='192.168.48.2')
    response_ = req.get_login(user_, pass_)
    req.connection.close()
    return jsonify(response_)

@app.route('/Books', methods=['GET'], strict_slashes=False)
def get_DocumentName():
    if((request.headers["user"]) == "gaby"):
        books = [{"name": "LOR"},{"name": "LOR2"},{"name": "LOR3"}]
        response = jsonify(books)
        return response

@app.route('/Workers', methods=['GET'], strict_slashes=False)
def get_Workers():
    requestDocument = request.headers["documentName"]
    if (requestDocument != ""):
        if (requestDocument == "LOR"):
            workers = [{"name": "gaby", "lastName": "avila"}]
            response = jsonify(workers)
            return response
        elif (requestDocument == "LOR2"):
            workers = [{"name": "isaac", "lastName": "ramirez"}]
            response = jsonify(workers)
            return response
        elif (requestDocument == "LOR3"):
            workers = [{"name": "andrey", "lastName": "garro"}]
            response = jsonify(workers)
            return response
    else:
        response = jsonify({"name": ""}) 
        return response   

@app.route('/Progress', methods=['GET'], strict_slashes=False)
def get_Progress():
    if((request.headers["user"]) == "gaby"):
        progress = [{"document":"LOR", "progress": "100", "documentFeel": "Hapyy", "ofensiveContent": "No"},
        {"document":"LOR2", "progress": "50", "documentFeel": "Angry", "ofensiveContent": "Si"},
        {"document":"LOR3", "progress": "10", "documentFeel": "Ofensive", "ofensiveContent": "Si"}]
        response = jsonify(progress)
        return response
    

#Se ejecuta el api
if __name__ == '__main__':
    app.run(port=4000, host='0.0.0.0')