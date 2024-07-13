from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def webhook():
    data = request.json
    user_id = data['message']['from']['id']
    first_name = data['message']['from']['first_name']
    return jsonify({"user_id": user_id, "first_name": first_name})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
