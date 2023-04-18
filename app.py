# import speech_recognition as sr
# import numpy as np

# import cv2
# from easygui import *
# import os
# from PIL import Image, ImageTk
# from itertools import count
# import tkinter as tk
import string
import matplotlib.pyplot as plt
from flask import Flask, render_template

#import selecting
# obtain audio from the microphone

#import selecting
# obtain audio from the microphone
def translate(word):
        a=word
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        
        while True:
                        
                        
                        try:
                                
                                a = a.lower()
                                print('You Said: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                
                                else:
                                    signLanguageArray=[]
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                                           ImageAddress = 'static/letters/'+a[i]+'.jpg'
                                                           signLanguageArray.append(ImageAddress)
                                                        # def serve_image():
                                                        #    return send_file('letters/'+a[i]+'.jpg', mimetype='image/jpeg')
                                                            # ImageAddress = 'static/letters/'+a[i]+'.jpg'
                                                            # ImageItself = Image.open(ImageAddress)
                                                            # ImageNumpyFormat = np.asarray(ImageItself)
                                                        #     plt.imshow(ImageNumpyFormat)
                                                        #     plt.draw()
                                                        #     plt.pause(0.8)
                                                            # return ImageNumpyFormat
                                    return signLanguageArray            

                        except:
                               print(" ")
                        plt.close()












from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    signLanguageArray  = translate(text)
    return render_template('translate.html', text=text, signLanguageArray =signLanguageArray)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
