import Predictor

BAR_SIZE = 60


class Peeps:
    predictors = []

    def __init__(self, nrOfPredictors):
        for i in range(0, nrOfPredictors):
            self.predictors.append(Predictor.CPredictor(0, True))

    def getBestPredictor(self):
        return self.predictors[0]

    def evaluatePredictors(self, tally):
        # The predictor is increased by one if it correctly predicted the tally being higher or lower than the threshold
        for pred in self.predictors:
            if (pred.getLastPrediction() <= BAR_SIZE and tally <= BAR_SIZE) or (pred.getLastPrediction() > BAR_SIZE and tally > BAR_SIZE):
                pred.incRanking()

        # Sort predictors by descending ranking
        self.predictors.sort(key=lambda x: x.getRanking(), reverse=True)