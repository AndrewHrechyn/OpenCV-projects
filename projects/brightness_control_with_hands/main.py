import cv2 as cv
import numpy as np
import screen_brightness_control as sbc
from math import hypot

try:
    from mediapipe.python.solutions import hands as mp_hands
    from mediapipe.python.solutions import drawing_utils as mp_draw

    print("Successfully connected via mediapipe.python.solutions")
except ImportError:
    import mediapipe.solutions.hands as mp_hands
    import mediapipe.solutions.drawing_utils as mp_draw

    print("Successfully connected via mediapipe.solutions")

hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

cap = cv.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv.flip(frame, 1)
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            points = {}
            for id, lm in enumerate(hand_landmarks.landmark):
                points[id] = (int(lm.x * w), int(lm.y * h))

            if 4 in points and 8 in points:
                x1, y1 = points[4]
                x2, y2 = points[8]

                cv.circle(frame, (x1, y1), 10, (255, 0, 0), cv.FILLED)
                cv.circle(frame, (x2, y2), 10, (255, 0, 0), cv.FILLED)
                cv.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

                distance = hypot(x2 - x1, y2 - y1)

                bright = np.interp(distance, [20, 200], [0, 100])

                try:
                    sbc.set_brightness(int(bright))
                except:
                    pass

                cv.putText(frame, f"Bright: {int(bright)}%", (10, 50),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow("Brightness Control", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
