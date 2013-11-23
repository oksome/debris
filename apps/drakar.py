import os
import sys
import platform

from os.path import isfile, join

DRAKAR_PATH = os.environ.get('DRAKAR', '/mnt/drakar')
SYSTEM = sys.platform + '-' + platform.machine()

sources = {
    'linux2-x86_64/processing-2.1-linux64.tgz': 'http://download.processing.org/processing-2.1-linux64.tgz',
    }

def get_archive(filename):
    
    archives_path = join(DRAKAR_PATH, 'archives', SYSTEM)
    # => /mnt/drakar/archives/linux2-x86_64
    
    file_path = join(archives_path, filename)
    # => /mnt/drakar/archives/linux2-x86_64/filename.foo
    
    if not isfile(file_path)
        here = os.getcwd()
        source = sources[join(SYSTEM, filename)]
        
        os.chdir(archives_path)
        os.system('wget ' + source)
        os.chdir(here)
    
    if isfile(file_path):
        return file_path
    else:
        raise IOError("Could not obtain '{}' in Drakar".format(filename))

get_archive('processing-2.1-linux64.tgz')
