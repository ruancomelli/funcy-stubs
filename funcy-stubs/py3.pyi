from typing import Any

from .calc import *
from .colls import *
from .debug import *
from .decorators import *
from .flow import *
from .funcolls import *
from .funcs import *
from .objects import *
from .primitives import *
from .seqs import *
from .strings import *
from .tree import *
from .types import *

def lzip(*seqs): ...

# This is a very complicated module, so for now we mark it as incomplete with
# the `__getattr__` special function.
# See https://github.com/python/typeshed/issues/5

def __getattr__(name: str) -> Any: ...
