import logging
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S', level=logging.DEBUG)


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
        self.luxury_given = False
        self.utility_given = False
        self.essential_given = False
        self.allocate_gifts(gift_list)
        self.set_happiness()
        self.compatibility = self.get_compatibility()


    def __str__(self):
        return str(self.boy.name + ' and ' + self.girl.name)

    def allocate_gifts(self, gift_list):
        """
        Allocates gift from given gift lisr
        :param gift_list: list of gift objects
        :return:
        """
        for gift in gift_list:
            if gift.__class__.__name__ == 'LuxuryGift' and not self.luxury_given:
                self.luxury_given = True
                self.girl.luxury_gift_cost += gift.price
                self.gifts.append(gift)
                self.girl.gift_cost += gift.price
                self.girl.gift_value += gift.value
                print(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
                logging.info(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
            elif gift.__class__.__name__ == 'EssentialGift' and not self.essential_given:
                self.essential_given = True
                self.gifts.append(gift)
                self.girl.gift_cost += gift.price
                self.girl.gift_value += gift.value
                print(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
                logging.info(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
            elif gift.__class__.__name__ == 'UtilityGift' and not self.utility_given:
                self.utility_given = True
                self.gifts.append(gift)
                self.girl.gift_cost += gift.price
                self.girl.gift_value += gift.value
                print(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
                logging.info(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
            elif (type(self.boy).__name__ == 'MiserBoy' or 'GeekBoy') and self.girl.gift_cost < self.girl.budget:
                if gift.__class__.__name__ == 'LuxuryGift':
                    self.girl.luxury_gift_cost += gift.price
                self.gifts.append(gift)
                self.girl.gift_cost += gift.price
                self.girl.gift_value += gift.value
                print(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
                logging.info(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
            elif type(self.boy).__name__ == 'GenerousBoy' and self.girl.gift_cost < self.boy.budget:
                if gift.__class__.__name__ == 'LuxuryGift':
                    self.girl.luxury_gift_cost += gift.price
                self.gifts.append(gift)
                self.girl.gift_cost += gift.price
                self.girl.gift_value += gift.value
                print(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')
                logging.info(self.boy.name + ' gifted ' + self.girl.name + ' with ' + gift.name + 'gift')

    def set_happiness(self):
        """
        Calculates boy's and girl's happiness individually and adds it.
        :return:
        """
        self.happiness = self.boy.get_happiness(girlfriend=self.girl) + self.girl.get_happiness()

    def get_compatibility(self):
        """
        Calculates compatibility of the couple
        :return:
        """
        compat_intell = abs(self.boy.intelligence - self.girl.intelligence)
        compat_attract = abs(self.boy.attractiveness - self.girl.attractiveness)
        compat_budget = self.boy.budget - self.girl.budget
        return compat_intell + compat_attract + compat_budget

    def breakup(self):
        if self.boy.single == 0 and self.girl.single == 0:
            self.girl.change_commitment()
            self.boy.change_commitment()
            logging.info(self.boy.name + ' broke up with ' + self.girl.name)
            print(self.boy.name + ' broke up with ' + self.girl.name)
            return True
        return False

