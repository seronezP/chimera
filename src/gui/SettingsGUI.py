import customtkinter
from customtkinter import CTkFrame


class SettingsGUI(CTkFrame):
    def __init__(self, parent, close_callback, width=500, height=300):
        super().__init__(parent, width=width, height=height)
        self.close_callback = close_callback

        # label settings
        label = customtkinter.CTkLabel(
            self,
            text="Settings",
        )
        label.place(relx=0.09, rely=0.09, anchor="center")

        # close settings button
        button_ok = customtkinter.CTkButton(
            self,
            text="OK",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=self.close_settings
        )
        button_ok.place(x=400, y=265, anchor="center")

    # func close settings
    def close_settings(self):
        self.close_callback()