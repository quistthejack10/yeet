from time import sleep
from py_imessage import imessage
from num import num


# get the words from text file
def get_lyrics():
    with open('lyrics.txt') as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string


# convert words into string
def get_words(lyrics_str):
    return lyrics_str.split()


# loop
def send_messages(phone_number, messages):
    for message in messages:
        send_message(phone_number, message)
        sleep(.2)


# open imessage
def send_message(phone_number, message):
    imessage.send(phone_number, message)


def get_lyrics_and_send_messages(phone_number, lyrics):
    words_list = get_words(lyrics)
    send_messages(phone_number, words_list)


get_lyrics_and_send_messages(num, get_lyrics())

