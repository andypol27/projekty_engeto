"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Andrea Poláková
email: andreapolaku@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz"  : "pass123"
    }

user_input = input("Zadejte své uživatelské jméno a heslo oddělené mezerou:")
parts = user_input.split()
if len(parts) == 2:
     user,password = parts
else:
    print("Musíš zadat přesně dvě slova!")

import time
if user not in users or users[user] != password:
        print(f"username:{user}")
        print(f"password:{password}")
        for _ in range(1):
          print("Unregistered user, terminating the program...")
          time.sleep(3)
          exit()
       
        
else:
        print(f"username:{user}")
        print(f"password:{password}")
        
        print(40*"-")
        print(f"Welcome to the app, {user} !")
        print(f"We have 3 texts to be analyzed")
        print(40*"-")
       
    
 
cislo_textu = input("Enter a number btw. (1 to 3) to select:")        
 
   
if cislo_textu.isdigit():
        text=int(cislo_textu)
        if text <= len(TEXTS):
           text=TEXTS[text-1]
           

        else:
           print("Takový text tu není, ukončuji program.")
           exit()
else:
        print("Chybný vstup, není číslo, ukončuji program.")
        exit()
  
        
print(40*"-")   
words = text.split()
pocet_slov = len(words) 
pocet_uppercase = sum(1 for word in words if word.isupper())
pocet_lowercase = sum(1 for word in words if word.islower())
pocet_titlecase = sum(1 for word in words if word.istitle())
pocet_numer_strings = sum(1 for word in words if word.isdigit())
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_uppercase} uppercase words in the selected text.")
print(f"There are {pocet_lowercase} lowercase words in the selected text.")
print(f"There are {pocet_titlecase} titlecase words in the selected text.")
print(f"There are {pocet_numer_strings} numeric strings in the selected text.")
suma_cisel = 0
for word in words :
  if word.isdigit():
          suma_cisel += int(word)

print(f"Sum of all numbers in the text is: {suma_cisel}")
  
print(40*"-")
print(f"LEN | OCCURRENCES | NR.")
print(40*"-")

len_occurrences = dict()
for word in words:
 delka_slova = len(word)
 if delka_slova in len_occurrences:
    len_occurrences[delka_slova] +=1
     
 else:
    len_occurrences[delka_slova] = 1

max_hodnota = max(len_occurrences.keys())
sirka_sloupce_hvezdicky = max_hodnota + 4
for delka_slova,pocet in sorted(len_occurrences.items()):
    hvezdy = '*' * delka_slova
    print(f"{delka_slova} | {hvezdy :<{sirka_sloupce_hvezdicky}} | {pocet}")

    
    
