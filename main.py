from GUI import *
from functions import *
import threading

while True:
    winEvents, values = window.read()

    if sg.WIN_CLOSED == winEvents: quit("Exiting")

    dropdown_choice = str(values["__CHOICE__"]).strip()

    # updates the image depending on the value of the dropdown element
    window["__KEY_REPRESENTATION__"].update(f"Images/{dropdown_choice}.png")

    if winEvents == "__TOGGLE_TYPING__":     # if the "Start" button is clicked
        threading.Thread(target=replace_letter, args=(dropdown_choice, values["__EXCEPTION__"], window),
                         daemon=True).start()
        window["__STATUS__"].update("Status: Started")

    if winEvents == "__STOP__":
        thread_comms.put("Stop")            # sending "Stop" to the thread above if the button "Stop" is clicked
        window["__STATUS__"].update("Status: Stopped")
