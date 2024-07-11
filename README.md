# Webhook Project

This project sets up a webhook server using Flask and runs it as a systemd service.

## Prerequisites

- Python 3
- Ubuntu 2x 
- `systemd` (for running the service)

### Directory Structre
```plaintext
webhook_project/
├── app/
│   ├── __init__.py
│   ├── webhook_server.py
├── venv/                # Virtual environment
├── requirements.txt     # Python dependencies
├── config/
│   ├── config.py        # Configuration files
├── logs/
│   ├── app.log          # Log files
└── uploads/             # Upload directory
```


## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/turalpashayev/webhook_project.git
cd webhook_project
```

### 2. Create and Activate a Virtual Environment
```
python3 -m venv venv  # To create a virtual environment
source venv/bin/activate  # To activate a virtual environment
```
### 3. Install Dependencies
```
pip install flask
```

### 4. Create `webhook_server.py`
Create a file named webhook_server.py in the app directory with the following content:
```
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
```

### 5. Create a `systemd` Service file
Create a `systemd` service file to run the Flask application as a service.
```
sudo vi /etc/systemd/system/webhook_server.service
```
Add the following content:
```
[Unit]
Description=Webhook Server

[Service]
ExecStart=/home/your-username/webhook_project/venv/bin/python /home/your-username/webhook_project/app/webhook_server.py
WorkingDirectory=/home/your-username/webhook_project
Restart=always
User=your-username
Environment="PATH=/home/your-username/webhook_project/venv/bin"

[Install]
WantedBy=multi-user.target
```

### 6. Reload `ssytemd` and Start the Service
```
sudo systemctl daemon-reload
sudo systemctl start webhook_server
sudo systemctl enable webhook_server
```

### 7. Check the Service Status
```
sudo systemctl status webhook_server
```
