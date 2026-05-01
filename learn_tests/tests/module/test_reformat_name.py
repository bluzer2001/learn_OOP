from src.functions import reformat_name
import pytest


@pytest.mark.parametrize('input_name, result_name', [
    ('mark ', 'Mark'),
    (' Mike', 'Mike'),
    ('Harry', 'Harry')
])
def test_reformat_name(input_name, result_name):
    assert reformat_name(input_name) == result_name
