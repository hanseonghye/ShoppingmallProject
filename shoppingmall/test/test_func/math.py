def abs(x):
    return x if x >= 0 else -x


def inc(x):
    return x + 1


def abs_sum(*argv):
    return sum(abs(x) for x in argv)


def abs_inc_sum(*argv):
    return sum(inc(abs(x) for x in argv))
