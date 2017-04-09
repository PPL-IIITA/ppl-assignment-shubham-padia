class Gift:
    def __init__(self, name, price, value):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of the gift
        """
        self.name = name
        self.price = int(price)
        self.value = int(value)


class EssentialGift(Gift):
    def __init__(self, name, price, value):
        Gift.__init__(self, name, price, value)


class LuxuryGift(Gift):
    def __init__(self, name, price, value, difficulty, rating):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of gift
        :param difficulty: difficulty in obtaining the gift
        :param rating: rating of the gift
        """
        Gift.__init__(self, name, price, value)
        self.difficulty = int(difficulty)
        self.rating = int(rating)


class UtilityGift(Gift):
    def __init__(self, name, price, value, utility_value, utility_class):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of gift
        :param utility_value: utility value of gift
        :param utility_class: utlility class of gift
        """
        Gift.__init__(self, name, price, value)
        self.utility_value = int(utility_value)
        self.utility_class = utility_class
