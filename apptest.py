from flask import Flask, render_template, request
import string
import matplotlib.pyplot as plt
from flask import Flask, render_template
from nltk.corpus import stopwords
isl_gif=['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink','hello''do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy','air','produce','environment','animals','because','care','clean','forest','future','generations','health','health','help','homes','important','keep','more','ourselves','oxygen','plant','protect','provide','taking','they','trees','try','we']
        
        
        
arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        
app = Flask(__name__)
def translate(text):            
                                signLanguageArray=[]
                                sentence=text
                                sentence = sentence.lower()
                                print('You Said: ' + sentence.lower())
                                
                                for c in string.punctuation:
                                    sentence= sentence.replace(c,"")
                                    
                                if(sentence.lower()=='goodbye' or sentence.lower()=='good bye' or sentence.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        
                                
                                elif(sentence.lower() in isl_gif):
                                     signLanguageArray.append('static/ISL_Gifs/'+sentence+'.gif')
                                     return signLanguageArray
                                
                                
                                    
                                else:
                                    word_list = sentence.split()
                                    
                                   
                                    for word in  word_list :
                                            if word in isl_gif and word not in stopwords.words('english'):
                                                    signLanguageArray.append('static/ISL_Gifs/'+word+'.gif')
                                            else:
                                                for i in range(len(word)):
                                                                if(word[i] in arr):
                                                                    ImageAddress = 'static/letters/'+word[i]+'.jpg'
                                                                    signLanguageArray.append(ImageAddress)
                                                                
                                    return signLanguageArray            

                      

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
