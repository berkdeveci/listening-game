from time import sleep
import os
import random
import pandas as pd
import vlc
from google_speech import Speech

def main():
    def genRandom():
        global rand
        rand = random.randint(0,2465)
    genRandom()

    def getJSON():
        global word
        df = pd.read_json("https://www.randomlists.com/data/words.json")
        word = df['data'][rand]
    getJSON()

    def translateVoice():
        text = word
        print(text)
        lang = "en" 
        speech = Speech(text, lang)
        speech.save(os.getcwd() + "\\words\\" + word + '.mp3')
    translateVoice()

    def playGame():
        vlc.MediaPlayer(os.getcwd() + "\\words\\" + word + '.mp3').play()
        print('Write the word that you just heard.')
        answer = input()
        os.remove(os.getcwd() + "\\words\\" + word + '.mp3')
        if answer == word:
            print('Correct!')
            return main()
        else:
            print('Wrong! Correct word is: ' + word)
            return main()
    playGame()
    print()
    sleep(1)
main()    