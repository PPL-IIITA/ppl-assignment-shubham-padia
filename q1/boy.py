class Boy:
    """  Class for boy"""
    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.single = single
        self.min_attraction = min_attraction

    def __str__(self):
        return str(self.single)

    def change_commitment(self):
        if self.single:
            self.single = 0
        else:
            self.single = 1
