import random

def poker(hands):
    """Return the best hand: poker([hand,...]) => hand"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable """
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
        return result


def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks



# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    """Shuffle the deck """
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

print(deal(8))




def hand_rank(hand):
    """return a value indicating the ranking of a hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(r, ranks):
        return (7, kind(4,ranks), kind(1,ranks))
    elif flush(hand):
        return (5,ranks)
    elif straight(ranks):
        return (4,max(ranks))
    elif kind(3,ranks):
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):
        return (3, two_pair(ranks),ranks)
    elif kind(2,ranks):
        return (1,kind(2,ranks),ranks)
    else:
        return (0,ranks)




def straight(ranks):
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


sf = "6C 7C 8C 9C TC".split()  # Straight Flush
fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
fh = "TD TC TH 7C 7D".split()  # Full House

print(flush(sf))
print(card_ranks(sf))


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


two_pair([3,3,1,7,7])

def hand_percentages(n=700*1000):
    """sample n random hands and print a table of percentages for each type of hand"""
    counts = [0] * 9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        hand_names = {8: "straight flush", 7: "four of a kind", 6: "full house",
                          5: " flush ", 4: " straight ", 3: " three of a kind ",
                          2: " two pair ", 1: " a pair ", 0: " high card "}
        print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)

    # %of the first character at the head of the string is the special quotation that means formating the string
    # %14s means max 14 characters of string , and %6.3f means max 6 digit and 3 precision, %% means % (escape) last % is the
    # statement of the formating.

hand_percentages()


def test():
    """test cases for the funcitons in poker program"""
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert straight([9,8,7,6,5]) == True
    assert straight([9,4,2,4,2]) == False

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8,10)
    assert hand_rank()
