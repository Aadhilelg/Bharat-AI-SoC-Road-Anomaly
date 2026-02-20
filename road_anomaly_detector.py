import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import RPi.GPIO as GPIO
import threading

# Bharat AI-SoC Pin Mapping (Physical Pins 12 & 18)
BUZZER_PIN, LED_PIN = 18, 24
GPIO.setmode(GPIO.BCM)
GPIO.setup([BUZZER_PIN, LED_PIN], GPIO.OUT)

def alert():
    GPIO.output([BUZZER_PIN, LED_PIN], GPIO.HIGH)
    import time; time.sleep(0.5)
    GPIO.output([BUZZER_PIN, LED_PIN], GPIO.LOW)

interpreter = tflite.Interpreter(model_path="pothole_detector.tflite")
interpreter.allocate_tensors()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    img = cv2.resize(frame, (224, 224))
    input_data = np.expand_dims(img, axis=0).astype(np.float32)
    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_data)
    interpreter.invoke()
    if interpreter.get_tensor(interpreter.get_output_details()[0]['index'])[0][0] > 0.5:
        threading.Thread(target=alert).start()
