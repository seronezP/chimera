import customtkinter
from customtkinter import CTkFrame, CTkScrollbar, CTkScrollableFrame


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

        # just a label
        label = customtkinter.CTkLabel(
            self,
            text="Enter your path to minecrfat directory: ",
        )
        label.place(relx=0.30, rely=0.23, anchor="center")


        # user enter path to minecraft directory
        path_minecraft = customtkinter.CTkEntry(
            self,
            placeholder_text="Your path",
            width=300,
            height=30
        )
        path_minecraft.place(x=180, y=100, anchor="center")


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