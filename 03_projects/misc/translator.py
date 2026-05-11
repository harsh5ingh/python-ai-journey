from googletrans import Translator

translator = Translator()
translation = translator.translate('Hello', dest='hi')
print(translation.text)