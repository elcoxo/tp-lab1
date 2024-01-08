import pytest
import os
from src.Types import DataType
from src.XMLDataReader import XMLDataReader
from xml.etree import ElementTree


class TestTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:

        text = """
        <?xml version="1.0" encoding="UTF-8" ?>
        <root>
            <ИвановИванИванович>
                <математика>67</математика>
                <литература>100</литература>
                <программирование>91</программирование>
            </ИвановИванИванович>
            <ПетровПетрПетрович>
                <математика>78</математика>
                <химия>87</химия>
                <социология>61</социология>
            </ПетровПетрПетрович>
        </root>
        """

        data = {
            "ИвановИванИванович": [
                ("математика", 67), ("литература", 100), ("программирование", 91) 
            ],
            "ПетровПетрПетрович": [
                ("математика", 78), ("химия", 87), ("социология", 61) 
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        cwd = os.getcwd()
        p = os.path.join(cwd, 'data/data.xml')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data:
                  tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
