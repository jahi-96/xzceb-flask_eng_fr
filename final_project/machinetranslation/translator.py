"""
Module to translate english to french and french to english
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

def get_translator_instance():
    """
    Function to get IBM Translator instance
    """
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version='2021-11-22',
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)
    return language_translator

def english_to_french(english_text):
    """
    Function to translate english to french
    """
    french_text= ''
    if(english_text):
        translation = get_translator_instance().translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Function to translate french to english
    """
    english_text = ''
    if(french_text):
        translation = get_translator_instance().translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
    return english_text
    