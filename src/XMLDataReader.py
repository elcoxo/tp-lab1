from src.Types import DataType
from src.DataReader import DataReader
from xml.etree import ElementTree


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ElementTree.parse(path)
        root = tree.getroot()
        for child in root:
            self.key = child.tag
            self.students[self.key] = []
            for attrb in child:
                self.students[self.key].append(
                            (attrb.tag, int(attrb.text)))

        return self.students
