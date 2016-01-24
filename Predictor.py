from random import randint
from Parameters import *


class CPredictor:
    predictors = {}

    def __init__(self, predictor_id, init_as_random):
        if init_as_random:
            self.id = randint(1, NR_OF_PREDICTORS)
        elif predictor_id:
            self.id = predictor_id
        else:
            raise Exception("No ID given for nonrandom predictor in constructor.")

        self.ranking = 0
        self.last_prediction = 0
        CPredictor.predictors[self.id] = self

    def predict(self, history):
        if self.id == 1:
            self.last_prediction = 0
        elif self.id == 2:
            self.last_prediction = POPULATION
        elif self.id == 3:
            self.last_prediction = randint(0, POPULATION)
        elif self.id == 4:
            self.last_prediction = BAR_SIZE + randint(-5, 5)
        elif self.id == 5:
            self.last_prediction = BAR_SIZE - 1
        elif self.id == 6:
            self.last_prediction = history.last()
        elif self.id == 7:
            self.last_prediction = history.last() - 10
        elif self.id == 8:
            self.last_prediction = history.last() + 10
        elif self.id == 9:
            self.last_prediction = history.get(history.count() - 2)
        else:
            raise Exception("Unexpected predictor ID: " + str(self.id))

        return self.last_prediction

    def get_id(self):
        return self.id

    def inc_ranking(self):
        self.ranking += 1

    def get_ranking(self):
        return self.ranking

    def get_last_prediction(self):
        return self.last_prediction

    @staticmethod
    def get_rankings_as_html():
        output = "Rankings:<br/>"
        for pred in CPredictor.predictors.values():
            output += str(pred.get_id()) + ": " + str(pred.get_ranking()) + "<br/>"
        return output
