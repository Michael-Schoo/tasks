# Assumptions:
# - password is lower-case alphabetic only
# - password has no minimum length
# - password has maximum length of max_length
# - password is checked through a plain-text match

from datetime import datetime, timedelta
import random
from time import sleep
from termcolor import colored
import os 

os.system('color')

def gen_all_passwords(alphabet, length):
  guesses = set([""])
  for idx in range(length):
    temp = set()
    for seq in guesses:
      for letter in alphabet:
        new_seq = seq
        new_seq += letter
        temp.add(new_seq)
    guesses = sorted(temp)
  return guesses


def brute_force(alphabet, password, length):
  for i in range(length+1):
   guesses = gen_all_passwords(alphabet, i)
   for guess in guesses:
     if password == guess:
       return "Password is " + guess


def brute_force2(wordsLoc, password):
    with open(wordsLoc) as words:  # point this to your words file
        for word in words:
            word = word.strip()  # remove trailing newline
            if word == password:
                return "Password is " + word
            # break



alphabet = "abcdefghijklmnopqrstuvwxyz"
words_loc = "../../../../Downloads/words.txt"
max_length = 5
password = "catty"
# print(brute_force(alphabet, password, max_length))
# print(brute_force2(words_loc, password))

cooldown = {}
# {1: {lastSent: Date, nextAllowedSent: Date, amountSent: 1}}

def sendpasswordReq(guess, id):
    if not cooldown.get(id):
        cooldown[id] = {}
        cooldown[id]["lastSent"] = datetime.now()
        cooldown[id]["amountSent"] = 0
        cooldown[id]["nextAllowedSent"] = cooldown[id]["lastSent"] 


    # if not right time yet
    if cooldown[id]["nextAllowedSent"] > datetime.now():
        future_date = (cooldown[id]["nextAllowedSent"])
        past_date = datetime.now()
        difference = (future_date - past_date)
        total_seconds = difference.total_seconds()

        print("Too soon, time left: " + str(total_seconds))
        return total_seconds

    cooldown[id]["amountSent"] += 1
    cooldown[id]["lastSent"] = datetime.now()
    
    global password
    if (password.strip() == str(guess).strip()):
        print(
            colored(f"Password is {guess}, in {cooldown[id]['amountSent']} attempts", "green"))
        return "Correct"
    else:
        print(colored("Password is not " + guess, 'red'))
        # return False
        numTries = cooldown[id]["amountSent"]
        secondsRem = numTries/10 
        if numTries == 1 | 2: return 0
        if (numTries % 5 == 0): secondsRem = numTries

        print(f"Your {cooldown[id]['amountSent']} attempt: {secondsRem} seconds cooldown")
        cooldown[id]["nextAllowedSent"] = cooldown[id]["lastSent"] + timedelta(seconds= secondsRem)

        return secondsRem

        

def main():
    with open(words_loc) as words:  # point this to your words file
        wordsList = [word for word in list(words) if word.__len__() == 5]
        print(f"possible options: {len(wordsList)} (for 5 char word)")
        global password
        password = random.choice(wordsList)
        print(colored("Password is: "+password, "green"))
        while True:
            word = random.choice(wordsList)
            wordsList.pop(wordsList.index(word))

            resp = sendpasswordReq(word.strip(), id=1)
            try:
                sleep(resp)
            except Exception as e:
                pass

            if resp == "Correct":
                return True
# main()


def mainWithInput():
    with open(words_loc) as words:  # point this to your words file
        wordsList = [word for word in list(words) if word.__len__() == 6]
        print(f"possible options: {len(wordsList)} (for 5 char word)")
        global password 
        password = random.choice(wordsList)
        print(colored("Password is: "+password, "green"))
        while True:
            word = input("Guess: ")
            resp = sendpasswordReq(word.strip(), 1)
            try:
                if resp != True: print(f"Sleeping for {resp} seconds")
                sleep(resp)
            except Exception as e:
                pass

            if resp == True:
                return True
                break

            # break
mainWithInput()
