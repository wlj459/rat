# -*- coding:utf-8 -*-
import rpyc
c = rpyc.connect("xxxx.xxxxx.xxxx", 111)
print c.root.get_file_list("\\")
c.close()
