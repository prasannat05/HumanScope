# HumanScope

A real-time human detection application powered by YOLOv11 object detection.

## Features

- 🎥 **Live Webcam Detection** - Real-time person detection from your webcam stream
- 📁 **Video Upload** - Upload video files for human detection and analysis
- ⚡ **YOLOv11 Model** - State-of-the-art object detection using YOLOv11n
- 🌐 **Web Interface** - Easy-to-use Flask-based web application

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Computer Vision**: OpenCV, Ultralytics YOLO
- **Frontend**: HTML/CSS
- **Detection Model**: YOLOv11n pre-trained weights

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prasannat05/HumanScope.git
cd HumanScope
```

2. Install dependencies:
```bash
pip install flask opencv-python ultralytics
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Choose between:
   - **Webcam Feed** - Real-time detection from your webcam
   - **Upload Video** - Upload a video file for detection

## How It Works

- The application uses YOLOv11n model to detect persons in video streams
- Detections are visualized with bounding boxes in real-time
- Video frames are streamed to the web interface via HTTP
- Confidence threshold: 0.5 (detects persons with 50%+ confidence)

## Project Structure

```
├── app.py                 # Main Flask application
├── yolo11n.pt            # Pre-trained YOLOv11n model weights
├── templates/            # HTML templates
├── uploads/              # User uploaded video files
└── SampleImages/         # Sample images/media
```

## License

This project is open source and available on GitHub.
