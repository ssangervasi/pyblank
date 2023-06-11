from main import main

def test_main():
    assert main() == 'Blank'


def test_fail():
    breakpoint()
    raise Exception('fail')



def test_breakpoint():
    breakpoint()
