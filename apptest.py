from flask import Flask, render_template, request
import string
import matplotlib.pyplot as plt
from flask import Flask, render_template
app = Flask(__name__)
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

@app.route("/")
def index():
    return render_template("test2.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    text = request.json["text"]
    signLanguageArray = translate(text)
    return {"signLanguageArray": signLanguageArray}



if __name__ == "__main__":
    app.run(debug=True)
