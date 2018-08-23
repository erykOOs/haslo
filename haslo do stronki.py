import sys,time

Haslo = input(">Haslo :  ")

TruePasword = "konik1992"

if TruePasword ==Haslo:
    print (">Wiatamy  w programie")
elif TruePasword !=Haslo:
    print(" >Haslo  : Podałes złe hasło        ")
    time.sleep(2)

input("Podaj haslo")
if TruePasword ==Haslo:
    print (">Witamy w programie")
elif TruePasword !=Haslo:
    print(" > Haslo : Druga proba nie udana")
    time.sleep(2)

input("Podaj haslo")
if TruePasword ==Haslo:
    print (">Witamy w programie")
elif TruePasword !=Haslo:
    print(" > Haslo : Trzeci proba nie udana program zostanie wznowiony za 2 miuty")
    time.sleep(120)
   