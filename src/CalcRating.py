import numpy as np
from src.Types import DataType


RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.quantile: list = []

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating

    def q1(self) -> RatingType:
        self.rating = sorted(self.rating.items(), key=lambda item: item[1])
        dict_len = len(self.rating)
        rating_list = list(self.rating)
        rating_q1 = np.percentile(
            [rating_list[k][1] for k in range(len(rating_list))], 25)
        for i in range(len(rating_list)):
            if rating_list[i][1] <= rating_q1:
                self.quantile.append(rating_list[i])

        return self.quantile
