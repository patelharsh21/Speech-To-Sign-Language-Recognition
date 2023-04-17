
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
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
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'static/letters/'+a[i]+'.jpg'
                                                            return ImageAddress
                                                        #     ImageItself = Image.open(ImageAddress)
                                                        #     # ImageNumpyFormat = np.asarray(ImageItself)
                                                        # #     plt.imshow(ImageNumpyFormat)
                                                        # #     plt.draw()
                                                        # #     plt.pause(0.8)
                                                        #     return ImageItself
                                                    else:
                                                        return None

                        except:
                               print(" ")
                        plt.close()

# while True:
#         translate("Harsh")
#         exit()