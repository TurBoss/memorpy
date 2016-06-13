import os

from cffi import FFI

ffi = FFI()
ffi.cdef(
"""
	bool IsUserAnAdmin(void);
"""
)

C = ffi.dlopen('shell32.dll')


def checkAdmin():
    isAdmin = C.IsUserAnAdmin()
    
    return isAdmin

