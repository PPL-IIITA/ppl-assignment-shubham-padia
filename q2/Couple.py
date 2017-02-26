import math


class Couple:
    def __init__(self, boy, girl, gift_list, happiness=0):
        """
        :param boy: boy object
        :param girl: girl object
        :param gift_list: list of gift object
        :param happiness: happiness of couple
        """
        self.boy = boy
        self.girl = girl
        self.happiness = happiness
        self.gifts = []
        self.gift_cost = 0
        self.gift_value = 0
        self.luxury_gift_cost = 0
        self.allocate_gifts(gift_list)
        self.set_happiness()
        self.compatibility = self.get_compatibility()

    def allocate_gifts(self, gift_list):
        """
        Allocates gift from given gift lisr
        :param gift_list: list of gift objects
        :return:
        """
        for gift in gift_list:
            if (self.boy.category == 'miser' or 'geeks') and self.gift_cost < self.girl.budget:
                if type(gift).__name__ == 'LuxuryGift':
                    self.luxury_gift_cost += gift.price
                self.gifts.append(gift)
                self.gift_cost += gift.price
                self.gift_value += gift.value
            if self.boy.category == 'generous' and self.gift_cost < self.boy.budget:
                if type(gift).__name__ == 'LuxuryGift':
                    self.luxury_gift_cost += gift.price
                    self.gifts.append(gift)
                self.gift_cost += gift.price
                self.gift_value += gift.value

    def set_happiness(self):
        """
        Calculates boy's and girl's happiness individually and adds it.
        :return:
        """
        if self.girl.category == 'choosy':
            self.girl.happiness = math.log(self.gift_cost + self.luxury_gift_cost)
        elif self.girl.category == 'normal':
            self.girl.happiness = self.gift_cost + self.gift_value
        else:
            self.girl.happiness = math.exp(self.gift_cost/1000)
        if self.boy.category == 'miser':
            self.boy.happiness = self.boy.budget - self.girl.budget
        elif self.boy.category == 'generous':
            self.boy.happiness = self.girl.happiness
        else:
            self.boy.happiness = self.girl.intelligence
        self.happiness = self.boy.happiness + self.girl.happiness

    def get_compatibility(self):
        """
        Calculates compatibility of the couple
        :return:
        """
        compat_intell = abs(self.boy.intelligence - self.girl.intelligence)
        compat_attract = abs(self.boy.attractiveness - self.girl.attractiveness)
        compat_budget = self.boy.budget - self.girl.budget
        return compat_intell + compat_attract + compat_budget

