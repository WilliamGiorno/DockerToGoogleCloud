import subprocess
import os
from datetime import datetime

def run_command(command):
    """Execute a system command."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f'Error: {stderr.decode()}')
    else:
        print(f'Result: {stdout.decode()}')

# Your variables
project_id = 'your-project-id'
region = 'your-region'
dockerfile_path = '/path/to/your/Dockerfile'

# Generate a unique name for the Docker image using a timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
image_name = f'your-image-name-{timestamp}'

# Log into Google Cloud
run_command('gcloud auth login')

# Configure the project and region
run_command(f'gcloud config set project {project_id}')
run_command(f'gcloud config set run/region {region}')

# Build and push the Docker image
os.chdir(dockerfile_path)
run_command(f'docker build -t gcr.io/{project_id}/{image_name} .')
run_command(f'docker push gcr.io/{project_id}/{image_name}')

# Deploy to Google Cloud Run
run_command(f'gcloud run deploy --image gcr.io/{project_id}/{image_name} --platform managed')
