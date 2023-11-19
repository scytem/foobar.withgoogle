import pytest
from google4 import solution

# Test cases
@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3, 4, 5, 6], 3),
    ([], 0),
    ([1, 1, 1], 1),
])
def test_solution(input, expected):
    result = solution(input)
    assert result == expected

if __name__ == '__main__':
    pytest.main()