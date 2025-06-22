from src.gui.MainWindow import App
from launch_logic import Launcher
from random import choice


def main():
    launcher = Launcher()

# show settings frame
    def show_frame():
        app.settings_frame.place(relx=0.63, rely=0.59, anchor="center")  # Отображаем Frame
# hide settings frame
    def hide_frame():
        app.settings_frame.place_forget()  # Скрываем Frame

# start function
    def launch_callback():
        username = app.get_username()
        version_id = app.get_selected_version()

        if not username:
            print("Please enter your name")
            return

        if version_id == "Select Version":
            # select default vesrion if usern dont select it
            version_id = choice(launcher.version_ids)
            print(f"Auto-selected version: {version_id}")

        launcher.launch_minecraft(version_id, username)

    app = App(launch_callback, show_frame, hide_frame)

    app.set_version_options(launcher.version_ids)
    # start gui
    app.run()


if __name__ == "__main__":
    main()