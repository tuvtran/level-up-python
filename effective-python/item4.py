"""
Write Helper Functions instead of Complex Expressions
"""
from urllib.parse import parse_qs

my_values = parse_qs(
    'red=5&blue=0&green='
)
print(repr(my_values))

# BAD
print('Red: ', my_values.get('red'))
print('Green: ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

# Still bad
red = my_values.get('red', None) or 0
green = my_values.get('green', None) or 0
opacity = my_values.get('opacity', None) or 0
