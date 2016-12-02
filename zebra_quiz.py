import itertools


def imright(h1, h2):
    h1 - h2 == 1


def nextto(h1, h2):
    abs(h1 - h2) == 1


def zebra_puzzle():
    """Return a tuple (water, zebra) indicating their house numbers"""
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((water, zebra)
                for (red, green, ivory, yellow, blue) in orderings
                for (Englishman, Spaniard, Ukranian, Japanese, Norweigian) in orderings
                for (dog, snails, fox, horse, zebra) in orderings
                for (coffee, tea, milk, oj, water) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Englishman is red
                if Spaniard is dog
                if coffee is green
                if Ukranian is tea
                if imright(green, ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if Norweigian is first
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                if LuckyStrike is oj
                if Japanese is Parliaments
                if nextto(Norweigian, blue)
                )


def zebra_puzzle2():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


print zebra_puzzle2()
