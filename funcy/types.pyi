from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    List,
    Mapping,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from typing_extensions import TypeGuard

_Any = TypeVar("_Any")
_Any1 = TypeVar("_Any1")
_Any2 = TypeVar("_Any2")
_Any3 = TypeVar("_Any3")
_Any4 = TypeVar("_Any4")

# TODO: replace the following `isa` overloads with variadic generics once mypy supports
# them
@overload
def isa(__type1: Type[_Any1]) -> Callable[[Any], TypeGuard[_Any1]]: ...
@overload
def isa(
    __type1: Type[_Any1], __type2: Type[_Any2]
) -> Callable[[Any], TypeGuard[Union[_Any1, _Any2]]]: ...
@overload
def isa(
    __type1: Type[_Any1], __type2: Type[_Any2], __type3: Type[_Any3]
) -> Callable[[Any], TypeGuard[Union[_Any1, _Any2, _Any3]]]: ...
@overload
def isa(
    __type1: Type[_Any1],
    __type2: Type[_Any2],
    __type3: Type[_Any3],
    __type4: Type[_Any4],
) -> Callable[[Any], TypeGuard[Union[_Any1, _Any2, _Any3, _Any4]]]: ...
@overload
def isa(*types: Type[_Any]) -> Callable[[Any], TypeGuard[_Any]]: ...
def is_mapping(x: Any) -> TypeGuard[Mapping[Any, Any]]: ...
def is_set(x: Any) -> TypeGuard[Set[Any]]: ...
def is_seq(x: Any) -> TypeGuard[Sequence[Any]]: ...
def is_list(x: Any) -> TypeGuard[List[Any]]: ...
def is_tuple(x: Any) -> TypeGuard[Tuple[Any, ...]]: ...
def is_seqcoll(x: Any) -> TypeGuard[Union[List[Any], Tuple[Any, ...]]]: ...
def is_seqcont(
    x: Any,
) -> TypeGuard[Union[List[Any], Tuple[Any, ...], Iterator[Any], range]]: ...
def iterable(x: Any) -> TypeGuard[Iterable[Any]]: ...
def is_iter(x: Any) -> TypeGuard[Iterator[Any]]: ...
