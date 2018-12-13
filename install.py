import os
import subprocess, shlex
import shutil
import argparse

file_names = [  'digital_symbol_sync_xx.xml',
                'timing_error_detector.cc',
                'timing_error_detector.h',
                'timing_error_detector_type.h']
result=[]
src=[]

#input the destination folder
parser = argparse.ArgumentParser(description='Update and Installation of an OQPSK TED for the \
                                              Symbol-Sync Block in GNURadio')
parser.add_argument('dst', metavar='destination',  type=str, help='Select the destination\
                    for the installation')
args = parser.parse_args()



#get the path of the modified files
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
    raise Exception('no files found')


#find the corresponding paths
for x in file_names:
    fname = find(x, args.dst)
    result.append(fname)
    src.append(getBasePath()+'/modified_files/'+x)

print('copying files')

len = len(result)
for x in range(len):
    shutil.copy2(src[x], result[x])

#go to build folder
dst = args.dst + ('src/gnuradio/build')
os.chdir(dst)

# make && make install in build folder
subprocess.Popen('make'.split(' ')).wait()
subprocess.Popen('make install'.split(' ')).wait()
print('\nInstallation done')
