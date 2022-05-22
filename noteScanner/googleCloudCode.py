# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:55:33 2022

@author: hgadd
"""

def getTextFromPicture(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    output = []
    outputText = ""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            

            for paragraph in block.paragraphs:
            

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    output.append(word_text)
                 

                    for symbol in word.symbols:
                        try:
                            breakType = str(symbol.property.detected_break.type_)
                            
                            outputText += str(symbol.text)
                            if breakType == "BreakType.SPACE":
                                outputText += " "
                            elif breakType == "BreakType.LINE_BREAK" or breakType =="BreakType.EOL_SURE_SPACE":
                                outputText += "\n"
                            elif breakType == "BreakType.SURE_SPACE":
                                outputText += "    "
                        except:
                            x = "noBreak"
        
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    else:
        return (outputText)
