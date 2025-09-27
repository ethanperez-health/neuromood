from deepface import DeepFace

result = DeepFace.analyze(img_path="C:/Users/ethan/OneDrive/Documents/face.jpeg", actions=["emotion"])
print(result)
