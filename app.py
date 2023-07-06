from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Instagram verification challenge
        verify_token = '<your_verify_token>'
        hub_challenge = request.args.get('hub.challenge')
        hub_verify_token = request.args.get('hub.verify_token')
        
        if hub_verify_token == verify_token:
            return hub_challenge
        else:
            return 'Invalid verification token', 403
    elif request.method == 'POST':
        # Handle webhook events from Instagram
        data = request.json
        print(data)  # Process the data as per your requirements
        
        return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
