import torch
import torchvision
from torchvision import datasets, transforms
from torch import nn, optim
import pickle

# image preprocessing
transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

# load dataset
dataset = datasets.ImageFolder("datasets/plant_disease/plantvillage", transform=transform)

train_loader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

# CNN model
model = nn.Sequential(
    nn.Conv2d(3,16,3),
    nn.ReLU(),
    nn.MaxPool2d(2),

    nn.Conv2d(16,32,3),
    nn.ReLU(),
    nn.MaxPool2d(2),

    nn.Flatten(),
    nn.Linear(32*30*30,128),
    nn.ReLU(),
    nn.Linear(128,len(dataset.classes))
)

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# training
for epoch in range(15):

    for images, labels in train_loader:

        preds = model(images)
        loss = loss_fn(preds, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print("Epoch complete")

# save model
torch.save(model, "models/disease_model.pth")

# save class names
with open("models/disease_classes.pkl", "wb") as f:
    pickle.dump(dataset.classes, f)

print("Disease model trained successfully")