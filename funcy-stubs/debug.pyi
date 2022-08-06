from types import TracebackType
from typing import Any, Callable, Iterator, List, Optional, Type, Union

from funcy.decorators import Call

print_durations: Any
print_errors: Any

class LabeledContextDecorator:
    print_func: Any
    label: Any
    repr_len: Any
    def __init__(
        self,
        print_func: Callable,
        label: Optional[str] = ...,
        repr_len: Union[int, Callable[..., int]] = ...,
    ) -> None: ...
    def __call__(
        self, label: Optional[Callable] = ..., **kwargs
    ) -> Union[LabeledContextDecorator, Callable]: ...
    def decorator(self, func: Callable) -> Callable: ...

class log_errors(LabeledContextDecorator):
    stack: Any
    def __enter__(self) -> log_errors: ...
    def __exit__(
        self,
        _exc_type: Optional[Type[BaseException]],
        _exc_value: Optional[BaseException],
        _traceback: Optional[TracebackType],
    ) -> None: ...
    def __init__(
        self,
        print_func: Callable,
        label: Optional[str] = ...,
        stack: bool = ...,
        repr_len: Union[int, Callable[..., int]] = ...,
    ) -> None: ...

class log_durations(LabeledContextDecorator):
    format_time: Any
    threshold: Any
    start: Any
    def __enter__(self) -> log_durations: ...
    def __exit__(
        self,
        _exc_type: Optional[Type[BaseException]],
        _exc_value: Optional[BaseException],
        _traceback: Optional[TracebackType],
    ) -> None: ...
    def __init__(
        self,
        print_func: Callable,
        label: Optional[str] = ...,
        unit: str = ...,
        threshold: float = ...,
        repr_len: Union[int, Callable[..., int]] = ...,
    ) -> None: ...

def log_calls(
    call: Call,
    print_func: Callable,
    errors: bool = ...,
    stack: bool = ...,
    repr_len: Union[int, Callable[..., int]] = ...,
): ...
def log_enters(
    call: Call, print_func: Callable, repr_len: Union[int, Callable[..., int]] = ...
): ...
def log_exits(
    call, print_func, errors: bool = ..., stack: bool = ..., repr_len=...
): ...
def log_iter_durations(
    seq: List[int], print_func: Callable, label: None = ..., unit: str = ...
) -> Iterator[int]: ...
def print_enters(repr_len: Union[int, Callable[..., int]] = ...): ...
def print_exits(errors: bool = ..., stack: bool = ..., repr_len=...): ...
def print_iter_durations(seq, label: Optional[Any] = ..., unit: str = ...): ...
def print_calls(
    errors: Union[bool, Callable] = ...,
    stack: bool = ...,
    repr_len: Union[int, Callable[..., int]] = ...,
) -> Callable: ...
def tap(x: Union[int, Callable[..., int]], label: Optional[str] = ...) -> int: ...
