import PySimpleGUI as sg

sg.theme("DarkBlue16")
sg.theme_border_width(0)

centered_titles = [x.center(26) for x in ["Random", "Small letters", "Inverted", "Full Width", "Circled Letters"]]

window_layout = [[sg.Text("Welcome!\nPress the button to start replacing your letters.",
                          font=("dubai", 18), justification="center")],

                 [sg.Combo(centered_titles, size=(16, 1), enable_events=True, font=("dubai", 14),
                           readonly=True, key="__CHOICE__", default_value=centered_titles[0])],

                 [sg.Image(r"Images/random.png", key="__KEY_REPRESENTATION__")],

                 [sg.Text("Letter(s) Exception: ", font=("dubai", 16), justification="center"),
                  sg.InputText("a", font=("dubai", 18), justification="center", size=(8, 1), key="__EXCEPTION__",
                               enable_events=True, tooltip="Letters that are in here will be written normally.")],


                 [sg.Text("Status: Stopped", font=("dubai", 14), justification="center", key="__STATUS__")],

                 [sg.Button("Start", font=("dubai", 14), size=(7, 1), key="__TOGGLE_TYPING__"),
                  sg.Button("Stop", font=("dubai", 14), size=(7, 1), key="__STOP__")],
                 ]


window = sg.Window("Weird Letters", window_layout, element_justification="center")

