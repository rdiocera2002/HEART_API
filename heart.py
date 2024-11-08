from flask import Flask, jsonify, request

app = Flask(__name__)

heart = [
    {
        "heart_id" : "2",
        "heart_date" : "November 9, 2024",
        "heart_rate" : "70"
    }
]

@app.route('/heart', methods=['GET'])
def getHeartInfo():
    return jsonify(heart)

@app.route('/heart', methods=['POST'])
def insertHeartID():
    hearts = request.get_json()
    heart.append(heart)
    return {'Successful, id': len(heart)}, 200

@app.route('/heart/<int:index>', methods=['PUT'])
def updateHeartInfo(index):
    hearts = request .get_json()
    heart[index] = heart
    return jsonify(heart[index]), 200

@app.route('/heart/<int:index>', methods=['DELETE'])
def deleteHeart(index):
    heart.pop(index)
    return "The heart id has been deleted successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
    
