# -*- coding:utf-8 -*-
import rpyc
c = rpyc.connect("127.0.0.1", 11111)
print c.root.get_file_list("/")
print "^^^^^^^^^^^^^^^^^^^^^^"
a = c.root.get_process_list()
print "^^^^^^^^^^^^^^^^^^^^^^"
for i in a:
        print i
c.close()
