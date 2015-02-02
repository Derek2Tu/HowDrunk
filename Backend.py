__author__ = 'Derek'

class Alcoholic():
    def __init__(self, name, weight, standard_drinks, hours, gender):
                self._name = name
                self._weight = weight
                self._gender = gender
                self._standard_drinks = standard_drinks
                self._hours = hours

    def __str__(self):
                return "My name is " + self._name + "and I drank " + self._standard_drinks + \
                       "servings of alcohol in " + self._hours + " hours."

    def calc_bac(self):
                if self._gender == "Male":
                    gender_value = 0.68
                else:
                    gender_value = 0.55

                bac = (float(self._standard_drinks) * 0.06 * 100 * (1.055 / float(self._weight)) * gender_value)\
                      - (0.015 * float(self._hours))
                return "Your blood alcohol content is " + str(bac)



