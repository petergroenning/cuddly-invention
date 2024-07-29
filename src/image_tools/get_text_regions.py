from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from PIL import Image

model = AutoModelForImageClassification.from_pretrained("microsoft/dit-base-finetuned-rvlcdip")
feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/dit-base-finetuned-rvlcdip")


img = Image.open("samples/test_img2.png").convert("RGB")

inputs = feature_extractor(images=img, return_tensors="pt")


print(model(inputs))
