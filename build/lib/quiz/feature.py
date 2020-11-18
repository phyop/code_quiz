# 1. 檔案要上傳到雲端（記憶體模擬）前，檔案的名稱必須經由 encrypt.FileNameCipher 的加密。
# 2. 創建的資料夾，要上傳檔案到雲端（記憶體模擬）前，資料夾的名稱必須經由 encrypt.FileNameCipher 的加密。
# 3. ls 指令的回傳結果，必須是明文。
# 4. 要多增加一個指令，可以選擇 “開啓/關閉” 功能1和2。

from quiz.cli import CommandLine
from base64 import urlsafe_b64encode, urlsafe_b64decode
from quiz.encrypt import FileNameCipher


class ClientFeature(CommandLine):

    def __init__(self, cloudclient):
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
