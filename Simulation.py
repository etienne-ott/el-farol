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
        prediction = peep.get_best_predictor().predict(history)
        if prediction <= BAR_SIZE:
            tally += 1

    # Reevaluate
    for peep in peeps:
        peep.evaluate_predictors(tally)

    history.add(tally)

# Print output
print(history.to_html())
print("<br/>")
print(CPredictor.get_rankings_as_html())