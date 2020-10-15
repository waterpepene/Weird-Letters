import queue
from pynput.keyboard import Events, Key, Controller, Listener
from random import choice
from json import load

thread_comms = queue.Queue()
kb = Controller()


class KeyboardEvents(Events):
    _Listener = Listener

    class Press(Events.Event):              # key press event
        def __init__(self, key):
            self.key = str(key).strip("'")  # converting the key pressed to string and removing the ''

    def __init__(self):                     # returning the key pressed
        super(Events, self).__init__(on_press=self.Press)


def replace_letter(mode, exception, window_name):
    with KeyboardEvents() as events, open("replace letters.json", "r", encoding="utf8") as replace_json:
        replace_dict = load(replace_json)[mode]     # load a json object with the parameter mode, which is received from
                                                    # the dropdown selected value
        for event in events:
            try:
                message = thread_comms.get_nowait()     # this will receive the messages sent from the GUI
                if message == "Stop":
                    break                               # break out of the loop if "Stop" is received from the GUI

            except queue.Empty:                         # get_nowait() will get exception when Queue is empty
                message = None

            if event.key in exception:                  # continue if the user-written key is in the exception input box
                continue

            if event.key in replace_dict:
                kb.press(Key.backspace)                     # deleted the user-written key
                kb.press(choice(replace_dict[event.key]))   # replaces the key with another

            if event.key == "Key.esc":
                window_name["__STATUS__"].update("Status: Stopped")
                break       # stop listening if ESC is pressed and update the GUI status to "Stopped"
