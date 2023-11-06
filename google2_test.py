import pytest
from google2 import solution

# Test cases
@pytest.mark.parametrize("input, expected", [
    ([2, -3, 1, 0, -5], "30"),
    ([0, 0, 0, 0, 0], "0"),
    ([0, 0, -1, 0, 0], "0"),
    ([-1, 0, -1, 0, -1], "1"),
    ([2, 3, 1, 4], "24"),
    ([-2, -3, -1, -4], "24"),
    ([2, -3, 1, -4], "24"),
    ([2, -3, 1, 0, -4], "24"),
    ([5], "5"),
    ([1000, -500, 999, -1000, 998], "498501000000000"),
    ([1] * 50, "1"),
    ([-1000] * 50, str(1000**50)),
    ([-1000] * 25 + [1000] * 25, str(1000**25*1000**24))
])
def test_solution(input, expected):
    result = solution(input)
    assert result == expected

if __name__ == '__main__':
    pytest.main()