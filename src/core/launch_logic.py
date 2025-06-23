import minecraft_launcher_lib
import subprocess
import threading

# constants
MINECRAFT_DIRECTORY = '/Users/stepanlukoyanov/seronez/chimera_laucnher/.minecraft'
UUID = '1'

class Launcher:
    def __init__(self):
        # get version list
        version_list = minecraft_launcher_lib.utils.get_version_list()
        self.version_ids = [version['id'] for version in version_list]

    def launch_minecraft(self, version_id, username):
        # installing minecraft
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version_id,
            minecraft_directory=MINECRAFT_DIRECTORY
        )

        # start optins
        """WITHOUT ENTER USERNAME MINECRAFT DONT START"""
        options = {
            'username': username,
            'uuid': UUID,
            'token': '',
        }

        # start minecraft thread
        minecraft_thread = threading.Thread(
            target=self._run_minecraft,
            args=(version_id, options))
        minecraft_thread.start()

    # method for starting minecraft
    def _run_minecraft(self, version_id, options):
        command = minecraft_launcher_lib.command.get_minecraft_command(
            version=version_id,
            minecraft_directory=MINECRAFT_DIRECTORY,
            options=options
        )
        subprocess.call(command)