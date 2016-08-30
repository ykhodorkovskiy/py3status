import requests
import sys
import shutil
import os


SYS_PACKAGES = ['dbus']

PYTHON_2 = sys.version_info < (3, 0)
SITE_PACKAGES_PATH = '/'.join(requests.__file__.split('/')[:-2])
TESTS_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-1])


if PYTHON_2:
    DIST_PACKAGES_PATH = '/usr/lib/python2.7/dist-packages'
else:
    DIST_PACKAGES_PATH = '/usr/lib/python3/dist-packages'

# Install any system packages inside our venv
for pkg in SYS_PACKAGES:
    src = os.path.join(DIST_PACKAGES_PATH, pkg)
    dst = os.path.join(SITE_PACKAGES_PATH, pkg)
    shutil.copytree(src, dst)
    print('system module %s moved' % pkg)

# Install our gi shim as system gi is really tricky to get working
dst = os.path.join(SITE_PACKAGES_PATH, 'gi.py')
src = os.path.join(TESTS_PATH, 'gi.py_')
shutil.copyfile(src, dst)
print('gi shim installed')
