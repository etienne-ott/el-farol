class CHistory:
    def __init__(self):
        self.hist = []

    def add(self, tally):
        self.hist.append(tally)

    def get(self, nr):
        # nr is one-indexed
        if nr < 0 or nr > self.count() - 1:
            return 0
        else:
            return self.hist[nr - 1]

    def last(self):
        if len(self.hist) > 0:
            return self.hist[len(self.hist) - 1]
        else:
            return 0

    def count(self):
        return len(self.hist)

    def to_html(self):
        html = "History: "
        for point in self.hist:
            html += str(point) + " "
        return html