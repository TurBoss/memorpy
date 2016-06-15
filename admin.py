import os

from cffi import FFI

ffi = FFI()
ffi.cdef(
"""
	bool IsUserAnAdmin(void);
"""
)

C = ffi.dlopen('shell32.dll')


def check_admin():
    is_admin = C.IsUserAnAdmin()
    
    return is_admin

