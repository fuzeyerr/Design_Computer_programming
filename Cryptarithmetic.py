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
ATOM**0.5 == A + TO + M
GLITTERS is not GLOD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R ** 3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def timedcall(fn, *args):
    """ Call function with args; return the time in seconds adn result """
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result


def average(numbers):
    """ Return the average (arithmetic mean) of a sequence of numbers  """
    return sum(numbers) / float(len(numbers))


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcalls(fn,*args)[0] for _ in range(n)]

    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def compile_formula(formula, verbose=False):
    """Compile formula into a function Also return letters found, as a str,
    in same order as params of function For example, 'YOU == ME**2' returns
    (lambda Y,M,E,U,O): (U+10*0+100*Y) == (E+10*M)**2, 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        tests = ' and '.join(L+'!=0' for L in firstletters)
        body = '%s and (%s)' % (tests, body)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters


def faster_solve(formula):
    """"Given a formula like 'ODD + ODD = EVEN', fill in digits
      to solve it. Input formula is a string; out put is a digit-filled- in string or None"""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def test():
    t0 = time.clock()
    for example in examples:
        print 13*'', example
        print '%6.4f sed:  %s ' % timedcall(faster_solve, example)

print(faster_solve('YOU == ME**2'))

print test()

print(set([6315237]))