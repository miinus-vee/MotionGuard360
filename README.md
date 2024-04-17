# MotionGuard360: Enhanced Object Detection

MotionGuard360 is a Python-based application designed to detect and highlight motion in video feeds. Utilizing computer vision techniques, this application can identify areas of movement within video streams and outline them in real-time. It's perfect for security purposes, monitoring areas where unexpected motion needs to be tracked and recorded.

## Features
- Video Feed Support: Utilize any MP4 video file or connect directly to a webcam.
- Real-Time Detection: Identify and highlight movements live as they happen.
- Easy-to-Use Interface: Start, stop, and open video functionality through a simple graphical interface.

## Installation
### Prerequisites
Before running MotionGuard360, ensure you have the following installed:
- Python 3.6 or higher
- OpenCV
- PIL (Pillow)
- tkinter for the GUI

### Install Dependencies
To install the required Python libraries, you can use the following pip commands:

`pip install opencv-python`

`pip install pillow`

`pip install tk`


### Running the Application

`git clone https://your-repository-url.git](https://github.com/miinus-vee/MotionGuard360.git`

`cd MotionGuard360`

### Run the application:

`python main.py`

## Usage
- Start the Application: Execute the script to launch the user interface.
- Open a Video: Click on the "Open Video" button to select a video file, or the application will default to your *webcam feed* if no file is selected.
- Start Detection: Click the "Start" button to begin motion detection. Detected motions will be highlighted in the video feed displayed.
- Stop Detection: Press the "Stop" button to end the detection. You can restart or open a new video file afterward.

## How It Works
MotionGuard360 processes video frames in real-time to detect differences between consecutive frames. When differences (i.e., motions) are detected, the affected areas are highlighted. The application uses OpenCV for video processing and tkinter for the GUI.
