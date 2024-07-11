import logging
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='/home/turalp/webhook_project/logs/webhook_server.log')

UPLOAD_FOLDER = '/home/turalp/webhook_project/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/webhook', methods=['POST'])
def webhook():
    app.logger.debug('Webhook triggered')
    if 'file' not in request.files:
        app.logger.error('No file part in request')
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        app.logger.error('No selected file')
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    app.logger.debug(f'File saved to {file_path}')

    return jsonify({'message': 'File uploaded successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
