import torch
import numpy as np
# a=torch.randn((1,5),device='cuda',requires_grad=True)
a=torch.tensor([-10,-1,-0.1,0.,0.1,1,20.])
print(a)
softPlus = torch.nn.Softplus(beta=50,threshold=0)
evidence = softPlus(a)
print(evidence)
# w1=torch.tensor((1.,1.,1.),requires_grad=True,device='cuda')
# m=a*w1
# leakyReLU = torch.nn.LeakyReLU()
# evidence = leakyReLU(m)
# y=torch.max(torch.tensor(1.).type_as(evidence),evidence+1)
# print(a)
# print(y)
# y=y.mean()

# y.backward()
# print(w1.grad)

# print(a)
# b=torch.relu(a)
# print(b)
# b=a.sum()
# b.backward()
# print(a.grad)