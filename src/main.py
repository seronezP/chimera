from src.gui.MainWindow import App
from src.core.launch_logic import Launcher
from random import choice

def main():
    launcher = Launcher()

    # start minecraft func
    def launch_callback():
        username = app.get_username()
        version_id = app.get_selected_version()
        minecraft_directory = app.get_minecraft_path()

        if not username:
            print("Please enter your name")
            return

        if version_id == "Select Version":
            # set default version if user not
            version_id = choice(launcher.version_ids)
            print(f"Auto-selected version: {version_id}")

        launcher.launch_minecraft(version_id, username, minecraft_directory)

    # creating and start window app
    app = App(launch_callback)
    app.set_version_options(launcher.version_ids)
    app.run()

if __name__ == "__main__":
    main()