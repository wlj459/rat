# -*- coding:utf-8 -*-
import os
from rpyc import Service
from rpyc.utils.server import ThreadedServer


class RemoteCallScript(Service):
    def exposed_get_file_list(self, path):
        return os.listdir(path)

s = ThreadedServer(RemoteCallScript, port=111, auto_register=False)
s.start()
