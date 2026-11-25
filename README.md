# pairwise-audio-edit-crossfade

## 领域

游戏、图形与多媒体

## 主题

音频剪切交叉淡化

## 说明

过零吸附、等功率曲线与引用去重。

初始状态下 `media/audio_edit_crossfade.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
