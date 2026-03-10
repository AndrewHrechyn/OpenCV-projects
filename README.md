# OpenCV-projects

# OpenCV-projects

A collection of computer vision projects built with OpenCV and MediaPipe, demonstrating real-time hand gesture recognition and facial analysis applications.

## Projects

### 1. Brightness Control with Hands
**Location:** `projects/brightness_control_with_hands/`

Control your screen brightness using hand gestures in real-time. This project uses MediaPipe to detect hand landmarks and calculates the distance between thumb and index finger to adjust system brightness.

**Features:**
- Real-time hand detection and tracking
- Distance-based brightness adjustment (0-100%)
- Visual feedback with hand landmarks and distance line
- Supports both MediaPipe import methods (fallback handling)
- Single hand mode with high confidence thresholds

**Requirements:**
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- Screen brightness control library (`screen_brightness_control`)
- NumPy

**How to Use:**
1. Run the script to start the webcam feed
2. Hold up one hand and pinch your thumb and index finger
3. Move your fingers apart to increase brightness, closer together to decrease
4. Press 'q' to quit the application

---

### 2. Real-time Face Mesh Detection
**Location:** `projects/realtime_face_mesh_detection/`

Detect and visualize facial landmarks in real-time using MediaPipe's Face Mesh solution. This project creates a 3D face mesh overlay on detected faces with tessellation connections.

**Features:**
- Real-time face detection and mesh generation
- 3D face mesh visualization with tessellation
- Smooth face tracking with single face mode
- Frame mirroring for intuitive interaction
- Automatic camera frame validation

**Requirements:**
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

**How to Use:**
1. Run the script to start the webcam feed
2. Position your face in front of the camera
3. The face mesh will automatically detect and overlay on your face
4. Press 'q' to quit the application

---

## General Requirements

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install opencv-python mediapipe screen-brightness-control
```

## Technical Stack

- **Python 3.11.9+**
- **OpenCV 4.13.0** - Computer vision processing
- **MediaPipe** - Hand and face landmark detection
- **NumPy** - Numerical computations

## Project Structure

```
OpenCV-projects/
├── projects/
│   ├── brightness_control_with_hands/
│   │   └── main.py
│   └── realtime_face_mesh_detection/
│       └── main.py
├── .gitignore
├── main.ipynb              # Jupyter notebook for experimentation
└── README.md
```

## Notes

- All projects use real-time video capture from your default webcam (index 0)
- Projects are designed to be modular and can be extended with additional features
- Error handling is implemented for common issues (e.g., brightness control failures on unsupported systems)

## License

Feel free to use these projects for learning and development purposes.
