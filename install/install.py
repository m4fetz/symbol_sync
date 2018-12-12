import os
import subprocess
import shutil

file_names = [  'digital_symbol_sync_xx.xml',
                'timing_error_detector.cc',
                'timing_error_detector.h',
                'timing_error_detector_type.h']

#/home/max/prefix/src/gnuradio/gr-digital/ grc/digital_symbol_sync_xx.xml
#/home/max/prefix/src/gnuradio/gr-digital/ lib/timing_error_detector.cc
#/home/max/prefix/src/gnuradio/gr-digital/ lib/timing_error_detector.h
#/home/max/prefix/src/gnuradio/gr-digital/ include/gnuradio/digital/timing_error_detector_type.h

def getBasePath():
    """
	__file__ will point to */install/install.py
	dirname() will give to containing folder 'python'
	by going one folder up we end up with the install folder
	realpath() will resolve any symlinks and return the actual path to the folder
    """
    return os.path.realpath(os.path.dirname(__file__))

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    raise Exception('oh no')

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

#find the corresponding paths
result=[]
src=[]


for x in file_names:
                    #this has to be an arg_prefix
    fname = find(x, '/home/max/prefix' )
    result.append(fname)
    src.append(getBasePath()+'/modified_files/'+x) #--> is the source directory



len = len(result)
#print(len)
for x in range(4):
    shutil.copy2(src[x], '/home/max/Desktop/test_install/')

#dst = result[]


#subprocess popen --> make and make install
#argparse  --> pass the needed directory

#copy/exchange the new files
#takes the path of find_all    --> src=new files
    #shutil.copyfile(src, dst) --> dst=result[]

command_line = ['']
