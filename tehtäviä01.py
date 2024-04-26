"""Tehtävä 102-1: Kirjoita ohjelma, joka kysyy oman nimesi ja tulostaa sen.

Tehtävä 102-2: Kirjoita ohjelma, joka kysyy oman nimesi kerran ja tulostaa sen kahdesti.

Tehtävä 102-3: Kirjoita ohjelma, joka kysyy kaksi kertaa nimen ja tulostaa sitten annetun nimen.

Tehtävä 102-4: Kirjoita ohjelma, joka kysyy nimen ja tulostaa jonkin erikoismerkin ja nimen ja toisen erikoismerkin.
Esimerkiksi: !Aapeli@

Ohjelmassa voi olla monta muuttujaa ja tulostuksessa voidaan käyttää useita muuttujia.

Tehtävä 102-5: Kirjoita ohjelma, joka kysyy etunimen ja sukunimen ja kirjoittaa "nimesi on <etunimi> sukunimi>."

Tehtävä 102-6: Kirjoita ohjelma, joka kysyy nimesi ja osoitteesi ja tulostaa sen kuten osoite kirjoitetaan kirjeessä

BONUS
=====

Tehtävä 102-7: Kirjoita ohjelma, joka kysyy 2-3 asiaa ja tulostaa lyhyen muutaman rivin tarinan, jossa näitä asioita on käytetty.


#1
name = input("What is your name?: ")
print(name)

#2
name = input("What is your name?: ")
print(name, name)

#3
name = input("What is your name?: ")
name = input("What is your name?: ")
print(name)

#4
name = input("What is your name?: ")
print(f"!{name}@")

#5
first_name, last_name = input("What is your first and last name?: ").split()
print(f'"Nimesi on <{first_name}> {last_name}."')
"""

#6 
name = input("What is your name?: ")
street, city = input("What is your address? Separate street and city by a comma: ").split(sep=', ')
print(f"{street, "\n", city)