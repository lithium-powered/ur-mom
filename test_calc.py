import pytest
from dataclasses import dataclass
from calc import calc


@pytest.mark.parametrize("expression_input,expression_output,expect_throw", 
    [
        pytest.param("0", 0, False, id="basic_expression"),
        pytest.param("-1", -1, False, id="basic_expression"),
        pytest.param("4 + 5", 9, False, id="addition"),
        pytest.param("-10 + -10", -20, False, id="addition"),
        pytest.param("4 * 5", 20, False, id="multiplication"),
        pytest.param("4 * 0", 0, False, id="multiplication"),
        pytest.param("4 * -10", -40, False, id="multiplication"),
        pytest.param("4 - 5", -1, False, id="subtraction"),
        pytest.param("5 - 4", 1, False, id="subtraction"),
        pytest.param("5 / 3", 1, False, id="division"),
        pytest.param("5/3", 1, False, id="division"),
        pytest.param("(10)", 10, False, id="parens"),
        pytest.param("(-10)", -10, False, id="parens"),
        pytest.param("-(10)", 10, False, id="parens"),
        pytest.param("(10) - (10)", 0, False, id="parens"),
        pytest.param("((10)) + 4", 14, False, id="parens"),
        pytest.param("(10 - 10) * 40", 0, False, id="parens"),
        pytest.param("four - 10", -6, False, id="parens"),
        pytest.param("four + five", 9, False, id="parens"),
        pytest.param("four + five", 9, False, id="parens"),
        pytest.param("IV - I", 3, False, id="roman numerals"),
        pytest.param("iv - i", 3, False, id="roman numerals"),
        pytest.param("iv - i", 3, False, id="roman numerals"),
    ]
)
def test_eval(expression_input: str, expression_output: int, expect_throw: bool):
    try:
        output: int = calc(expression_input)
    except:
        assert expect_throw
    else:
        assert output == expression_output