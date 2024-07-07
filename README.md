# Webhook Project

This project sets up a webhook server using Flask and runs it as a systemd service.

## Prerequisites

- Python 3
- Ubuntu 2x 
- `systemd` (for running the service)

## Setup Instructions

### 1. Clone the Repository


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
