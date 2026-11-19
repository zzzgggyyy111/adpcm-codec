"""ADPCM：量化、反量化与步长：待实现的核心模块。"""


def step_for(index, table):
    """步长索引。"""
    raise NotImplementedError

def quantize(sample, step):
    """量化。"""
    raise NotImplementedError

def dequantize(code, step):
    """反量化。"""
    raise NotImplementedError

def encode(samples, step):
    """编码。"""
    raise NotImplementedError

def decode(codes, step):
    """解码。"""
    raise NotImplementedError
