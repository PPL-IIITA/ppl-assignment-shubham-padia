class Boy:
    """  Class for boy"""
    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1, happiness=0):
        self.name = name
        self.attractiveness = int(attractiveness)
        self.intelligence = int(intelligence)
        self.budget = int(budget)
        self.single = single
        self.min_attraction = int(min_attraction)
        self.happiness = happiness

    def __str__(self):
        return str(self.single)

    def change_commitment(self):
        if self.single:
            self.single = 0
        else:
            self.single = 1


class GeekBoy(Boy):

    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1, happiness=0):
        Boy.__init__(self, name, attractiveness, min_attraction, intelligence, budget, single, happiness)

    def get_happiness(self, girlfriend):
        return girlfriend.intelligence


class MiserBoy(Boy):

    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1, happiness=0):
        Boy.__init__(self, name, attractiveness, min_attraction, intelligence, budget, single, happiness)

    def get_happiness(self, girlfriend):
        return self.budget - girlfriend.budget


class GenerousBoy(Boy):

    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1, happiness=0):
        Boy.__init__(self, name, attractiveness, min_attraction, intelligence, budget, single, happiness)

    def get_happiness(self, girlfriend):
        return girlfriend.happiness


