from dataclasses import dataclass

from ..binary import BinaryReader, BinarySerializable, BinaryWriter


@dataclass()
class bCVector4(BinarySerializable):
    x: float
    y: float
    z: float
    w: float

    def read(self, reader: BinaryReader) -> None:
        self.x = reader.read_float()
        self.y = reader.read_float()
        self.z = reader.read_float()
        self.w = reader.read_float()

    def write(self, writer: BinaryWriter) -> None:
        writer.write_float(self.x)
        writer.write_float(self.y)
        writer.write_float(self.z)
        writer.write_float(self.w)
