import customtkinter
from customtkinter import CTkFrame
from src.gui.SettingsGUI import SettingsGUI

class App:
    def __init__(self, launch_callback):
        self.app = customtkinter.CTk()
        self.app.title("Chimera Launcher")
        self.app.geometry("600x340")
        self.app.resizable(False, False)

        # main frame of application
        self.main_frame = CTkFrame(master=self.app, width=500, height=300)
        self.main_frame.place(x=130, y=50)

        # field for user enter
        self.entry_1 = customtkinter.CTkEntry(
            self.main_frame,
            placeholder_text="Enter Your Name",
            width=120,
            height=30
        )
        self.entry_1.place(x=180, y=170)

        # version select
        self.combobox_var = customtkinter.StringVar(value="Select Version")
        self.combobox = customtkinter.CTkComboBox(
            self.main_frame,
            width=120,
            height=30,
            variable=self.combobox_var
        )
        self.combobox.place(x=180, y=210)

        # start button
        button_1 = customtkinter.CTkButton(
            self.main_frame,
            text="Launch",
            fg_color="#1a1a1a",
            width=120,
            height=30,
            command=launch_callback
        )
        button_1.place(x=180, y=250)

        # settings button in main frame
        self.settings_button = customtkinter.CTkButton(
            self.app,
            text="Settings",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=self.show_settings
        )
        self.settings_button.place(x=15, y=300)

        # creating settings frame (default: hide)
        self.settings_gui = SettingsGUI(self.app, self.hide_settings)
        self.settings_gui.place_forget()

    # show settings frame func
    def show_settings(self):
        self.settings_gui.place(x=380, y=200, anchor="center")

    # hide settings frame func
    def hide_settings(self):
        self.settings_gui.place_forget()

    # set versions in combobox
    def set_version_options(self, versions):
        self.combobox.configure(values=versions)

    # get select version
    def get_selected_version(self):
        return self.combobox_var.get()

    # get username
    def get_username(self):
        return self.entry_1.get().strip()

    # sart app
    def run(self):
        self.app.mainloop()