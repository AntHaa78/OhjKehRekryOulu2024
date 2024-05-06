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
<<<<<<< Updated upstream


Tehtävä 106-1: Tee ohjelma, jossa kirjoitetaan merkkijono ja ilmoitetaan sen pituus.

Tehtävä 106-2: Tee ohjelma, jossa kirjoitetaan liukuluku ja ohjelma ilmoittaa sen pyöristyksen kokonaisluvuksi.

Tehtävä 106-3: Tee ohjelma, jolle syötetään luku Celsiusasteina. Ohjelma ilmoittaa arvon Fahrenheitteina. Etsi kaava netistä.


#106-1
string ="fnewfnwe"
print(len(string))

#106-2 
number = float(input("Enter a floating number: "))
print("The number rounded is ", int(number+0.5))

#106-3
# Sama kuin 105-5


Tehtävä 107-1: Tee ohjelma, joka ilmoittaa monta pistettä tuli jääkiekossa voiton, tasapelin tai tappion tullessa.

Tehtävä 107-2: Tee ohjelma, johon syötetään 2 lukua, kerro kumpi on suurempi vai oliko kyseessä sama luku.

Tehtävä 107-3: Tee ohjelma, johon syötetään 2 nimeä ja ikää. Kerro kumpi henkilö on vanhempi.

Tehtävä 107-4: Tee, ohjelma, johon syötetään kaksi merkkijonoa. Kerro kumpi on ensimmäinen ja viimeinen.


#107-1 
tulos = input("Miten meni (voitto, tasapeli tai tappio)?: ")
if tulos == 'voitto':
    print(f"Se oli voitto -> 3 pistettä")
elif tulos == 'tasapeli':
    print(f"Se oli tasapeli -> 1 piste")
elif tulos == 'tappio':
    print(f"Se oli tappio -> 0 piste")
else:
    print("Tulos not recognized")

#107-2
num1, num2 = [int(x) for x in input("Enter 2 numbers: ").split()]
if num1 > num2:
    print(f"{num1} is > {num2}")
elif num1==num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is < {num2}")

#107-3
name1, age1 = input("H1, what is your name and your age: ").split()
name2, age2 = input("H23, what is your name and your age: ").split()
if int(age1) > int(age2):
    print(f"{name1} is older than {name2}")
elif int(age1)==int(age2):
    print("You are the same age!")
else:
    print(f"{name2} is older than {name1}")

#107-4
string1, string2 = input("Enter 2 strings: ").split()
if string1 < string2:
    print(f"{string1} is 'first'")
else:
    print(f"{string1} is 'second'")

    
Tehtävä 108-1: Tee ohjelma, joka kysyy luvun ja sanoo että alle 10 on pieni ja että negatiivinen luku on negatiivinen. Muuten luku on suuri.

Tehtävä 108-2: Tee ohjelma, joka ilmoittaa onko syötetty nimi joku Aku Ankan veljenpojista.

Tehtävä 108-3: Tee ohjelma, joka ilmoittaa onko syötetty kokonaisluku jaollinen viidellä.

Tehtävä 108-4: Tee ohjelma, joka laskee onko kyseessä karkausvuosi.

#108-1
luku = int(input("Enter a number: "))
if luku < 0:
    print("Luku on negatiivinen")
elif 0 <= luku < 10:
    print("Luku on pieni")
else:
    print("Luku on pieni")

#108-2
veljenpojat = ("Tupu", "Hupu", "Lupu", "Riri", "Fifi", "Loulou")
nimi = input("Anna nimi: ")
if nimi in veljenpojat:
    print(f"{nimi} on yksi Aku Ankan veljenpojista")
else:
    print("Syötetty nimi ei ole yhtä Aku Ankan veljenpojista")

#108-3
num = int(input("Enter a numer: "))
if num%5==0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divible by 5")

#108-4
year = int(input("Enter a year: "))
if year%4==0:
    if year%400==0:
        print(f"{year} is a leap year")
    elif year%100==0:
        print(f"{year} is not a leap year (centuries exception)")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Tehtävä 109-1: Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa "ei"

# Tehtävä 109-2: Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa luvun välillä 1 ja 100

# Tehtävä 109-3: Syötä salasana. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salasana>.

# Tehtävä 109-4: Syötä salanumero. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salanumero>.
Pysäytä tehtävä, jos yrityksiä on enemmän kuin kolme.

# Tehtävä 109-5: Tee lähtölaskenta arvosta 8 arvoon 1, jonka jälkeen kirjoita "Laukaisu!"

# Tehtävä 109-6: Tee toistolause, johon syötetään lukuja kunnes käyttäjä kirjoittaa -1. Laske tämän jälkeen keskiarvo.

#109-1
answer = ''
while answer != 'ei':
    answer = input("What is your answer: ")

#109-2
answer = 0
while answer not in range(1,101):
    answer = int(input("What is your answer: "))

#109-3
salasana = input("Choose salasana: ")
answer = ''
while answer!=salasana:
    answer = input("Enter salasana: ")
print("Pw correct")

#109-4
salanumero = int(input("Choose salanumero: "))
answer = ''
tries=0
while answer!=salanumero and tries<3:
    answer = int(input("Enter salanumero: "))
    tries+=1
if tries<3:
    print("Pw correct")
else:
    print("Number of tries exceeded")

#109-5
x = 8
while x!=0:
    print(x)
    x-=1
print("laukaisu")

#109-6
number_list=[]
while True:
    number = int(input("Enter a number, -1 ends it: "))
    number_list.append(number)
    if number ==-1:
        break
print("The average is:", sum(number_list)/len(number_list))



Tehtävä 110-1: Tulosta joka kolmas luku välillä 1 ja 50.

Tehtävä 110-2: Tee uusiksi lähtölaskentatehtävä niin että siinä ei ole while True: riviä 
vaan jotain muunlainen rivi.

Tehtävä 110-3: Tulosta luvut 1stä eteenpäin käyttäjän antamaan lukuun asti.

Tehtävä 110-4: Tulosta aluksi 1 ja sitten seuraava luku niin että se on edellisen luvun arvo kerrottuna kahdella.

Tehtävä 110-5: kysy kaksi lukua ja tulosta sen potenssit arvosta 0 toiseen lukuun asti

Tehtävä 110-6: Kysy käyttäjältä luku ja tee ohjelma joka laskee 1+2+3... kunnes summa on käyttäjältä saatu luku tai sitä pienempi edellinen luku. Näytä tiedot "1+2+3..." tavalla.

#110-1
for x in range(1,50,3):
    print(x)

#110-2 = 109-5

#110-3
number = int(input("Giva a number bigger than 1: "))
for x in range(1,number+1):
#x=1
#while x <= number:
    print(x)
    #x+=1

#110-4
x = 1
while True:
    print(x)
    answer = input("Continue?: ")
    if answer=='n':
        break
    x=2*x

#110-5
num1, num2 = [int(x) for x in input("Enter 2 numbers: ").split()]
for x in range(1,num2+1):
    print(pow(num1,x))

#110-6
number = int(input("Enter a number: "))
result_sum=0
print("0 ",end='')
for x in range(1,number):
    print("+",x,end=' ')
    result_sum+=x
    if result_sum>=number:
        print(f"\nThe sum is {result_sum} which is greater than or equal to {number}")
        break

        

Tehtävä 111-1: Piirrä joulukuusi * merkeillä. Syötä ensin joulukuusen korkeus numerona.

Tehtävä 111-2: Syötä merkkijono ja toistojen lukumäärä. Tulosta sitten merkkijono toistettuna.

Tehtävä 111-3: Syötä merkkijono ja tulosta se. Lisää vielä "=" merkeillä merkkijonon pituinen alleviivaus.

Tehtävä 111-4: Syötä kaksi merkkijonoa ja kerro kumpi on pitempi

Tehtävä 111-5: Syötä merkkijono ja tulosta sen merkit viimeisestä ensimmäiseen

Tehtävä 111-6: Syötä merkkijono ja tulosta sen toinen ja toiseksi viimeinen merkki

Tehtävä 111-7: Syötä merkkijono ja tee siitä uusi merkkijono, jonka merkit ovat päinvastoin

Tehtävä 111-8: Syötä merkkijono ja tulosta se niin, että kullakin rivillä on yhdestä pituuteen verran kirjaimia

Tehtävä 111-9: Tee 20 merkkinen merkkijono "=" merkeistä. Syötä merkkijono, jono korvaa = merkkejä. 
Tämä merkkijono on lisäksi tasattu oikealle, vasemmalle tai keskelle valinnan mukaan.

Trehtävä 111-10: Syötä merkkijono ja etsi kaikki vokaalit


#111-1
korkeus = int(input("Anna puun korkeus: "))
i = 0
j = 0
while i<int((korkeus/2)+0.5):
    line = " "*(korkeus-i) + "*"*(i*2+1)
    print(line)
    i+=1
while j<int(korkeus/2):
    line2 = " "*(korkeus) + "*"
    print(line2)
    j+=1

#111-2
merkkijono = input("Anna merkkijono: ")
toisto = int(input("Anna toistojen lukumäärä: "))
print(f"{merkkijono} kertaa {toisto} on {merkkijono*toisto}")

#111-3
merkkijono = input("Anna merkkijono: ")
print(merkkijono)
print(f"{len(merkkijono)*'='}")

#111-4
merkkijono1, merkkijono2 = input("Anna 2 merkkijonoa: ")
if len(merkkijono1)>len(merkkijono2):
    print("1 on pitempi kuin 2")
elif len(merkkijono1)==len(merkkijono2):
    print("1 ja 2 ovat yhtä pitkät")
else:
    print("1 on pienempi kuin 2")

#111-5
merkkijono = input("Anna merkkijono: ")
for i in range(len(merkkijono),0,-1):
    print(merkkijono[i-1],end='')

#111-6
merkkijono = input("Anna merkkijono: ")
print(f"toinen merkki: {merkkijono[1]}, toiseksi viimeinen merkki: {merkkijono[-2]}"

#111-7
merkkijono = input("Anna merkkijono: ")
merkkijono_reversed=''
for i in range(len(merkkijono),0,-1):
    merkkijono_reversed = merkkijono_reversed + (merkkijono[i-1])
print(merkkijono_reversed)

#111-8
merkkijono = input("Anna merkkijono: ")
for x in merkkijono:
    print(x)

#111-9
merkkijono = input("Anna merkkijono: ")
order = 2 # 0=vasemma,1=keski,2=oikea
if order==0:
    tulos = merkkijono + (20-len(merkkijono))*"="
elif order==1:
    tulos = int(10-(len(merkkijono)/2))*"=" + merkkijono + int(10-(len(merkkijono)/2)+0.5)*"="
elif order==2:
    tulos = (20-len(merkkijono))*"=" + merkkijono
print(tulos)
print(len(tulos))

#111-10
merkkijono = input("Anna merkkijono: ")
vokaalit = ['a','e','y','u','i','o','ä','ö']
vokaalit_count = 0
for x in merkkijono:
    if x in vokaalit:
        vokaalit_count+=1
print(vokaalit_count)


Tehtävä 112-1: Etsi toinen "i" sanasta "Seinäjoki"

Tehtävä 112-2: Etsi ja ilmoita kaikki indeksit "i" sanalle sanasta "saippuakauppias"

Tehtävä 112-3: Etsi kaikki kolmemerkkiset osajonot, jotka alkavat kirjaimella "a" sanasta "saippuakauppias"


#Small ex
salaisuus = "saaaaalaaasana"

arvaus = input("Anna kirjain: ")
print(f"tekstissä on {salaisuus.count(arvaus)} kpl krijainta {arvaus}")

for count,value in enumerate(salaisuus):
    if value == arvaus:
        print(f"indexissä {count} on krijain {arvaus}")
        
lista = enumerate(salaisuus)
print(list(lista)) 

iter=0
for value in range(len(salaisuus)):
    if salaisuus[value]==arvaus:
        print(f"Indexissä {value} on kirjain {arvaus}")
    iter+=1


#112-1
i_count=0
sana = "Seinäjoki"
for x in sana:
    if x=='i':
        i_count+=1
if i_count==2:
    print("Toinen 'i' löytyy!")
else:
    print("More or less than 2 'i'")
 
#112-2
sana = 'saippuakauppias'
for count,letter in enumerate(sana):
    if letter == 'i':
        print(f"indexissä {count} on 'i' kirjain")

#112-3
sana = "saippuakauppias"
for position,letter in enumerate(sana):
    #print(f"Pos {position} is a {letter}")
    if letter == 'a':
        if position + 2 < len(sana):
            print("Word is " + letter + sana[position+1] + sana[position+2])


Tehtävä 113-1: Tee ohjelma, joka laskee kertotaulun lukuun X asti, eli (esim 2) 1x1, 1xX, Xx1, XxX...

Tehtävä 113-2: Tee ohjelma, jolle syötät lauseen. Tulosta jokaisen sanan ensimmäinen kirjain.

Tehtävä 113-3: Tee ohjelma, joka laskee annetun luvun X kertoman (esim 4) 1*2*3*X = ...

Tehtävä 113-4: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
Tee ohjelma niin, että kukin pari lukuja esitetään suurempi ensin.

Tehtävä 113-5: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
Tee ohjelma niin, että ensin esitetään 1, sitten X, sitten 2, sitten X-1 jne...

#113-1
luku = int(input("Anna luku? "))
laskuriA, laskuriB = 1, 1
while laskuriA <= luku:
    while laskuriB <= luku:
        print(f"{laskuriA}*{laskuriB} = {laskuriA*laskuriB}")
        laskuriB+=1
    laskuriB=1
    laskuriA+=1

#113-2
lause = input("Syötä lause: ")
print(lause[0])
for position, letter in enumerate(lause):
    if letter == ' ':
        print(lause[position+1])

#113-3
luku = int(input("Anna luku? "))
laskuri = 1
tulo = 1
teksti = ""
while laskuri <= luku:
    teksti = teksti + str(laskuri) + "*"
    tulo *= laskuri
    print(f"{laskuri} saa arvoksi {teksti[:-1]} = { tulo }")
    laskuri += 1

luku = int(input("Anna luku? "))
tulo = 1
teksti = ''
for i in range(1,luku+1):
    teksti = teksti + str(i)+"*"
    tulo *=i
    print(f"{i} saa arvoksi {teksti[:-1]} = {tulo}")

#113-4
luku = int(input("Anna luku? "))
luku_list = list(range(1, luku+1))
teksti = ''
for i in range(0, len(luku_list), 2):
    luku_list[i], luku_list[i+1] = luku_list[i+1], luku_list[i] 
    teksti = teksti + ' ' + str(luku_list[i]) + ' ' + str(luku_list[i+1])
print(luku_list)
print(teksti)

#113-5
luku = int(input("Anna luku? "))
luku_list = list(range(1,luku+1))
j=1
for i in range(len(luku_list)):
    if i%2!=0:
        luku_list[i] = luku-int(i/2)
    if i%2==0:
        luku_list[i]=j
        j+=1
    
print(luku_list)

arr = ['sunday', 'monday', 'tuesday', 'wednesday']
 
# without using asterisk, unpacking
print (*arr) # = print(' '.join(map(str,arr)))
"""

# Number guessing game:

""" import random
random.seed()

def guessing_number(result):
    num_wrong_answers = 0
    while num_wrong_answers < 10:
        answer = int(input("\nGuess a number between 1-100! "))

        if answer == result:
            break

        elif answer-result < -5:
            print("\nThe number is larger than {}, try again!".format(answer))
            num_wrong_answers+=1
            print("You now have",10-num_wrong_answers, "attempts left")
            
        elif answer-result > 5:
            print("\nThe number is smaller than {}, try again!".format(answer))
            num_wrong_answers+=1
            print("You now have",10-num_wrong_answers, "attempts left")

        elif abs(answer-result) < 5:
            if answer > result:
                print("\nThe number is smaller than {}, but you're burning!!".format(answer))
            elif answer < result:
                print("\nThe number is larger than {}, but you're burning!!".format(answer))
            num_wrong_answers+=1
            print("You now have",10-num_wrong_answers, "attempts left")
    
    if num_wrong_answers < 10:
        print("\nCongratulations, you guessed it! The number was: ", number)
    elif num_wrong_answers==10:
        print("\nYou lost the game!")

while True:
    number = random.randrange(1,101)
    #print("The number to guess is", number) # for testing
    guessing_number(number)
    play_again = input("\nType 'y' to play again: ")
    if play_again != 'y': 
        break
"""

# Tehtävä 114-6: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen "o" merkillä.

def piirtaa(x,y):
    i=0
    while i < y:
        print("o"*x)
        i+=1

#piirtaa(3,5)

#Tehtävä 114-7: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen aluksi "1" ja sitten "0" merkeillä shakkilautana.

""" def sheikkilauta(x,y):
    for i in range(y):
        print("\r")
        if i%2==0:
            for j in range(x):
                if j%2==0:
                    print("1", end='')
                elif j%2!=0:
                    print("0", end='')
        elif i%2!=0:
            for j in range(x):
                if j%2==0:
                    print("0", end='')
                elif j%2!=0:
                    print("1", end='')
 """

#sheikkilauta(10,10)

#Tehtävä 114-8: Tee ohjelma, jossa on funktio, joka ottaa merkkijonon ja piirtää siitä sananeliön

def piirrasananelio2(sana):
    rivi = sana*2
    for i in range(len(sana)):
        print(rivi[i:len(sana)+i])

#piirrasananelio2('testi')

# Tehtävä 115-1: Tee ohjelma, jonka funktio palauttaa anntuista parametreista pienimmän

def bigger(a,b):
    if a > b:
        return a
    elif b > a:
        return b
#print(bigger(1,2))

# Tehtävä 115-2: Tee ohjelma, jonka funktio ilmoittaa onko annettu merkki sama tai ei (True tai false)
def onkosama(str1,str2):
    return str1==str2
#print(onkosama('lala','lalo'))

# Tehtävä 115-3: Tee ohjelma, jossa on funktio, joka piirtää parametrina annettua merkkiä annetun luvun verran.
# Tee funktio joka piirtää näin neliön annettua merkkiä.

def draw(merkki, luku):
    print(merkki*luku)
    print('\n')
    for i in range(luku):
        print(merkki*luku)

#draw('*',4)

# Tehtävä 116-1: Tee ohjelma, johon kuuluu lista = [0,0,0,0,0,0,0,0,0,0] 
# syötetään indeksi 0+ ja luku arvoksi. Täytä listaa ja tulosta joka syötön jälkeen listan sisältö.

""" lista = [0,0,0,0,0,0,0,0,0,0]
indeksi = int(input("Anna indeksi? "))
while abs(indeksi) < len(lista):
    arvo = int(input("Anna arvo? "))
    lista[indeksi] = arvo
    print(lista)
    indeksi = int(input("Anna indeksi? "))
print("Index out of bound") """

# Tehtävä 116-2: Tee ohjelma, johon syötetään X kappaletta numeroita. 
# Tulosta luotu lista lopuksi.
""" lista=[]
while True:
    try: 
        number = int(input("Test: "))
        lista.append(number)
    except ValueError:
        print("ERROR: --- Not a number ---")
        break
#print(isinstance('lol',int))
print(lista) """
    
# Tehtävä 116-3: Tee ohjelma, jossa on lista, johon voi lisätä ja poistaa arvoja.

""" lista = list(range(10))
print(lista)
answer = input("Lisätä (l) vai Poistaa (p): ")
while answer == 'l' or answer == 'p':
    if answer == 'l':
        lisattu = input("Mitä lisataan: ")
        lista.append(lisattu)
    elif answer == 'p':
        index = int(input("Mikä indeksi? "))
        lista.pop(index)
    print(lista)
    answer = input("Lisätä (l) vai Poistaa (p): ") """

# Tehtävä 116-4: Tee ohjelma, johon syötetään sanoja. Pysäytä se, jos sama sana tuli kahdesti.

""" lista=[]
duplicate = False
while duplicate==False:
    sana = input("Syötä sana: ")
    lista.append(sana)
    print(lista)
    if len(lista) != len(set(lista)): #smart trick, convert to set. other method count duplicates
        print("Duplicates found!")
        duplicate = True """

# Tehtävä 116-5: Tee ohjelma, johon syötetään numeroita. 
# Tulosta joka numeron jälkeen lista sekä sen järjestetty versio.

""" lista = []
while True:
    number = int(input("Söytä numero: "))
    lista.append(number)
    print(sorted(lista))
 """
# Tehtävä 116-7: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# Järjestä lista ja anna se paluuarvona
""" list_test = [1,5,9,7,6,2]

def sorting(lista):
    return sorted(lista)

print(sorting(list_test))
 """
# Tehtävä 117-3: Tulosta "*" niin, että kullekin riville tulee se lukumäärä, 
# joka on sanottu listan elementin arvona.