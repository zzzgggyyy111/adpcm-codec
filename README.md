# ADPCM：量化、反量化与步长

音频压缩后底噪大、解码波形偏移：量化没有按步长取整，量化越界没有钳制，反量化符号错，步长索引越界，编解码长度不一致，空输入崩，批量编码只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
codec/__init__.py
codec/adpcm.py
tests/test_adpcm.py
```

## 当前状态

`codec/adpcm.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_adpcm.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 量化按步长取整
2. 量化钳制范围
3. 反量化符号
4. 步长索引钳制
5. 编解码长度一致
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `codec/adpcm.py`
后 15 条用例应全部通过。
