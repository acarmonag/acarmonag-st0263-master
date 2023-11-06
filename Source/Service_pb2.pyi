from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Archive(_message.Message):
    __slots__ = ["busqueda"]
    BUSQUEDA_FIELD_NUMBER: _ClassVar[int]
    busqueda: str
    def __init__(self, busqueda: _Optional[str] = ...) -> None: ...

class singleTransactionResponse(_message.Message):
    __slots__ = ["nombre", "last_updated", "size"]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    last_updated: str
    size: float
    def __init__(self, nombre: _Optional[str] = ..., last_updated: _Optional[str] = ..., size: _Optional[float] = ...) -> None: ...

class multipleTransactionResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[singleTransactionResponse]
    def __init__(self, files: _Optional[_Iterable[_Union[singleTransactionResponse, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
