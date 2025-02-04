import pytest

def main():
    x=.2
    y=.1
    z=x+y
    assert z == pytest.approx(.3)
    print(z)

main()