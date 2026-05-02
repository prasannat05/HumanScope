import cv2
from flask import Flask, render_template, Response, request
from ultralytics import YOLO
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = YOLO("yolo11n.pt")

def generate_frames(source=0):
    cap = cv2.VideoCapture(source)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Run YOLO detection (Person class only)
            results = model.predict(source=frame, classes=[0], conf=0.5, verbose=False)
            annotated_frame = results[0].plot()

            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = buffer.tobytes()

            # Yield the output frame in the byte format required for HTTP streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Default to webcam
    return Response(generate_frames(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload_feed', methods=['POST'])
def upload_feed():
    if 'file' not in request.files:
        return "No file uploaded"
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Stream the uploaded file
    return Response(generate_frames(filepath), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, port=5000)