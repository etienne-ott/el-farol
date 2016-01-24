import Predictor
from Parameters import *


class Peeps:
    predictors = []

    def __init__(self, nr_of_predictors):
        for i in range(0, nr_of_predictors):
            self.predictors.append(Predictor.CPredictor(0, True))

    def get_best_predictor(self):
        return self.predictors[0]

    def evaluate_predictors(self, tally):
        # The predictor is increased by one if it correctly predicted the tally being higher or lower than the threshold
        for pred in self.predictors:
            if (pred.get_last_prediction() <= BAR_SIZE and tally <= BAR_SIZE) or\
                    (pred.get_last_prediction() > BAR_SIZE and tally > BAR_SIZE):
                pred.inc_ranking()

        # Sort predictors by descending ranking
        self.predictors.sort(key=lambda x: x.get_ranking(), reverse=True)