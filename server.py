# -*- coding:utf-8 -*-
import os
import psutil
import shutil
import commands
from rpyc import Service
from rpyc.utils.server import ThreadedServer


class RemoteCallScript(Service):
    def exposed_listdir(self, path):
        return os.listdir(path)

    def exposed_rmdir(self, path):
            return shutil.rmtree(path)

    def exposed_move(self, oldpos, newpos):
        if not os.path.exists(oldpos):
            return False

        if not os.path.exists(newpos):
            os.makedirs(newpos)
        return shutil.move(oldpos, newpos)

    def exposed_process_list(self):
        p = psutil.process_iter()
        return list(p)

    def exposed_shell(self, cmd):
        a = commands.getoutput(cmd)
        return a

s = ThreadedServer(RemoteCallScript, port=11111, auto_register=False)
s.start()
