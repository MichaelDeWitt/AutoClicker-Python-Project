import pyautogui
import keyboard
import threading
import time

# -----------------------------
# Settings
# -----------------------------
CLICKS_PER_SECOND = 20      # Change this to your desired speed
BUTTON = "left"             # "left", "right", or "middle"

START_STOP_KEY = "f6"
EXIT_KEY = "esc"

# -----------------------------
# PyAutoGUI Safety
# -----------------------------
# Moving the mouse to the top-left corner will stop the program.
pyautogui.FAILSAFE = True

clicking = False
running = True


def click_loop():
    global clicking, running

    delay = 1 / CLICKS_PER_SECOND

    while running:
        if clicking:
            try:
                pyautogui.click(button=BUTTON)
            except pyautogui.FailSafeException:
                print("\nFAILSAFE ACTIVATED!")
                print("Mouse moved to the top-left corner.")
                print("Stopping autoclicker...")
                clicking = False

            time.sleep(delay)
        else:
            time.sleep(0.05)


# Start clicking thread
thread = threading.Thread(target=click_loop, daemon=True)
thread.start()

print("=" * 40)
print("Python AutoClicker")
print("=" * 40)
print(f"Start/Stop : {START_STOP_KEY.upper()}")
print(f"Exit       : {EXIT_KEY.upper()}")
print(f"Button     : {BUTTON}")
print(f"Speed      : {CLICKS_PER_SECOND} CPS")
print("=" * 40)

try:
    while running:

        if keyboard.is_pressed(START_STOP_KEY):
            clicking = not clicking

            if clicking:
                print("AutoClicker: ON")
            else:
                print("AutoClicker: OFF")

            time.sleep(0.3)  # Prevent multiple toggles

        if keyboard.is_pressed(EXIT_KEY):
            running = False
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    running = False

print("Program closed.")