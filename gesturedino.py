import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe and camera
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

# Function to detect pinch gesture
def is_pinch(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    # Calculate distance between thumb and index fingertip
    pinch_distance = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)
    return pinch_distance < 0.05  # Adjust sensitivity threshold

# Main loop
print("Press 'q' to quit the game.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read from webcam.")
        break

    frame = cv2.flip(frame, 1)  # Flip frame horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check for pinch gesture
            if is_pinch(hand_landmarks):
                pyautogui.press("space")  # Simulate spacebar press for jump
                cv2.putText(frame, "Jump!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the instructions and video feed
    cv2.putText(frame, "Pinch to Jump", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Gesture Controlled Dino Game", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
