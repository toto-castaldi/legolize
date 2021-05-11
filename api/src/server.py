from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
#app.secret_key = b"\x04\x15'bc\xf1\xfamO\xd6L\x87\x98\xb6\xc9^"
CORS(app)

@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>', methods=['POST', 'GET', 'DELETE'])
def main_entry_point(path):
    method = request.method
    request_query = request.args.copy()
    request_body = request.json if request.json else {}
 
    print(method)
    print(request_body)
    print(request_query)

    return make_response({}, 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)