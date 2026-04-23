from flask import Flask, Response
import cv2, threading

app = Flask(__name__)
camera = Camera()
lock = threading.Lock()
latest_frame = None

def capture_loop():
    global latest_frame
    while True:
        frame = camera.read()
        if frame is not None:
            with lock:
                latest_frame = frame.copy()

def generate():
    while True:
        with lock:
            if latest_frame is None:
                continue
            _, jpeg = cv2.imencode('.jpg', latest_frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' +
               jpeg.tobytes() + b'\r\n')

@app.route('/video')
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=capture_loop, daemon=True)
    t.start()
    app.run(host='0.0.0.0', port=5000)