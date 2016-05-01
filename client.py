# -*- coding:utf-8 -*-
import rpyc
c = rpyc.connect("127.0.0.1", 11111)
a = c.root.listdir("/")
for i in a:
    print i
print "^^^^^^^^^^^^^^^^^^^^^^"
a = c.root.process_list()
for i in a:
        print i
print "^^^^^^^^^^^^^^^^^^^^^^"
# a = c.root.move('/Users/libai/code/rat/test', "/Users/libai/code/rat/yooo")
print "^^^^^^^^^^^^^^^^^^^^^^"
# a = c.root.rmdir('/Users/libai/code/rat/yooo')
a = c.root.shell("ls")
print a
c.close()
