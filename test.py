import re

"""txt = "The rain in Span"
x = re.search("^The.*Spain$", txt)
n=str(type(x))
print("--  " + n)
#<class 'NoneType'>
#<class 're.Match'>"""

import re

txt = "The rain in Span"
x = re.search("^The.*Spain$", txt)
print(x.string)