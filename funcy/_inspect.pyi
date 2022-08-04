from typing import Any, Callable, Dict, NamedTuple, Set

ARGS: Dict[str, Dict[str, str]]
STD_MODULES: Set[str]

class Spec(NamedTuple):
    max_n: Any
    names: Any
    req_n: Any
    req_names: Any
    kw: Any

def get_spec(func: Callable, _cache: Dict[Callable, Spec] = ...) -> Spec: ...
