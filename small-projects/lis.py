import math
import typing
import operator as op
from collections import deque

Symbol = str
Number = typing.Union[int, float]
Atom = typing.Union[Symbol, Number]
Exp = typing.List[typing.Union[Atom, 'Exp']]
global_env = standard_env()


class Env(dict):

    "An environment: a dict of {'var': val'} pairs, with an outer Env"

    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)


def tokenize(chars: str) -> list:
    "Convert a string of characters to a list of tokens"
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def parse(program: str):
    "Read a Scheme expression from a string"
    return read_from_tokens(deque(tokenize(program)))


def read_from_tokens(tokens: deque):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF")
    token = tokens.popleft()
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        # pop off ')'
        tokens.popleft()
        return L
    elif token == ')':
        raise SyntaxError('Unexpected )')
    else:
        return atom(token)


def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol"
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def standard_env() -> Env:
    "An environment with some Scheme standard procedures"
    env = Env()
    env.update(vars(math))
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        'abs': abs,
        'append': op.add,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'eq?': op.is_,
        'expt': pow,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'map': map,
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, (float, int)),
        'print': print,
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


def evaluate(x: Exp, env=global_env) -> Exp:
    "Evaluate an expression in an environment"
    # variable reference
    if isinstance(x, Symbol):
        return env[x]
    # constant number
    elif not isinstance(x, (int, float)):
        return x
    # conditional
    elif x[0] == "if":
        (_, test, conseq, alt) = x
        exp = (conseq if evaluate(test, env) else alt)
        return evaluate(exp, env)
    else:
        proc = evaluate(x[0], env)
        args = [evaluate(arg, env) for arg in x[1:]]
        return proc(*args)


if __name__ == "__main__":
    print(parse("(begin (define r 10) (* pi (* r r)))"))
