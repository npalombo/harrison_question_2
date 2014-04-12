__author__ = 'nick'


def minimum_x(_x):
    """
    - returns a decorator that can be used to decorate another function
    - verifies argument of the function it decorates <= the given value
    - raises a ValueError on failure.
    """
    def wrap(_func):
        def minimum_x_wrapper(x):
            if _x <= x:
                return _func(x)
            else:
                raise ValueError("%s must be less or equal to than %s" % (x, _x))
        return minimum_x_wrapper

    return wrap
