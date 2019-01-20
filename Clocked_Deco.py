"""
A decorator to get the time elapsed during runtime
how to use it:
    import Clocked_Deco

    @Clocked_Deco.clock
    def theFunctionYouWantToClock():
        ...
        ...
        
"""

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter()-t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
