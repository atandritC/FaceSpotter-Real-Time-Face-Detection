# FaceSpotter - Real-Time Face Detection

## Real-Time Face Detection using OpenCV and dlib

Welcome to FaceSpotter, a Streamlit web application for real-time face detection using OpenCV and dlib. This application allows users to start and stop face detection on live video streams from their camera.

## What This Project Does

FaceSpotter utilizes computer vision techniques to detect human faces in real-time video streams. It draws bounding boxes around detected faces and labels them sequentially. Users can control the face detection with a simple start/stop toggle button.

## Demonstration

![FaceSpotter Demo](https://github.com/atandritC/Demo-GIFs-Pictures/blob/main/FaceSpotter.gif)

## Installation and Usage Instructions 

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/FaceSpotter-Real-Time-Face-Detection.git
    cd FaceSpotter-Real-Time-Face-Detection
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Follow the on-screen instructions to start and stop face detection.

### File Structure

- `app.py`: Main Streamlit application script.
- `main.py`: Contains the face detection logic using OpenCV and dlib.
- `requirements.txt`: List of Python dependencies required for the project.

## Contributing

Contributions are welcome! If you'd like to contribute to FaceSpotter, please follow these steps:

1. Fork the repository and create your branch (`git checkout -b feature/AmazingFeature`).
2. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
3. Push to the branch (`git push origin feature/AmazingFeature`).
4. Open a pull request.

Please ensure your code follows the existing style and includes necessary tests.

Thank you for using FaceSpotter! Detect faces in real-time effortlessly.
