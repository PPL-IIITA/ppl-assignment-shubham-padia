class Girl:
    """  Class for girl"""
    def __init__(self, name, attractiveness, intelligence, budget, single=1):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.__single = single

    def __str__(self):
        return str(self.__single)

    def change_commitment(self):
        if self.__single:
            self.__single = 0
        else:
            self.__single = 1
