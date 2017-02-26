class Girl:
    """  Class for girl"""
    def __init__(self, name, attractiveness, intelligence, budget, category, single=1, happiness=0):
        """
        :param name: Name of the girl
        :param attractiveness: attractiveness of the girl
        :param intelligence: intelligence of the girl
        :param budget: maintenance budget if the girl
        :param category: Category of the girl, wither choosy, normal or desperate
        :param single: single status, either 0 or 1
        :param happiness: happiness of girl
        """
        self.name = name
        self.attractiveness = int(attractiveness)
        self.intelligence = int(intelligence)
        self.budget = int(budget)
        self.__single = single
        self.category = category
        self.happiness = happiness

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

