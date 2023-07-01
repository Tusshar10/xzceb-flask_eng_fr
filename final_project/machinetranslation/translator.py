"""This is translator.py"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """Convert english text to french"""
    frenchtext=MyMemoryTranslator(source='en-IN', target='fr-FR').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """Convert french text to english"""
    englishtext=MyMemoryTranslator(source='fr-FR', target='en-IN').translate(frenchtext)
    return englishtext
