from typing import Hashable, List, Set, Tuple, Union, Dict, Any, Optional

foo = Optional[int]
bar = Union[int, str]
baz = List[str]

baz.append("Hello")
print(baz)