import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import openai
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text);

def ai(prompt):
    import openai

    openai.api_key = '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'

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )

    print(response['choices'][0]['text'].strip())
    say(response['choices'][0]['text'].strip())


chatstr=""
def chat(query):
    global chatstr
    chatstr+= f"shashank:{query}\n jarvis:"
    import openai


    openai.api_key = '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'

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=60
    )
    chatstr += f"{response['choices'][0]['text']}\n"
    print(chatstr)
    say(response['choices'][0]['text'].strip())



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
          query = r.recognize_google(audio, language="en-in")
          return query
        except Exception as e:
            return "soory"
if __name__ == "__main__":
    say("hey there , i am jarvis . who's there ? ")
    take_name = takecommand()
    say(f"hey {take_name} . how are you ?")
    query = takecommand()
    if "fine" in query.lower():
        say("ohh nice")
    if "not" in query.lower():
        say("ohh, don't sad . you will have a great luck . i can see a lot of potential in u dear")
    temp=0;
    while 1:
      query = takecommand()
      sites= [["youtube","https://www.youtube.com"],["google","www.google.com"],["wikipedia","https://www.wikipedia.org/"],["instagram","https://www.instagram.com/"]]
      for site in sites:
        if f"open {site[0]}".lower() in query.lower():
          say(f"opening {site[0]}")
          webbrowser.open(site[1])
          temp=1;
          break
      if(temp==1):
          break
      if "the time" in query.lower():
          strftime = datetime.datetime.now().strftime("%H:%M:%S")
          say(f"the time is {strftime}")
      elif "using artificial intelligence".lower() in query.lower():
          ai(query)
      else:
          chat(query)

