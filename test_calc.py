import pytest
from dataclasses import dataclass
from calc import calc


@pytest.mark.parametrize("expression_input,expression_output,expect_throw", 
    [
        pytest.param("0", 0, False, id="basic_expression")
    ]
)
def test_eval(expression_input: str, expression_output: int, expect_throw: bool):
    try:
        output: int = calc(expression_input)
    except:
        assert expect_throw
    else:
        assert output == expression_output