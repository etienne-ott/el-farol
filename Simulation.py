from Peep import Peeps
from History import CHistory
from Predictor import CPredictor
from Parameters import *

peeps = []
for i in range(0, POPULATION):
    peeps.append(Peeps(PREDICTORS_PER_PEEP))

history = CHistory()

for i in range(0, STEPS):
    # Predict
    tally = 0
    for peep in peeps:
        prediction = peep.getBestPredictor().predict(history)
        if prediction <= BAR_SIZE:
            tally += 1

    # Reevaluate
    for peep in peeps:
        peep.evaluatePredictors(tally)

    history.add(tally)

# Print output
print(history.toHTML())
print("<br/>")
print(CPredictor.getRankingsAsHTML())