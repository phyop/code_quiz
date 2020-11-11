import cmd

from quiz.backend.cloudclient import MemoryCloudClient


def arg_parse(func):
    def outerfunc(self, line):
        try:
            args = tuple(line.split())
            return func(self, *args)
        except Exception as ex:
            print('Syntax error', ex)
    return outerfunc


class CommandLine(cmd.Cmd):
    prompt = 'quiz_cli:'

    def __init__(self, cloudclient):
        self._cloudclient = cloudclient
        super().__init__()

    @arg_parse
    def do_upload(self, parent_id, name, data):
        node = self._cloudclient.upload_file(parent_id, name, data)
        self._dump_nodes([node])

    @arg_parse
    def do_mkdir(self, parent_id, name):
        node = self._cloudclient.create_folder(parent_id, name)
        self._dump_nodes([node])

    @arg_parse
    def do_ls(self, folder_id):
        nodes = self._cloudclient.list_children(folder_id)
        self._dump_nodes(nodes)

    @arg_parse
    def do_root_id(self):
        print(self._cloudclient.root_id)

    def _dump_nodes(self, nodes):
        for node in nodes:
            print(node)

    def do_EOF(self, line):
        return True


def main():
    cloudclient = MemoryCloudClient()
    cli = CommandLine(cloudclient)
    cli.cmdloop()
