import torch
from PIL import Image
from torchvision import transforms


model = torch.load("models/disease_model.pth", weights_only=False)
model.eval()

transform = transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])

def predict_disease(image_path):

    img = Image.open(image_path)
    img = transform(img).unsqueeze(0)

    output = model(img)

    _, pred = torch.max(output,1)

    return pred.item()