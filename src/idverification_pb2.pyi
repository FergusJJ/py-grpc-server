from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerificationImageRequest(_message.Message):
    __slots__ = ("image_info", "chunk_data")
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    image_info: ImageInfo
    chunk_data: bytes
    def __init__(self, image_info: _Optional[_Union[ImageInfo, _Mapping]] = ..., chunk_data: _Optional[bytes] = ...) -> None: ...

class ImageInfo(_message.Message):
    __slots__ = ("message_id", "image_type", "identification_type")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    image_type: str
    identification_type: str
    def __init__(self, message_id: _Optional[str] = ..., image_type: _Optional[str] = ..., identification_type: _Optional[str] = ...) -> None: ...

class VerificationImageResponse(_message.Message):
    __slots__ = ("message_id", "message_length")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    message_length: int
    def __init__(self, message_id: _Optional[str] = ..., message_length: _Optional[int] = ...) -> None: ...
