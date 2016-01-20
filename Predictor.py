from random import randint
from Parameters import *


class CPredictor:

    predictors = {}
    id = 0
    ranking = 0
    lastPrediction = 0

    def __init__(self, id, initAsRandom):
        if initAsRandom:
            self.id = randint(1, NR_OF_PREDICTORS)
        elif id:
            self.id = id
        else:
            raise Exception("No ID given for nonrandom predictor in constructor.")

        CPredictor.predictors[self.id] = self

    def predict(self, history):
        if self.id == 1:
            self.lastPrediction = 0
        elif self.id == 2:
            self.lastPrediction = POPULATION
        elif self.id == 3:
            self.lastPrediction = randint(0, POPULATION)
        elif self.id == 4:
            self.lastPrediction = BAR_SIZE + randint(-5, 5)
        elif self.id == 5:
            self.lastPrediction = BAR_SIZE - 1
        elif self.id == 6:
            self.lastPrediction = history.last()
        elif self.id == 7:
            self.lastPrediction = history.last() - 10
        elif self.id == 8:
            self.lastPrediction = history.last() + 10
        elif self.id == 9:
            self.lastPrediction = history.get(history.count() - 2)
        else:
            raise Exception("Unexpected predictor ID: " + str(self.id))

        return self.lastPrediction

    def getId(self):
        return self.id

    def incRanking(self):
        self.ranking += 1

    def getRanking(self):
        return self.ranking

    def getLastPrediction(self):
        return self.lastPrediction

    @staticmethod
    def getRankingsAsHTML():
        output = "Rankings:<br/>"
        for pred in CPredictor.predictors.values():
            output += str(pred.getId()) + ": " + str(pred.getRanking()) + "<br/>"
        return output
