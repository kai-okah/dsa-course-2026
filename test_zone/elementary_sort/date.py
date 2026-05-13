class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        if self.year < other.year: return True
        if self.year > other.year: return False
        if self.month < other.month:return True
        if self.month > other.month:return False
        if self.day < other.day:return True
        return False

    def __repr__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)
