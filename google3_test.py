import pytest
from google3 import solution

# Test cases
@pytest.mark.parametrize("input, expected", [
    ("--->-><-><-->-", 10),
    (">----<", 2),
    ("<<>><", 4),
])
def test_solution(input, expected):
    result = solution(input)
    assert result == expected

if __name__ == '__main__':
    pytest.main()