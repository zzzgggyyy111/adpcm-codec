import pytest

from codec import adpcm as mod

CASES = [
    ('step_for', [0, [16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66]], 16, False),
    ('step_for', [99, [16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66]], 66, False),
    ('quantize', [100, 16], 6, False),
    ('quantize', [-100, 16], -6, False),
    ('dequantize', [2, 16], 32, False),
    ('encode', [[16, -32], 16], [1, -2], False),
    ('decode', [[1, -2], 16], [16, -32], False),
    ('encode', [[], 16], [], False),
    ('step_for', [-1, [16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66]], 16, False),
    ('quantize', [0, 16], 0, False),
    ('quantize', [1000, 16], 7, False),
    ('dequantize', [-8, 16], -128, False),
    ('encode', [[], 16], [], False),
    ('decode', [[], 16], [], False),
    ('decode', [[7], 16], [112], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_adpcm_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
