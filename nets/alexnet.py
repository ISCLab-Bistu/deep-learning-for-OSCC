import torch
import torch.nn as nn
import torchvision

class AlexNet(nn.Module):
    def __init__(self,num_classes=6):
        super(AlexNet,self).__init__()
        self.feature_extraction = nn.Sequential(
            nn.Conv1d(in_channels=1044,out_channels=512,kernel_size=1,stride=1,padding=0,bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(512),
            # nn.MaxPool1d(kernel_size=1,stride=1,padding=0),
            nn.Conv1d(in_channels=512,out_channels=256,kernel_size=1,stride=1,padding=0,bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(256),
            # nn.MaxPool1d(kernel_size=1,stride=1,padding=0),
            nn.Conv1d(in_channels=256,out_channels=128,kernel_size=1,stride=1,padding=0,bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(128),
            nn.Conv1d(in_channels=128,out_channels=64,kernel_size=1,stride=1,padding=0,bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(64),
            nn.Conv1d(in_channels=64,out_channels=32,kernel_size=1,stride=1,padding=0,bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(32),
            # nn.MaxPool1d(kernel_size=1, stride=2, padding=0),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(in_features=32,out_features=16),
            nn.Dropout(p=0.5),
            # nn.Linear(in_features=4096, out_features=4096),
            nn.Linear(in_features=16, out_features=num_classes),
        )
    def forward(self,x):
        # x = x.permute(0, 2, 1)
        x = self.feature_extraction(x)
        x = x.view(x.size(0),-1)
        x = self.classifier(x)
        return x



