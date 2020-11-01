# -*- coding: utf-8 -*-
# !pip install googletrans

"""
Created on Mon Nov  2 01:44:11 2020

@author: Nasik
"""
#import the package
from googletrans import Translator 


# Store some text for translation in bangla language
text= '''
ধনধান্য পুষ্প ভরা আমাদের এই বসুন্ধরা
তাহার মাঝে আছে দেশ এক সকল দেশের সেরা
ও সে স্বপ্ন দিয়ে তৈরি সে দেশ স্মৃতি দিয়ে ঘেরা
এমন দেশটি কোথাও খুঁজে পাবে নাকো তুমি
ও সে সকল দেশের রাণী সে যে আমার জন্মভূমি
সে যে আমার জন্মভূমি, সে যে আমার জন্মভূমি।
'''

# Create an instance of Translator to use
translator = Translator()

# detect the language of your entered data
lang =translator.detect(text)
print(lang)

# Call the translate()
res = translator.translate(text, dest = 'en')
#print the result
print(res)

# Call the translate() in french language
res = translator.translate(text, dest = 'fr')
print(res)

# Call the translate() in arabic language
res = translator.translate(text, dest = 'ar')
print(res)