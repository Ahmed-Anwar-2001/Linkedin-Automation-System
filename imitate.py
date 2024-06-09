import keyboard
from pynput.mouse import Listener, Controller
from pynput import mouse
from time import sleep
from queue import Queue
from threading import Thread
import pyautogui
import time
q = Queue()
# Function to add mouse events to a queue
def on_move(x, y):
    q.put('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    q.put('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    q.put('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll)
listener.start()

# Start recording keyboard events
keyboard.start_recording(recorded_events_queue=q)

time.sleep(5)

# Stop recording keyboard events
keyboard.stop_recording()

# Stop listening to mouse events
listener.stop()

# Get all events from the queue
interactions = list(q.queue)

print(interactions)
