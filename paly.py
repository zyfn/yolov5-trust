from tkinter import ANCHOR
import torch
import numpy as np
# a=torch.randn((1,5),device='cuda',requires_grad=True)
# a=torch.tensor([-10,-1,-0.1,0.,0.1,1,20.])
# print(a)
# softPlus = torch.nn.Softplus(beta=50,threshold=0)
# evidence = softPlus(a)
# print(evidence)

import torch.nn as nn
# cls_convs = nn.ModuleList()
# reg_convs = nn.ModuleList()
# m = nn.ModuleList()
# cls_convs.append(
#     nn.Sequential(
#         *[
#             nn.Conv2d(
#                 in_channels=int(256),
#                 out_channels=int(256),
#                 kernel_size=3,
#                 stride=1,
#             ),
#             nn.Conv2d(
#                 in_channels=int(256),
#                 out_channels=int(256),
#                 kernel_size=3,
#                 stride=1,
#                         ),
#                     ]
#                 )
#             )
# reg_convs.append(
#     nn.Sequential(
#         *[
#             nn.Conv2d(
#                 in_channels=int(256),
#                 out_channels=int(256),
#                 kernel_size=3,
#                 stride=1,
#             ),
#             nn.Conv2d(
#                 in_channels=int(256),
#                 out_channels=int(256),
#                 kernel_size=3,
#                 stride=1,
#             ),
#         ]
#     )
# )
# m.append(cls_convs)
# m.append(reg_convs)
# print(m)