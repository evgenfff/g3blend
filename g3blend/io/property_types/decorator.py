from typing import List, Dict, Optional, List

def _process_class(cls, name: Optional[str], aliases: Optional[List[str]]):
    from ..property_types import registry
    registry.PropertyTypeRegistry.register(cls, name if name else cls.__name__)
    if aliases:
        for alias in aliases:
            registry.PropertyTypeRegistry.register(cls, alias)
    return cls


def property_type(cls=None, *, name: Optional[str] = None, aliases: Optional[List[str]] = None):
    """Register in data type registry."""

    def wrap(cls):
        return _process_class(cls, name, aliases)

    # See if we're being called as @property_type or @property_type().
    if cls is None:
        # We're called with parens.
        return wrap

    # We're called as @property_type without parens.
    return wrap(cls)
