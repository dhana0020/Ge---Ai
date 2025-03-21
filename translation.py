# -*- coding: utf-8 -*-
"""translation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eUFP_EVqq7TeHFOrCbkQD958OHEEFYFL

text to translation
"""

from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, target_language):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

    return translated_text


text_to_translate = "dhana,have you had lunch"
target_lang = "fr"  # French
translated_text = translate_text(text_to_translate, target_lang)
print(f"Translated Text: {translated_text}")

"""text to audio"""

from gtts import gTTS
import IPython.display as ipd

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save("speech_output.mp3")
    return ipd.Audio("speech_output.mp3")

# Example usage
text_to_speak = "hai dhana, how are you? have you had your breakfast"
lang = "en"  # English

audio = text_to_speech(text_to_speak, lang=lang)
ipd.display(audio)

"""text to audio in other language"""

import IPython.display as ipd

from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import os

def translate_text(text, target_language):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

    return translated_text

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")  # Change to "afplay" for Mac or "mpg321" for Linux
    return ipd.Audio("translated_audio.mp3")
# Example usage
text_to_translate = " how are you?"
target_lang = "fr"  # French
translated_text = translate_text(text_to_translate, target_lang)

print(f"Translated Text: {translated_text}")

# Convert translated text to speech
audio=text_to_speech(translated_text, "fr")  # French speech output


ipd.display(audio)

!pip install gtts

