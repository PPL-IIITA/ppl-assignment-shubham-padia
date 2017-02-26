class Boy:
    """  Class for boy"""
    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, category, single=1, happiness=0):
        self.name = name
        self.attractiveness = int(attractiveness)
        self.intelligence = int(intelligence)
        self.budget = int(budget)
        self.category = category
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


