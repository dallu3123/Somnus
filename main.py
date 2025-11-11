import camera
import time
import requests
from picamera2 import Picamera2
from datetime import datetime
import io

SERVER_URL = "http://your-server-url:5000/upload"

picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()

def capture_and_send():
    try:
        datetime_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        stream = io.BytesIO()
        picam2.capture_to_file(stream, format="jpeg")
        stream.seek(0)
        files = {
            'image': (f'sleep_{datetime_now}.jpg', stream, 'image/jpeg')
        }

    except Exception as e:
        print(f"Error: {e}")
    finally:
        picam2.stop()

print("수면 모니터링 시작")

while True:
    capture_and_send()
    time.sleep(60)

