"""
Differences between bytes, str, and unicode

Python 3:
- bytes: raw 8-bit values
- str: unicode characters

encode(): str or bytes -> bytes
decode(): str or bytes -> str

Python 2:
- str: raw 8-bit values
- unicode: unicode characters

encode(): str or unicode -> str
decode(): str or unicode -> unicode
"""
import json

name = "Tuấn Tú"

with open('demo.txt', mode='w') as f:
    f.write(name)

print(open('demo.txt', mode='rb').read().decode('utf-8'))
