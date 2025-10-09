import customtkinter
from customtkinter import CTkFrame
import subprocess

new_mode = "Light"


class SettingsGUI(CTkFrame):
    def __init__(self, parent, close_callback, current_path, width=500, height=300):
        self.input_mode = None
        super().__init__(parent, width=width, height=height)
        self.close_callback = close_callback

        # label settings
        label_1 = customtkinter.CTkLabel(
            self,
            text="Settings",
        )
        label_1.place(relx=0.09, rely=0.07, anchor="center")

        # just a label
        label_2 = customtkinter.CTkLabel(
            self,
            text="Enter your path to minecrfat directory: ",
        )
        label_2.place(relx=0.30, rely=0.23, anchor="center")

        # Select theme
        self.combobox_pityh = customtkinter.StringVar(value="Theme")
        self.combobox = customtkinter.CTkComboBox(
            self,
            width=120,
            height=30,
            variable=self.combobox_pityh,
            values=["Dark Theme", "Light Theme"],
        )
        self.combobox.place(x=30, y=160)

        # just another label
        label_3 = customtkinter.CTkLabel(
            self,
            text="Select Your Theme",
        )
        label_3.place(x=90, y=140, anchor="center")

        # user enter path to minecraft directory
        self.path_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Your path",
            width=300,
            height=30,
        )
        self.path_entry.place(x=180, y=100, anchor="center")
        # Insert current path
        self.path_entry.insert(0, current_path)

        # close settings button
        button_ok = customtkinter.CTkButton(
            self,
            text="OK",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=self.close_settings,
        )
        button_ok.place(x=400, y=265, anchor="center")

        # close settings button
        button_open_folder = customtkinter.CTkButton(
            self,
            text="Open Folder",
            fg_color="#1a1a1a",
            width=100,
            height=30,
            command=self.open_folder,
        )
        button_open_folder.place(x=390, y=100, anchor="center")

        # close settings button
        button_theme_enter = customtkinter.CTkButton(
            self,
            text="Apply",
            fg_color="#1a1a1a",
            width=80,
            height=30,
            command=self.change_theme,
        )
        button_theme_enter.place(x=200, y=175, anchor="center")

    def get_minecraft_path(self):
        """Get entered Minecraft path"""
        return self.path_entry.get().strip()

    # func close settings
    def close_settings(self):
        self.close_callback()

    # open folder .minecraft
    def open_folder(self):
        try:
            subprocess.run(["open", self.get_minecraft_path()], check=True)
        except subprocess.CalledProcessError as e:
            print(f"error with open folder: {e}")

    def change_theme(self):
        self.input_mode = self.combobox_pityh.get()
        # turn theme
        if self.input_mode == "Light Theme":
            new_mode = "Light"
        else:
            new_mode = "Dark"
        customtkinter.set_appearance_mode(new_mode)
        customtkinter.set_default_color_theme("blue")
        # update theme
        self.update_idletasks()
