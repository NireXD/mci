from ctypes import create_unicode_buffer, windll, wintypes
from time import sleep

windll.winmm.mciSendStringW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UINT, wintypes.HANDLE]
windll.winmm.mciGetErrorStringW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.UINT]

def mci(command, buffer_length=600):
	buffer = create_unicode_buffer(buffer_length)
	error_code = windll.winmm.mciSendStringW(command, buffer, buffer_length - 1, 0)
	if error_code:
		error_buffer = create_unicode_buffer(buffer_length)
		windll.winmm.mciGetErrorStringW(error_code, error_buffer, buffer_length - 1)
		exception_message = (
			'\n' + '\t' + f'Error {error_code} for command:' \
			'\n' + '\t\t' + command + 
			'\n' + '\t' + error_buffer.value
		)
		raise Exception(exception_message)
	return buffer.value
