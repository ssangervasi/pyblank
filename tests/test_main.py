def test_fail():
    breakpoint()
    raise Exception('fail')


def test_breakpoint():
    breakpoint()
