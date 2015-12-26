import platform

if platform.machine().startswith('arm'):
    from box2d_arm7 import *
else:
    if platform.architecture()[0] == '64bit':
        from box2d_64 import *
    else:
        from ctypes import cdll
        libstdc = cdll.LoadLibrary("lib/libstdc++.so")
        from box2d_32 import *
