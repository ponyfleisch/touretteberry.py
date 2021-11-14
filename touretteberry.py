import pyttsx3
import argparse
import time
import requests
import random
import logging
import threading

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

nice_words = ['butt', 'wiener', 'boobies']
naughty_words = ['fuck', 'shit', 'ass']

parser = argparse.ArgumentParser(description='Profanity for better air.')
parser.add_argument('--url', type=str, required=True, help='Full URL to endpoint')
parser.add_argument('--min', type=int, default=1000, help='Value at which profanity starts')
parser.add_argument('--max', type=int, default=2000, help='Maximum profanity at this value')
parser.add_argument('--nice-words', default=nice_words, nargs='+', type=str)
parser.add_argument('--naughty-words', default=naughty_words, nargs='+', type=str)

args = parser.parse_args()

engine = pyttsx3.init()
engine.setProperty('rate', 200)

co2 = 0

def fetch_data():
    global co2
    while True:
        try:
            data = requests.get(args.url).json()
            co2 = data.get('co2', 0)
            logging.info(f'CO2 at {co2}')
        except e:
            logging.info(f'Error getting data {e}')
            co2 = 0
        time.sleep(30)

threading.Thread(target=fetch_data).start()

while True:
    random_threshold = random.randint(args.min, args.max)

    if co2 >= random_threshold:
        if co2 >= (args.min + args.max)/2:
            word = random.choice(args.naughty_words)
        else:
            word = random.choice(args.nice_words)
        logging.info(word)
        engine.say(word)
        engine.runAndWait()

    time.sleep(random.randint(3, 10))



