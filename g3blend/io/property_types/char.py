from dataclasses import dataclass

from .decorator import property_type
from ..binary import BinaryReader, BinarySerializable, BinaryWriter


@property_type(name='char')
@dataclass(slots=True)
class gChar(BinarySerializable):
    value: bytes

    def read(self, reader: BinaryReader) -> None:
        self.value = reader.read_char()

    def write(self, writer: BinaryWriter) -> None:
        writer.write_char(self.value)
