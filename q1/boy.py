class Boy:
    """  Class for boy"""
    def __init__(self, name, attractiveness, min_attraction, intelligence, budget, single=1):
        """
        :param name: name of boy
        :param attractiveness: attractiveness of boy
        :param min_attraction: minimum attraction of girl required
        :param intelligence: intelligence of boy
        :param budget: budget of boy
        :param single: commitment status
        """
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.single = single
        self.min_attraction = min_attraction

    def __str__(self):
        return str(self.single)

    def change_commitment(self, val=0):
        """
        change commitment status to given value
        :param val:
        :return:
        """
        if self.single:
            self.single = val
        else:
            self.single = val

