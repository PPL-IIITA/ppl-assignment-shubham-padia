class EssentialGift:
    def __init__(self, name, price, value):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of the gift
        """
        self.name = name
        self.price = int(price)
        self.value = int(value)


class LuxuryGift:
    def __init__(self, name, price, value, difficulty, rating):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of gift
        :param difficulty: difficulty in obtaining the gift
        :param rating: rating of the gift
        """
        self.name = name
        self.value = int(value)
        self.price = int(price)
        self.difficulty = int(difficulty)
        self.rating = int(rating)


class UtilityGift:
    def __init__(self, name, price, value, utility_value, utility_class):
        """
        :param name: name of gift
        :param price: price of gift
        :param value: value of gift
        :param utility_value: utility value of gift
        :param utility_class: utlility class of gift
        """
        self.name = name
        self.utility_value = int(utility_value)
        self.utility_class = utility_class
        self.price = int(price)
        self.value = int(value)
