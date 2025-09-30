# YOLOv8 Real-Time Object Detection 

This project demonstrates real-time object detection using Ultralytics YOLOv8 with a live webcam feed. It leverages OpenCV for video streaming and YOLOv8 for state-of-the-art object detection.

This project supports real-time detection using your webcam, YOLOv8 pre-trained models (n, s, m, etc.), and is lightweight and easy to extend for custom datasets.

## Installation

Clone this repository:
```bash
git clone https://github.com/Oyefusi-Samuel/YOLO-V8-OBJECT-DETECTION-.git
```
```
cd YOLO-V8-OBJECT-DETECTION-
```

Create and activate a virtual environment:
```bash
python -m venv venv
```
 # Windows
```
.env\Scripts/ctivate
```
# Mac/Linux
```
source venv/bin/activate  
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Python script to start real-time detection:
```bash
python main.py
```
Press `q` to exit the live window.

## Screenshot Example

*(Include an example screenshot of detection here if available)*

## Future Improvements

- Train YOLOv8 on a custom dataset for specific object detection tasks  
- Deploy model to edge devices (e.g., Raspberry Pi, Jetson Nano)  
- Add real-time alerts/notifications when detecting certain objects  
- Integrate with cloud services for remote monitoring and analytics  
- Improve GUI interface for non-technical users  

## License

This project is licensed under the MIT License.
