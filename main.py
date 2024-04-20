from translator import translate_text #rom reverso_context_api import Client

'''
to-do:
1. Can I train/finetune a model on jp images for text extraction.(https://www.kaggle.com/datasets/hnthnt/jp-font-image-dataset-02)
2. ocr paper (https://arxiv.org/pdf/1801.01316.pdf)
'''

''' 
5/16/24:
Not too bad, the translation should be decent if you can extract well.
For manga, its kinda weird 
'''

def detect_text(path):
    """ Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
        image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print("Texts:")
    #print(texts[0].description)
    text_arr = []
    for line in texts[0].description.splitlines():
        if line:  # Add check to avoid empty lines
            text_arr.append(line)
    return text_arr
  


extracted_text=detect_text("./images/irl/irl2.jpeg")
#print(extracted_text)

''' returns array of translated text '''
translated_words= (translate_text(extracted_text))


''' since extracted text and translated words are at the same indice, make dict with ext:trans'''

if len(translated_words) == len(extracted_text):
  translation_dict = {i: j for i, j in zip(extracted_text, translated_words)}    
else:
    print("Lengths of extracted text and translated words do not match.")
print(translation_dict)


