import customtkinter
from customtkinter import CTkFrame

class App:
    def __init__(self, launch_callback, show_frame, hide_frame):
        self.app = customtkinter.CTk()
        self.app.title("Chimera Launcher")
        self.app.geometry("600x340")
        self.app.resizable(False, False)

        frame_1 = CTkFrame(master=self.app, width=500, height=300)
        frame_1.place(x=130, y=50)

        #create entry
        self.entry_1 = customtkinter.CTkEntry(
            self.app,
            placeholder_text="Enter Your Name",
            width=120,
            height=30
        )
        self.entry_1.place(x=300, y=220)

        # create combobox for select version
        self.combobox_var = customtkinter.StringVar(value="Select Version")
        self.combobox = customtkinter.CTkComboBox(
            self.app,
            width=120,
            height=30,
            variable=self.combobox_var
        )
        self.combobox.place(x=300, y=260)

        # create button for launch minecraft
        button_1 = customtkinter.CTkButton(
            self.app,
            text="Launch",
            fg_color="#1a1a1a",
            width=120,
            height=30,
            command=launch_callback
        )
        button_1.place(x=300, y=300)

        # create settings button for customization
        button_2 = customtkinter.CTkButton(
            self.app,
            text="Settings",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=show_frame
        )
        button_2.place(x=15, y=300)

        # create new settings frame
        self.settings_frame = customtkinter.CTkFrame(self.app, width=500, height=300)
        self.settings_frame.place(relx=0, rely=0, anchor="center")
        self.settings_frame.place_forget()  # Изначально скрываем Frame

        # create label settings
        label = customtkinter.CTkLabel(self.settings_frame, text="Settings")
        label.pack(padx=300, pady=100)
        label.place(relx=20, rely=20)

        # create button Ok for close(hide) settings frame
        button_3 = customtkinter.CTkButton(
            self.settings_frame,
            text="Ok",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=hide_frame
        )
        button_3.place(x=350, y=250)


    def set_version_options(self, versions):
        """install version to combobox"""
        self.combobox.configure(values=versions)

    def get_selected_version(self):
        """give select version"""
        return self.combobox_var.get()

    def get_username(self):
        """give username"""
        return self.entry_1.get().strip()

    def run(self):
        """start the app"""
        self.app.mainloop()