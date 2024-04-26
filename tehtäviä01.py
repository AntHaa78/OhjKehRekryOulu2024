"""Tehtävä 102-1: Kirjoita ohjelma, joka kysyy oman nimesi ja tulostaa sen.

Tehtävä 102-2: Kirjoita ohjelma, joka kysyy oman nimesi kerran ja tulostaa sen kahdesti.

Tehtävä 102-3: Kirjoita ohjelma, joka kysyy kaksi kertaa nimen ja tulostaa sitten annetun nimen.

Tehtävä 102-4: Kirjoita ohjelma, joka kysyy nimen ja tulostaa jonkin erikoismerkin ja nimen ja toisen erikoismerkin.
Esimerkiksi: !Aapeli@

Ohjelmassa voi olla monta muuttujaa ja tulostuksessa voidaan käyttää useita muuttujia.

Tehtävä 102-5: Kirjoita ohjelma, joka kysyy etunimen ja sukunimen ja kirjoittaa "nimesi on <etunimi> sukunimi>."

Tehtävä 102-6: Kirjoita ohjelma, joka kysyy nimesi ja osoitteesi ja tulostaa sen kuten osoite kirjoitetaan kirjeessä


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

#6 
name = input("What is your name?: ")
street, city = input("What is your address? Separate street and postal code/city by a comma: ").split(sep=', ')
print(f"{name}\n{street}\n{city}\nFinland")

----------------------------------------------------------------------------------------------------------------------------------

Python 104-1: Laske painoindeksi BMI eli paino jaettuna pituuden neliöllä (pituus metreinä).

Python 104-2: Python kerro minä vuonna synnyit ja laske näin kuinka vanha olet

Python 104-3: Kerro nimesi ja minä vuonna synnyit ja kirjoita seuraavaa:
Nimesi on <nimi> ja olet <X> vuotta vanha.

Python 104-4: Määritä luku ja ilmoita sen potenssi kahteen.

Python 104-5: Määritä kaksi lukua ja laske niiden potenssi.

Python 104-6: Kerro tietokoneelle monta päivää on kyseessä ja laske niiden minuuttien lukumäärä

Python 104-7: Syötä kolme lukua ja laske niiden tulo

Python 104-8: Syötä kolme lukua ja laske niiden summa

Python 104-9: Syötä kolme lukua ja laske niiden keskiarvo


#104-1
paino = float(input("Mikä on sun paino(kg)?: "))
pituus = float(input("Mikä on sun pituus(m)?: "))
print(f"Sinun BMI on {paino/(pituus*pituus)}")

#104-2
birthyear = int(input("Milloin synnyit?: "))
print(f"Sinä olet {2024-birthyear}-vuotias tänä vuonna")

#104-3
nimi = input("Mikä on sinun nimi?: ")
birthyear = int(input("Milloin synnyit?: "))
print(f'Nimesi on <{nimi}> ja olet <{2024-birthyear}> vuotta vanha')

#104-4
number = int(input("Give me a number: "))
print(f"{number}^2 is {pow(number,2)}")

#104-5
number1, number2 = input("Give me two numbers: ").split()
number1 = int(number1)
number2 = int(number2)
print(f"{number1}^{number2} is {pow(number1,number2)}")

#104-6
days = int(input("How many days?: "))
print(f"That's equivalent to {days*24*60*60:.2E} seconds")

#104-7
num1, num2, num3 = [ int(x) for x in input("Enter 3 numbers: ").split()]
print(f"Niiden tulo on: {num1*num2*num3}")

#104-8
num1, num2, num3 = [ int(x) for x in input("Enter 3 numbers: ").split()]
print(f"Niiden summa on: {num1+num2+num3}")

#104-9
num1, num2, num3 = [ int(x) for x in input("Enter 3 numbers: ").split()]
print(f"Niiden keskiarvo on: {(num1+num2+num3)/3}")

----------------------------------------------------------------------------------------------------------------------------------


Tehtävä 105-1: Tee ohjelma, joka kysyy vuoden ja sanoo syntymävuotesi, jos kyseessä on vuosi jolloin synnyit.

Tehtävä 105-2: Tee ohjelma, joka antaa luvun itseisarvon. Sen on katsottava onko luku pienempi kuin 0 ja tällöin kertoo luvun -1:llä.

Tehtävä 105-3: Tee ohjelma, joka kysyy nimen ja lukumäärän. Nimen ollessa Aapeli, ohjelma sanoo että tässä ilmainen ruoka. Muuten ohjelma sanoo, että annokset maksavat lukumäärä kertaa 5,90 euroa.

Tehtävä 105-3: Ohjelmalle syötetään luku. Se ilmoittaa että luku on pienempi kuin 10/100/1000/10000

Tehtävä 105-4: Ohjelmalle syötetään kaksi lukua ja laskentatapa (plus, miinus, kerto, jako). 
Ohjelma laskee laskentatavan mukaisen tuloksen ja tulostaa sen.

Tehtävä 105-5: Tee ohjelma, jolle syötetään luku Celsiusasteina. Ohjelma ilmoittaa arvon Fahrenheitteina. Etsi kaava netistä.


#105-1
year = input("Give me a year between 1980 and 2000: ")
if year == '1989':
    print("1989 is your birthyear!")
else:
    print(f"{year} is not your birthyear")

#105-2
number = int(input("Give me a number: "))
if number < 0:
    print(f"The absolute value of {number} is {number*(-1)}")
else:
    print(f"The absolute value of {number} is {number}")

#105-3
name = input("What is your name?: ")
num = int(input("Give me a number: "))
if name == 'Aapeli':
    print("Tässä ilmainen ruoka")
else:
    print(f"Annokset maksavat {num*5.9}e")

#105-4
num1, num2 = [int(x) for x in input("Enter 2 numbers: ").split()]
operation = input("What operation to perform: plus, miinus, kerto, jako ")
if operation == 'plus':
    print(f"The sum is {num1+num2}")
elif operation == 'miinus':
    print(f"The subtraction is {num1-num2}")
elif operation == 'kerto':
    print(f"The product is {num1*num2}")
elif operation == 'jako':
    print(f"The division is {num1/num2}")
else:
    print("Operation not recognised")

#105-5
temp = float(input("What is the termperature?: "))
print(f"The temperature in Far is {(temp*9/5)+32}")
"""