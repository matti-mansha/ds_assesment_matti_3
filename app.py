import subprocess
from flask import Flask, request
from PIL import Image

app = Flask(__name__)

@app.route('/detect_memory', methods=['POST'])
def detect_memory():
    # Load the input image from the request
    image_file = request.files['image']
    image = Image.open(image_file)

    # Save the input image to a temporary file
    input_image_file = 'input_image.png'
    image.save(input_image_file)

    # Execute the detect.py command using subprocess
    command = "python detect.py --weights runs/train/exp3/weights/last.pt --img 640 --conf 0.25 --source {}".format(input_image_file)
    subprocess.run(command, shell=True)

    # Load the resulting image with bounding boxes
    processed_image_file = 'runs/train/exp3/val_batch0_pred.jpg'
    processed_image = Image.open(processed_image_file)

    # Convert the resulting image to a byte stream for Flask response
    processed_image_byte_stream = processed_image.tobytes()
    
    return processed_image_byte_stream, 200, {'Content-Type': 'image/jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
