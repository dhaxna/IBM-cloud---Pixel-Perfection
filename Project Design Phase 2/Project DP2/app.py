from flask import Flask, request
import yaml
import os

app = Flask(__name__)

# Load the configuration from the YAML file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    image_file = request.files['image']
    if image_file.filename == '':
        return 'No selected file', 400

    save_path = os.path.join(config['storage']['path'], image_file.filename)
    image_file.save(save_path)

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
