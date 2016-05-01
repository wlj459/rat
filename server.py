# -*- coding:utf-8 -*-
import os
import psutil
from rpyc import Service
from rpyc.utils.server import ThreadedServer


class RemoteCallScript(Service):
    def exposed_get_file_list(self, path):
        return os.listdir(path)

    def exposed_get_process_list(self):
        p = psutil.process_iter()
        return list(p)


s = ThreadedServer(RemoteCallScript, port=11111, auto_register=False)
s.start()
