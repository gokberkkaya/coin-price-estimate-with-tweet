from flask import Flask, request, jsonify
from app.model import predict_tweet_effect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def validate_request(data):
    if 'tweet' not in data or 'tweet_owner' not in data:
        return False
    if not isinstance(data['tweet'], str) or not isinstance(data['tweet_owner'], str):
        return False
    return True

@app.route('/api/get-tweet-estimate', methods=['POST'])
def get_tweet_estimate():
    data = request.get_json()
    
    if not validate_request(data):
        return jsonify({'error': 'Invalid request format'}), 400
    
    tweet = data['tweet']
    tweet_owner = data['tweet_owner']
    prediction = predict_tweet_effect(tweet, tweet_owner)
    
    return jsonify({'estimate': bool(prediction)}), 200

if __name__ == '__main__':
    app.run(debug=True)
