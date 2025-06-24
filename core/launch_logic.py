import minecraft_launcher_lib
import subprocess
import threading

class Launcher:
    def __init__(self):
        # get version list
        version_list = minecraft_launcher_lib.utils.get_version_list()
        self.version_ids = [version['id'] for version in version_list]

    def launch_minecraft(self, version_id, username, minecraft_directory):
        # installing minecraft
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version_id,
            minecraft_directory=minecraft_directory
        )

        # start options
        options = {
            'username': username,
            'uuid': '1',  # fixed UUID for demo
            'token': '',
        }

        # start minecraft thread
        minecraft_thread = threading.Thread(
            target=self._run_minecraft,
            args=(version_id, minecraft_directory, options))
        minecraft_thread.start()

    # method for starting minecraft
    def _run_minecraft(self, version_id, minecraft_directory, options):
        command = minecraft_launcher_lib.command.get_minecraft_command(
            version=version_id,
            minecraft_directory=minecraft_directory,
            options=options
        )
        subprocess.call(command)