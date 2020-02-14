import torch
import numpy as np
import torch.utils.data as Data
import torch.nn as nn
from torch.nn import init
import torch.optim as optim

num_features = 2
num_samples = 1000


# 创造/生成数据集
def make_data():
    true_w = [2, -3.4]
    true_b = 4.2
    # 正太分布 样本数*特征数
    features = torch.tensor(np.random.normal(0, 1, (num_samples,num_features)),
                            dtype=torch.float)
    # 完全标准线性的标签值
    labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
    # 添加轻微扰动，使标签值更真实
    labels = labels + torch.tensor(np.random.normal(0, 0.01, size=labels.size()),
                                   dtype=torch.float)
    return features, labels


# 读取数据
def read_data():
    features, labels = make_data()
    batch_size = 10
    # 使用torch的数据导入函数，将训练数据的特征和标签组合成数据集
    dataset = Data.TensorDataset(features, labels)
    # 随机读取小批量
    # 把 dataset 放入 DataLoader
    data_iter = Data.DataLoader(
        dataset=dataset,  # torch TensorDataset format
        batch_size=batch_size,  # mini batch size
        shuffle=True,  # 要不要打乱数据 (打乱比较好)
        num_workers=1,  # 可使用多线程来读数据
    )
    return data_iter


# 定义模型
def construct_net():
    # 用Sequence的方法直接调用生成
    net = nn.Sequential(nn.Linear(num_features, 1))
    return net


# 初始化模型参数
def init_net_parameter(net):
    init.normal_(net[0].weight, mean=0, std=0.01)
    init.constant_(net[0].bias, val=0)


# 定义损失函数与优化算法
def define_loss_and_optimizer(net):
    loss = nn.MSELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.03)
    return loss, optimizer


# 训练模型
def train_model(net, data_iter):
    global l
    num_epochs = 3
    loss, optimizer = define_loss_and_optimizer(net)
    for epoch in range(num_epochs):
        for x, y in data_iter:
            output = net(x)
            l = loss(output, y.view(-1, 1))
            optimizer.zero_grad()  # 梯度清零 ？
            l.backward()
            optimizer.step()
        # .item()是将一个标量tensor转换成一个python number
        print("epoch %d , loss: %f " % (epoch + 1, l.item()))


if __name__ == "__main__":
    # 读取迭代式数据集
    data_iter = read_data()
    # 构建网络
    net = construct_net()
    print(net)
    # 初始化模型参数
    init_net_parameter(net)
    # 开始训练
    train_model(net=net, data_iter=data_iter)
