# -*- coding:utf-8 -*-
import rpyc
c = rpyc.connect("127.0.0.1", 11111)
print c.root.get_file_list("/")
c.close()
