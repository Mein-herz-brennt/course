import sys


def key_params(fun):
    def _params(*args, **kwargs):
        if len(args) > 0:
            sys.exit()
        else:
            fun(**kwargs)

    return _params


@key_params
def function(b=2, a=10, c=10):
    print(a * b * c)


function(a=1, b=2, c=5)
