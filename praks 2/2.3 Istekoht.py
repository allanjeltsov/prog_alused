from random import randint
valik = input("Kas soovite istekohta ise valida,kui ja, siis kirjutage (ise) või kui soovite loosida, kirjutage (loos) ")
if valik == "ise":
    kohav = input("kas soovite istuda akna juures (aken) või mitte (muu) ")
    if kohav == "aken" :
        print("valisite ise aknakoht")
    else :
        print ("valisite muu koht")
elif valik =="loos":
    tõenäosus = randint(1,3)
    if tõenäosus == 3:
        print("loositi aknakoht")
    else :
        print ("loositi muu koht")