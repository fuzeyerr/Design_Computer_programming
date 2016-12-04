from __future__ import division
import string, re, itertools, time



def solve(formula):
    """"Given a formula like 'ODD + ODD = EVEN', fill in digits
      to solve it. Input formula is a string; out put is a digit-filled- in string or None"""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    """"Generate all possible fillings-in of letter in formula with
     digits"""
    letters = ''.join(set(re.findall('[A-Z]',formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """ Formula f is valid if it has no numbers with leading zero, and evals  """
    try:
        return not re.search(r'\b[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N ++ C**N and N > 1

"""

def timedcalls(n, fn, *args):
    if isinstance(n, (int,long)):
        times = [timedcalls(fn,*args)[0] for _ in range(n)]

    else:
        total, times = 0, []
        while total <= n:
            time = timedcalls(fn, *args)[0]
            times.append(time)
            total += time

    return min(times), average(times), max(times)





def test():
    t0 = time.clock()
    for example in examples:
        print; pring 13*'', example
        print '%6.4f sed:  %s ' % timedcall(solve,example)
