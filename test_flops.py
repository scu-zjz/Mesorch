from fvcore.nn import FlopCountAnalysis, flop_count_table
from mesorch import MesorchFull
import torch

model = MesorchFull()
model.eval()

# 构造输入
x = torch.randn(1, 3, 512, 512)
mask = torch.randn(1, 1, 512, 512)

# 计算 FLOPs
flops = FlopCountAnalysis(model, (x, mask))

print(flop_count_table(flops))