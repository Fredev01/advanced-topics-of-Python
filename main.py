from flask import Flask, request, json, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/api/*', origins="*")


@app.get('/api/get_model_to_render')
def get_model_to_render():
    return {"msg": "trying to better"}


@app.post('/api/execute_action_fixture')
def execute_action_ficture():
    data = request.json
    if data:
        print(data['typeComponent'])
        return jsonify({"msg": "Action executed"})
    return jsonify({"error": "no data recived"})


if __name__ == "__main__":
    app.run()