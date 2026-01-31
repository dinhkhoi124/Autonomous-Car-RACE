# RACE: Autonomous Car Simulation with Computer Vision & PID Control
**RACE** is a comprehensive autonomous driving system designed for navigation within a simulated environment. The project integrates traditional computer vision techniques, deep learning models for sign recognition, and a PID controller to optimize vehicle trajectory.

## Key Features
- **Real-time Lane Detection:** Utilizes Bird’s-Eye View (Perspective) Transform and Image Thresholding to accurately determine the road center.

- **Traffic Sign Recognition (TSR)**: Features a pipeline integrating HSV color filtering and a CNN (LeNet) model to recognize navigational signs such as Turn Left, Turn Right, Straight, and Stop.

- **PID Control System**: Provides smooth steering control based on cross-track error, combined with a dynamic throttle mechanism that automatically adjusts speed during sharp turns.

- **High-Performance Multiprocessing**: Decouples the traffic sign recognition process from the main control loop using Python's multiprocessing to maintain a stable FPS and minimize system latency.

## System Architecture

Image data is transmitted from the simulator via Websockets and processed through two parallel pipelines:

**1. Perception Layer (Image Processing & AI)**
- **Lane Detection:** * Converts images to grayscale and applies thresholding to extract lane markings.

  - Applies a Perspective Transform (Bird’s-Eye View) to remove perspective distortion for more accurate distance calculation.
  
  - Identifies navigation points at two specific markers: LINEOFINTEREST_Y1 and LINEOFINTEREST_Y2.

- **Sign Detection**: * Uses HSV color filtering to localize potential traffic sign regions.
  - A LeNet model (in .onnx / .pth format) classifies the signs from the candidate regions.

**2. Control Layer**
- **PID Controller**: Calculates the steering_angle based on the deviation between the vehicle's center and the lane center.

- **Decision Logic**: Manages vehicle states (PID, WAITING, TURN_LEFT/RIGHT, STRAIGHT) based on the outputs from the Perception Layer.


## Project Structure
```
.
├── requirements.txt
├── run.py
├── configs/
│   └── config.py
│   └── map.py
├── models/
│   ├── traffic_sign_classifier.pth
│   └── traffic_sign_model.onnx
└── utils/
    ├── controller.py
    ├── lane_detector.py
    └── trafficsign_detector.py
```


- **requirements.txt:** Lists the Python dependencies for the project.
- **run.py:** The main entry point to start the application.
- **configs/:** Contains configuration files.
  - **config.py**
  - **map.py:**  Main configuration file for application settings, parameters, and model paths.
- **models/:** Stores the pre-trained machine learning models.
  - **traffic_sign_classifier.pth:** PyTorch model for traffic sign classification.
  - **traffic_sign_model.onnx:** ONNX model for cross-platform inference.
- **utils/:** Contains helper modules and utility functions.
  - **controller.py:** Manages vehicle control (steering, throttle).
  - **lane_detector.py:** Handles lane detection from image data.
  - **trafficsign_detector.py:** Detects and classifies traffic signs.

## Installation
```
git clone https://github.com/dinhkhoi124/Autonomous-Car-RACE.git
cd your-repository-name

pip install -r requirements.txt
```
⚠️ Recommended: Python ≥ 3.9

## Usage
- Launch the Simulator (RACE environment).
- Run the main script:
  ``` python run.py ```

## Author

Dinh Van Anh Khoi

🎓 AI Engineer (Final-year student)

💡 Interests: Computer Vision, Autonomous Driving, Robotics
