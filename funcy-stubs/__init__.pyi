from .compat import PY2

if PY2:
    from .py2 import *
else:
    from .py3 import *
