class Girl:
    """  Class for girl"""
    def __init__(self, name, attractiveness, intelligence, budget, single=1):
        """
        :param name: name of girl
        :param attractiveness: attractiveness of girl
        :param intelligence: intelligence of girl
        :param budget: budget of girl
        :param single: commitment status
        """
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.__single = single

    def __str__(self):
        return str(self.__single)

    def change_commitment(self, val=0):
        """
        change commitment status to given value
        :param val:
        :return:
        """
        if self.__single:
            self.__single = val
        else:
            self.__single = val
