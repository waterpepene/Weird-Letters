import PySimpleGUI as sg

sg.theme("DarkBlue16")
sg.theme_border_width(0)

window_layout = [[sg.Text("Welcome!\nPress the button to start replacing your letters."
                          "\nOnce Started, press ESC to stop.",
                          font=("dubai", 18), justification="center")],

                 [sg.Button("Start", font=("dubai", 14), size=(7, 1), key="-TOGGLE_TYPING-")],

                 [sg.Text("Letter(s) Exception: ", font=("dubai", 16), justification="center"),
                  sg.InputText("v", font=("dubai", 18), justification="center", size=(8, 1), key="-EXCEPTION-",
                               enable_events=True, tooltip="Letters written in here will be typed as they are.")]]


window = sg.Window("Weird Letters", window_layout, element_justification="center")

