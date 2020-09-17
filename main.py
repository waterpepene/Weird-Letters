from GUI import *
from functions import *

while True:
    events, values = window.read()

    if sg.WIN_CLOSED == events: quit()

    if events == "-TOGGLE_TYPING-":     # if the "Start" button is clicked
        with KeyboardEvents() as events:
            for event in events:                                  # iterates over every keyboard event and replaces the
                replace_letter(event.key, values["-EXCEPTION-"])  # letter unless it's present in values["-EXCEPTION-"].

                if event.key == "Key.esc": break            # stop listening if ESC is pressed.
