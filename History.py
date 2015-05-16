class History:
    hist = []

    def add(self, tally):
        self.hist.append(tally)

    def get(self, nr):
        if nr < 0 or nr > self.count():
            return 0
        else:
            return self.hist[nr]

    def count(self):
        return self.hist.count()

    def toHTML(self):
        str = "History: "
        for point in self.hist:
            str += point + " "
        return str