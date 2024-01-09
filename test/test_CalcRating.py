from src.Types import DataType
from src.CalcRating import CalcRating
import pytest


RatingsType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
        "ИвановИванИванович": [
                ("математика", 67), ("литература", 100),
                ("программирование", 91)
            ],
        "ПетровПетрПетрович": [
                ("математика", 78), ("химия", 87), ("социология", 61)
            ],
        "ПановАртёмЯрославович": [
                ("математика", 56), ("литература", 67),
                ("программирование", 78)
            ],
        "ИльинаСофьяДанииловна": [
                ("математика", 68), ("литература", 87),
                ("программирование", 71)
            ],
        "МироновЮрийМихайлович": [
                ("математика", 90), ("литература", 67),
                ("программирование", 98)
            ],
        "ЕфремоваАлинаДанииловна": [
                ("математика", 78), ("литература", 76),
                ("программирование", 87)
            ],
        "СеминМатвейМаркович": [
                ("математика", 89), ("литература", 100),
                ("программирование", 87)
            ],
        "ЗыковаЕлизаветаГригорьевна": [
                ("математика", 92), ("литература", 76),
                ("программирование", 96)
            ],
        "МакароваЕлизаветаСвятославовна": [
                ("математика", 87), ("литература", 57),
                ("программирование", 100)
            ],
        "АндрееваДарьяКирилловна": [
                ("математика", 87), ("литература", 57),
                ("программирование", 100)
            ]
        }

        rating_scores: RatingsType = {
            "ИвановИванИванович": 86.0,
            "ПетровПетрПетрович": 75.33333333333333,
            "ПановАртёмЯрославович": 67.0,
            "ИльинаСофьяДанииловна": 75.33333333333333,
            "МироновЮрийМихайлович": 85.0,
            "ЕфремоваАлинаДанииловна": 80.33333333333333,
            "СеминМатвейМаркович": 92.0,
            "ЗыковаЕлизаветаГригорьевна": 88.0,
            "МакароваЕлизаветаСвятославовна": 81.33333333333333,
            "АндрееваДарьяКирилловна": 81.33333333333333
        }

        rating_q1: list = [
            ("ПановАртёмЯрославович", 67.0),
            ("ПетровПетрПетрович", 75.33333333333333),
            ("ИльинаСофьяДанииловна", 75.33333333333333)
        ]
        return data, rating_scores, rating_q1

    def test_init_calc_rating(self, input_data:
                              tuple[DataType, RatingsType]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
    
    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:
        calc = CalcRating(input_data[0])
        calc_rating = calc.calc()
        q1 = calc.q1()
        for student in range(len(input_data[2])-1):
            assert pytest.approx(q1[student][student],
                                 abs=0.001) == input_data[2][student][student]