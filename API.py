from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {"value": "No Data Yet"}

@app.route('/data', methods=['GET'])
def receive_data():
    global latest_data
    data = request.args.get('value')
    if data:
        latest_data = {"value": data}
        print(f"Received: {data}")
    return "Data Received"

@app.route('/fetch', methods=['GET'])
def fetch_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run()  # Ensure it's accessible on the network
