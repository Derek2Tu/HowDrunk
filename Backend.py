__author__ = 'Derek'

class Alcoholic():
    def __init__(self, name, weight, gender, standard_drinks, hours):
                self._name = name
                self._weight = weight
                self._gender = gender
                self._standard_drinks = standard_drinks
                self._hours = hours

    def __str__(self):
                return "My name is " + self._name + "and I drank " + self._standard_drinks + \
                       "servings of alcohol in " + self._hours + " hours."

    def calc_bac(self):
                bac = (self._standard_drinks * 0.06 * 100 * (1.055 / self._weight) * self._gender)\
                      - (0.015 * self._hours)
                return bac

    def

