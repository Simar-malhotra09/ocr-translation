from translator import translate_text #rom reverso_context_api import Client

'''
to-do:
1. Can I train/finetune a model on jp images for text extraction.(https://www.kaggle.com/datasets/hnthnt/jp-font-image-dataset-02)
2. ocr paper (https://arxiv.org/pdf/1801.01316.pdf)
'''
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
        image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print("Texts:")
    print(texts[0].description)
    return texts[0].description

extracted_text=detect_text("./images/ja-4.jpg")

''' Call function from translator.py file '''
print(translate_text(extracted_text))



