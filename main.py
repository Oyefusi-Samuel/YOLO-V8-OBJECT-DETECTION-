import cv2
from ultralytics import YOLO # type: ignore

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt, yolov8m.pt etc. for better accuracy

# Open webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Run real-time object detection
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Visualize results on frame
    annotated_frame = results[0].plot()

    # Display the output
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and close
cap.release()
cv2.destroyAllWindows()