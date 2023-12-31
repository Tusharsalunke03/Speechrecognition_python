import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as wb
# import pyjokes
import requests, json , sys



listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()



def weather(city):
    # Enter your API key here 
    api_key = "1d45f1656e314bf9c3586dd24a1220e0"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
    
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        #current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        #current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        #z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        #weather_description = z[0]["description"]
        return str(current_temperature)
    
        # print following values 
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''

def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
    
    
def run_alexa():
    command = user_commands()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' + time)

    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)

    # elif 'joke' in command:
    #     engine_talk(pyjokes.get_joke())

    elif 'weather' in command:
        engine_talk('Please tell the name of the city')
        city = user_commands()
        #weather_api = weather('Hong Kong')
        weather_api = weather(city)
        engine_talk(weather_api + 'degree fahreneit' )
    
    elif 'play' in command:
        song = command.replace('play', '')
        #print('New Command is' +command)
        #print('The bot is telling us: Playing' +command)
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
        sys.exit()

    elif 'amazon' in command:
        product = command.replace('amazon', '')
        #print('New Command is' +command)
        #print('The bot is telling us: Playing' +command)
        engine_talk('opening amazon' + product)
        url = 'https://www.amazon.in/s?k='
        wb.open_new(url+product)
        

    elif 'stop' in command:
        sys.exit()
        
    else:
        engine_talk('I could not hear you properly')
        
        
while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print("No Command! Alexa has stopped Working!!")
        break

