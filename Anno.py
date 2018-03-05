import math


class Anno():
    bread = 0
    beer = 0
    linen = 0
    leather = 0
    books = 0
    candle_sticks = 0
    meat = 0
    wine = 0
    fur_coats = 0
    glasses = 0
    robes = 0
    dates = 0
    milk = 0
    carpets = 0
    coffee = 0
    pearl_necklaces = 0
    perfume = 0
    marzipan = 0

    def __init__(self, beggars, peasants, citizens, patritians, noblemen, nomads, envoys):
        self.beggars = beggars
        self.peasants = peasants * 8
        self.citizens = citizens * 15
        self.patritians = patritians * 25
        self.noblemen = noblemen * 40
        self.nomads = nomads * 15
        self.envoys = envoys * 25

    # def fish(self) is a method or a function inside a class
    def fish(self, item):
        if item == 1:
            print("\n" + str(math.ceil((self.beggars * 0.007 / 2.5)
                                       + (self.peasants * 0.01 / 2.5) +
                                       (self.citizens * 0.004 / 2.5) +
                                       (self.patritians * 0.0022 / 2.5) +
                                       (self.noblemen * 0.0016 / 2.5))) + " fish")

        elif item == 2:
            print("\n" + str(math.ceil((self.beggars * 0.007 / 3)
                                       + (self.peasants * 0.01 / 3) +
                                       (self.citizens * 0.004 / 3) +
                                       (self.patritians * 0.0022 / 3) +
                                       (self.noblemen * 0.0016 / 3))) + " fish")

        elif item == 3:
            print("\n" + str(math.ceil((self.beggars * 0.007 / 3.5)
                                       + (self.peasants * 0.01 / 3.5) +
                                       (self.citizens * 0.004 / 3.5) +
                                       (self.patritians * 0.0022 / 3.5) +
                                       (self.noblemen * 0.0016 / 3.5))) + " fish")

        else:
            print("\n" + str(math.ceil((self.beggars * 0.007 / 2)
                                       + (self.peasants * 0.01 / 2) +
                                       (self.citizens * 0.004 / 2) +
                                       (self.patritians * 0.0022 / 2) +
                                       (self.noblemen * 0.0016 / 2))) + " fish")

    def cider(self, item):
        if item == 1:
            print(str(math.ceil((self.beggars * 0.003 / 1.875) + (self.peasants
                                                                  * 0.0044 / 1.875) + (
                                self.citizens * 0.0044 / 1.875) + (
                                    self.patritians * 0.0023 / 1.875) + (
                                    self.noblemen * 0.0013 / 1.875))) + " cider")

        elif item == 2:
            print(str(math.ceil((self.beggars * 0.003 / 2.25) + (self.peasants
                                                                 * 0.0044 / 2.25) + (self.citizens * 0.0044 / 2.25) + (
                                    self.patritians * 0.0023 / 2.25) + (
                                    self.noblemen * 0.0013 / 2.25))) + " cider")

        elif item == 3:
            print(str(math.ceil((self.beggars * 0.003 / 2.625) + (self.peasants
                                                                  * 0.0044 / 2.625) + (
                                self.citizens * 0.0044 / 2.625) + (
                                    self.patritians * 0.0023 / 2.625) + (
                                    self.noblemen * 0.0013 / 2.625))) + " cider")
        else:
            print(str(math.ceil((self.beggars * 0.003 / 1.5) + (self.peasants
                                                                * 0.0044 / 1.5) + (self.citizens * 0.0044 / 1.5) + (
                                    self.patritians * 0.0023 / 1.5) + (
                                    self.noblemen * 0.0013 / 1.5))) + " cider")

    def spice(self, item):
        if item == 1:
            print(str(math.ceil((self.citizens * 0.004 / 2.5) + (
                self.patritians * 0.0022 / 2.5) + (
                                    self.noblemen * 0.0016 / 2.5))) + " spice")

        elif item == 2:
            print(str(math.ceil((self.citizens * 0.004 / 3) + (
                self.patritians * 0.0022 / 3) + (
                                    self.noblemen * 0.0016 / 3))) + " spice")

        elif item == 3:
            print(str(math.ceil((self.citizens * 0.004 / 3.5) + (
                self.patritians * 0.0022 / 3.5) + (
                                    self.noblemen * 0.0016 / 3.5))) + " spice")

        else:
            print(str(math.ceil((self.citizens * 0.004 / 2) + (
                self.patritians * 0.0022 / 2) + (
                                    self.noblemen * 0.0016 / 2))) + " spice")

    def linen(self, item):
        global linen
        if item == 1:
            linen = math.ceil((self.citizens * 0.0042 / 2.5) + (
                self.patritians * 0.0019 / 2.5) + (
                                  self.noblemen * 0.0008 / 2.5))

        elif item == 2:
            linen = math.ceil((self.citizens * 0.0042 / 3) + (
                self.patritians * 0.0019 / 3) + (
                                  self.noblemen * 0.0008 / 3))

        elif item == 3:
            linen = math.ceil((self.citizens * 0.0042 / 3.5) + (
                self.patritians * 0.0019 / 3.5) + (
                                  self.noblemen * 0.0008 / 3.5))

        else:
            linen = math.ceil((self.citizens * 0.0042 / 2) + (
                self.patritians * 0.0019 / 2) + (
                                  self.noblemen * 0.0008 / 2))

        print(str(linen) + " linen garments")
        print("    " + str(linen * 2) + " hemp")

    def bread(self, item):
        global bread
        if item == 1:
            bread = math.ceil((self.patritians * 0.0055 / 5) + (self.noblemen *
                                                                0.0039 / 5))

        elif item == 2:
            bread = math.ceil((self.patritians * 0.0055 / 6) + (self.noblemen *
                                                                0.0039 / 6))

        elif item == 3:
            bread = math.ceil((self.patritians * 0.0055 / 7) + (self.noblemen *
                                                                0.0039 / 7))

        else:
            bread = math.ceil((self.patritians * 0.0055 / 4) + (self.noblemen *
                                                                0.0039 / 4))
        print(str(bread) + " bread")
        print("    " + str(bread) + " flour")
        print("        " + str(bread * 2) + " wheat")

    def beer(self, item):
        global beer
        if item == 1:
            beer = math.ceil((self.patritians * 0.0024 / 1.875) +
                             (self.noblemen * 0.0014 / 1.875))

        elif item == 2:
            beer = math.ceil((self.patritians * 0.0024 / 2.25) +
                             (self.noblemen * 0.0014 / 2.25))

        elif item == 3:
            beer = math.ceil((self.patritians * 0.0024 / 2.625) +
                             (self.noblemen * 0.0014 / 2.625))

        else:
            beer = math.ceil((self.patritians * 0.0024 / 1.5) +
                             (self.noblemen * 0.0014 / 1.5))
        print(str(beer) + " beer")
        print("    " + str(beer) + " herbs")
        print("    " + str(beer) + " wheat")

    def leather(self, item):
        global leather
        if item == 1:
            leather = math.ceil((self.patritians * 0.0028 / 5) +
                                (self.noblemen * 0.0016 / 5))

        elif item == 2:
            leather = math.ceil((self.patritians * 0.0028 / 6) +
                                (self.noblemen * 0.0016 / 6))

        elif item == 3:
            leather = math.ceil((self.patritians * 0.0028 / 7) +
                                (self.noblemen * 0.0016 / 7))

        else:
            leather = math.ceil((self.patritians * 0.0028 / 4) +
                                (self.noblemen * 0.0016 / 4))
        print(str(leather) + " leather")
        print("    " + str(math.ceil(leather * 2)) + " animal hides")
        print("    " + str(math.ceil(leather / 2)) + " salt")
        print("        " + str(math.ceil(leather / 2)) + " brine")
        print("        " + str(math.ceil(leather / 2)) + " coal")

    def books(self, item):
        global books
        if item == 1:
            books = math.ceil((self.patritians * 0.0016 / 3.75) +
                              (self.noblemen * 0.0009 / 3.75))

        elif item == 2:
            books = math.ceil((self.patritians * 0.0016 / 4.5) +
                              (self.noblemen * 0.0009 / 4.5))

        elif item == 3:
            books = math.ceil((self.patritians * 0.0016 / 5.25) +
                              (self.noblemen * 0.0009 / 5.25))

        else:
            books = math.ceil((self.patritians * 0.0016 / 3) +
                              (self.noblemen * 0.0009 / 3))
        print(str(books) + " books")
        print("    " + str(math.ceil(books * 2)) + " indego")
        print("    " + str(math.ceil(books / 2)) + " paper")
        print("        " + str(math.ceil(books)) + " wood")

    def candle_sticks(self, item):
        global candle_sticks
        if item == 1:
            candle_sticks = math.ceil((self.patritians * 0.0008 / 2.5) +
                                      (self.noblemen * 0.0006 / 2.5))

        elif item == 2:
            candle_sticks = math.ceil((self.patritians * 0.0008 / 3) +
                                      (self.noblemen * 0.0006 / 3))

        elif item == 3:
            candle_sticks = math.ceil((self.patritians * 0.0008 / 3.5) +
                                      (self.noblemen * 0.0006 / 3.5))

        else:
            candle_sticks = math.ceil((self.patritians * 0.0008 / 2) +
                                      (self.noblemen * 0.0006 / 2))
        print(str(candle_sticks) + " candle sticks")
        print("    " + str(math.ceil(candle_sticks * 1.5)) + " candles")
        print("        " + str(math.ceil(candle_sticks * 3)) + " beeswax")
        print("        " + str(math.ceil(candle_sticks * 1.5)) + " hemp")
        print("    " + str(math.ceil(candle_sticks * 0.75)) + " brass")
        print("        " + str(math.ceil(candle_sticks * 0.75)) +
              " copper ore")
        print("        " + str(math.ceil(candle_sticks / 2)) + " coal")

    def meat(self, item):
        global meat
        if item == 1:
            meat = math.ceil((self.noblemen * 0.0022 / 3.125))

        elif item == 2:
            meat = math.ceil((self.noblemen * 0.0022 / 3.75))

        elif item == 3:
            meat = math.ceil((self.noblemen * 0.0022 / 4.375))

        else:
            meat = math.ceil((self.noblemen * 0.0022 / 2.5))
        print(str(meat) + " meat")
        print("    " + str(math.ceil(meat * 2)) + " cows")
        print("    " + str(math.ceil(meat * 0.48)) + " salt")
        print("        " + str(math.ceil(meat * 0.48)) + " brine")
        print("        " + str(math.ceil(meat * 0.48)) + " coal")

    def wine(self, item):
        global wine
        if item == 1:
            wine = math.ceil((self.noblemen * 0.002 / 2.5))

        elif item == 2:
            wine = math.ceil((self.noblemen * 0.002 / 3))

        elif item == 3:
            wine = math.ceil((self.noblemen * 0.002 / 3.5))

        else:
            wine = math.ceil((self.noblemen * 0.002 / 2))
        print(str(wine) + " wine")
        print("    " + str(math.ceil(wine * 3)) + " grapes")
        print("    " + str(math.ceil(wine)) + " barrels")
        print("        " + str(math.ceil(wine * 2 / 3)) + " wood")
        print("        " + str(math.ceil(wine / 2)) + " iron")
        print("            " + str(math.ceil(wine / 2)) + " iron ore")
        print("            " + str(math.ceil(wine / 2)) + " coal")

    def fur_coats(self, item):
        global fur_coats
        if item == 1:
            fur_coats = math.ceil((self.noblemen * 0.0016 / 3.125))

        elif item == 2:
            fur_coats = math.ceil((self.noblemen * 0.0016 / 3.75))

        elif item == 3:
            fur_coats = math.ceil((self.noblemen * 0.0016 / 4.375))

        else:
            fur_coats = math.ceil((self.noblemen * 0.0016 / 2.5))
        print(str(fur_coats) + " fur coats")
        print("    " + str(math.ceil(fur_coats)) + " fur")
        print("    " + str(math.ceil(fur_coats * 1 / 3)) + " salt")
        print("        " + str(math.ceil(fur_coats * 1 / 3)) + " brine")
        print("        " + str(math.ceil(fur_coats * 1 / 3)) + " coal")

    def glasses(self, item):
        global glasses
        if item == 1:
            glasses = math.ceil((self.noblemen * 0.00117 / 2.5))

        elif item == 2:
            glasses = math.ceil((self.noblemen * 0.00117 / 3))

        elif item == 3:
            glasses = math.ceil((self.noblemen * 0.00117 / 3.5))

        else:
            glasses = math.ceil((self.noblemen * 0.00117 / 2))
        print(str(glasses) + " glasses")
        print("    " + str(math.ceil(glasses * 0.75)) + " quartz")
        print("    " + str(math.ceil(glasses * 0.75)) + " brass")
        print("        " + str(math.ceil(glasses * 0.75)) + " copper ore")
        print("        " + str(math.ceil(glasses / 2)) + " coal")

    def robes(self, item):
        global robes
        if item == 1:
            robes = math.ceil((self.noblemen * 0.00142 / 3.75))

        elif item == 2:
            robes = math.ceil((self.noblemen * 0.00142 / 4.5))

        elif item == 3:
            robes = math.ceil((self.noblemen * 0.00142 / 5.25))

        else:
            robes = math.ceil((self.noblemen * 0.00142 / 3))
        print(str(robes) + " robes")
        print("    " + str(math.ceil(robes * 2)) + " silk")
        print("    " + str(math.ceil(robes)) + " gold")
        print("        " + str(math.ceil(robes)) + " gold ore")
        print("        " + str(math.ceil(robes * 0.75)) + " coal")

    def dates(self, item):
        global dates
        if item == 1:
            dates = math.ceil((self.nomads * 0.00666 / 3.75) + (self.envoys * .005 / 3.75))

        elif item == 2:
            dates = math.ceil((self.nomads * 0.00666 / 4.5) + (self.envoys * .005 / 4.5))

        elif item == 3:
            dates = math.ceil((self.nomads * 0.00666 / 5.25) + (self.envoys * .005 / 5.25))

        else:
            dates = math.ceil((self.nomads * 0.00666 / 3) + (self.envoys * .005 / 3))
        print(str(dates) + " dates")

    def milk(self, item):
        global dates
        if item == 1:
            milk = math.ceil((self.nomads * 0.00344 / 1.875) + (self.envoys * .00225 / 1.875))

        elif item == 2:
            milk = math.ceil((self.nomads * 0.00344 / 2.25) + (self.envoys * .00225 / 2.25))

        elif item == 3:
            milk = math.ceil((self.nomads * 0.00344 / 2.625) + (self.envoys * .00225 / 2.625))

        else:
            milk = math.ceil((self.nomads * 0.00344 / 1.5) + (self.envoys * .00225 / 1.5))
        print(str(milk) + " milk")

    def carpets(self, item):
        global dates
        if item == 1:
            carpets = math.ceil((self.nomads * 0.00165 / 1.875) + (self.envoys * .001 / 1.875))

        elif item == 2:
            carpets = math.ceil((self.nomads * 0.00165 / 2.25) + (self.envoys * .001 / 2.25))

        elif item == 3:
            carpets = math.ceil((self.nomads * 0.00165 / 2.625) + (self.envoys * .001 / 2.625))

        else:
            carpets = math.ceil((self.nomads * 0.00165 / 1.5) + (self.envoys * .001 / 1.5))
        print(str(carpets) + " carpets")
        print("    " + str(math.ceil(carpets)) + " silk")
        print("    " + str(math.ceil(carpets)) + " indigo")

    def coffee(self, item):
        global coffee
        if item == 1:
            coffee = math.ceil((self.envoys * 0.001 / 1.25))

        elif item == 2:
            coffee = math.ceil((self.envoys * 0.001 / 1.5))

        elif item == 3:
            coffee = math.ceil((self.envoys * 0.001 / 1.75))

        else:
            coffee = math.ceil((self.envoys * 0.001))
        print(str(coffee) + " coffee")
        print("    " + str(math.ceil(coffee * 2)) + " coffee beans")

    def pearl_necklaces(self, item):
        global pearl_necklaces
        if item == 1:
            pearl_necklaces = math.ceil((self.envoys * 0.00133 / 1.25))

        elif item == 2:
            pearl_necklaces = math.ceil((self.envoys * 0.00133 / 1.5))

        elif item == 3:
            pearl_necklaces = math.ceil((self.envoys * 0.00133 / 1.75))

        else:
            pearl_necklaces = math.ceil((self.envoys * 0.00133))
        print(str(pearl_necklaces) + " pearl_necklaces")
        print("    " + str(math.ceil(pearl_necklaces)) + " pearls")

    def perfume(self, item):
        global perfume
        if item == 1:
            perfume = math.ceil((self.envoys * 0.0008 / 1.25))

        elif item == 2:
            perfume = math.ceil((self.envoys * 0.0008 / 1.5))

        elif item == 3:
            perfume = math.ceil((self.envoys * 0.0008 / 1.75))

        else:
            perfume = math.ceil((self.envoys * 0.0008))
        print(str(perfume) + " perfume")
        print("    " + str(math.ceil(perfume * 3)) + " roses")

    def marzipan(self, item):
        global marzipan
        if item == 1:
            marzipan = math.ceil((self.envoys * 0.00163 / 5))

        elif item == 2:
            marzipan = math.ceil((self.envoys * 0.00163 / 6))

        elif item == 3:
            marzipan = math.ceil((self.envoys * 0.00163 / 7))

        else:
            marzipan = math.ceil((self.envoys * 0.00163 / 4))
        print(str(marzipan) + " marzipan")
        print("    " + str(math.ceil(marzipan * 2)) + " almonds")
        print("    " + str(math.ceil(marzipan)) + " sugar")
        print("        " + str(math.ceil(marzipan * 2)) + " sugar cane")

"""Replace the 0s in my_game = Anno(0, 0, 0, 0, 0, 0) with the total number of beggars (individual beggars not houses)
and the number of peasant, citizen, patrician, nobleman, nomads, and envoy houses."""

my_game = Anno(0, 0, 0, 0, 0, 0, 0)

""" Replace the 0s with the number of productivity items you have for each of the resources. Ex. If you have 2 items
that increase the productivity of the fishing hut, then replace the 0 with 2."""

my_game.fish(0)
my_game.cider(0)
my_game.spice(0)
my_game.linen(0)
my_game.bread(0)
my_game.beer(0)
my_game.leather(0)
my_game.books(0)
my_game.candle_sticks(0)
my_game.meat(0)
my_game.wine(0)
my_game.fur_coats(0)
my_game.glasses(0)
my_game.robes(0)
my_game.dates(0)
my_game.milk(0)
my_game.carpets(0)
my_game.coffee(0)
my_game.pearl_necklaces(0)
my_game.perfume(0)
my_game.marzipan(0)

# Prints the total amounts needed
print("\nTotals:")
print(str(math.ceil(books + (wine * 2 / 3))) + " wood")
print(str(math.ceil(beer + (bread * 2))) + " wheat")
print(str(math.ceil((meat * 0.48) + (fur_coats * 1 / 3) + (leather / 2))) +
      " salt")
print(str(math.ceil((meat * 0.48) + (fur_coats * 1 / 3) + (leather / 2) +
                    (candle_sticks / 2) + (wine / 2) + (glasses / 2) + (robes * 0.75))) +
      " coal")
print(str(math.ceil((linen * 2) + (candle_sticks * 1.5))) + " hemp")
print(str(math.ceil((glasses * 0.75) + (candle_sticks * 0.75))) + " brass")
