# System Information Dashboard

A Docker-containerized Flask web application that displays real-time system information including CPU usage, memory utilization, and disk space.

## Features

- Real-time system metrics monitoring
- Clean, modern web interface
- Visual progress bars for usage statistics
- Cross-platform compatibility
- Docker containerization

## Prerequisites

- Docker installed on your system
- Git (for cloning the repository)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/emooney/docker_learn_1.git
cd docker_learn_1
```

2. Build the Docker image:
```bash
docker build -t system-info-app .
```

3. Run the container:
```bash
docker run -p 5000:5000 --name system-info system-info-app
```

4. Access the dashboard:
Open your web browser and navigate to `http://localhost:5000`

## Project Structure

```
docker_learn_1/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── templates/
    └── index.html     # Web interface template
```

## Running on Raspberry Pi

This application is compatible with Raspberry Pi (ARM architecture). To deploy:

1. SSH into your Raspberry Pi:
```bash
ssh username@raspberry-pi-ip
```

2. Clone the repository and build:
```bash
git clone https://github.com/emooney/docker_learn_1.git
cd docker_learn_1
docker build -t system-info-app .
docker run -p 5000:5000 --name system-info system-info-app
```

## Technologies Used

- Python 3.11
- Flask (Web Framework)
- psutil (System Information)
- Docker
- HTML/CSS

## Notes

- The system information displayed reflects the container's environment, not the host system
- The application runs on port 5000 by default

## License

This project is open source and available under the MIT License.
