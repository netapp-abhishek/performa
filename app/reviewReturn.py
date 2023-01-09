import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html><head><title>Performa</title></head><body><h1>Spot Automation API Simple Application</h1></body></html>"

@app.route('/checkMyDetails', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    with open(r'./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record["name"] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})    


@app.route('/enterMyDetails', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    with open(r'./tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open(r'./tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)   


@app.route("/updateMyDetails",methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open(r'./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)  
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open(r'./tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/removeMyDetails', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open(r'./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open(r'./tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)



if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)