import time
from pynput import keyboard

# Variables
times = []
test_type = None
time_window = 1

# Function to calculate CPS
def calculate_cps():
    global time_window
    
    # Add current time of input to the times array
    times.append(time.time())

    # Remove timestamps in times older than the time_window
    for timestamp in times[:]:
        if time.time() - timestamp >= time_window:
            times.remove(timestamp)

    total_time = times[-1] - times[0]

    if len(times) >= 2:
        cps = len(times) / (total_time + (time_window - total_time) * (time_window - total_time / time_window))
    else:
        cps = 1
    
    return cps

# Function to handle key press events
def on_press(key):
    global test_type
    
    try:
        k = key.char
    except AttributeError:
        k = key.name
    
    cps = calculate_cps()
    
    if test_type == 1:
        cps = round(cps, 2)
        print("cps:", cps)
    elif test_type == 2:
        bpm = round(cps * 60 / 4, 2)
        print("bpm:", bpm)
    elif test_type == 3:
        wpm = round(cps * 60 / 5, 2)
        print("wpm:", wpm)

    if k == 'esc':
        print('Exiting...')
        return False

# Function to handle setup of test parameters
def test_setup():
    global test_type
    global time_window
    
    print("cps: 1, bpm: 2, wpm: 3")
    
    # Get test_type input
    while True:
        try:
            user_input = input("Select: ")
            if user_input == "":
                test_type = 1  # Default value if Enter is pressed
            else:
                test_type = int(user_input)
            
            if test_type in [1, 2, 3]:
                break  # Exit loop if valid selection
            else:
                print("Incorrect selection. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
    
    # Get time_window input
    print("Select a time window (in seconds)")
    while True:
        try:
            user_input = input("Select (default: 1): ")
            if user_input == "":
                time_window = 1  # Default value if Enter is pressed
            else:
                time_window = int(user_input)
            break  # Exit the loop once a valid input is received
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")

# Run test setup
test_setup()

# Set up the listener for key presses
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the program running to listen for key presses
listener.join()
