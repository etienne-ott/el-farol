class CHistory:
    hist = []

    def add(self, tally):
        self.hist.append(tally)

    def get(self, nr):
        # nr is one-indexed
        if nr < 0 or nr > self.count() - 1:
            return 0
        else:
            return self.hist[nr - 1]

    def last(self):
        return self.hist[len(self.hist) - 1]

    def count(self):
        return len(self.hist)

    def toHTML(self):
        html = "History: "
        for point in self.hist:
            html += str(point) + " "
        return html