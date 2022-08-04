import sys
from collections import Hashable as Hashable
from collections import Iterable as Iterable
from collections import Iterator as Iterator
from collections import Mapping as Mapping
from collections import Sequence as Sequence
from collections import Set as Set
from itertools import filterfalse as filterfalse
from operator import itemgetter as itemgetter
from typing import Any, Callable, List, Tuple, Type, TypeVar, Union, overload

from typing_extensions import TypeGuard

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_S = TypeVar("_S")

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

basestring: Tuple[Type[bytes], Type[str]]

# overloads taken from typeshed for the `filter` function and adapted
@overload
def lfilter(
    self, __function: None, __iterable: Iterable[Union[_T, None]]
) -> List[_T]: ...
@overload
def lfilter(
    self, __function: Callable[[_S], TypeGuard[_T]], __iterable: Iterable[_S]
) -> List[_T]: ...
@overload
def lfilter(
    self, __function: Callable[[_T], Any], __iterable: Iterable[_T]
) -> List[_T]: ...
@overload
def lmap(self, __func: Callable[[_T], _S], __iter1: Iterable[_T]) -> List[_S]: ...
@overload
def lmap(
    self,
    __func: Callable[[_T1, _T2], _S],
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
) -> List[_S]: ...
@overload
def lmap(
    self,
    __func: Callable[[_T1, _T2, _T3], _S],
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
) -> List[_S]: ...
@overload
def lmap(
    self,
    __func: Callable[[_T1, _T2, _T3, _T4], _S],
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
) -> List[_S]: ...
@overload
def lmap(
    self,
    __func: Callable[[_T1, _T2, _T3, _T4, _T5], _S],
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
    __iter5: Iterable[_T5],
) -> List[_S]: ...
@overload
def lmap(
    self,
    __func: Callable[..., _S],
    __iter1: Iterable[Any],
    __iter2: Iterable[Any],
    __iter3: Iterable[Any],
    __iter4: Iterable[Any],
    __iter5: Iterable[Any],
    __iter6: Iterable[Any],
    *iterables: Iterable[Any],
) -> List[_S]: ...
