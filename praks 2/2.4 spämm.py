ksuurus = float(input("Sisestage kirja suurus "))
pealkiri = input("sisestage kirja teema pealkiri ")
fail = input("kas kirjaga on kaasa fail? (jah) või (ei)")
if pealkiri == "" or (fail == "jah" and ksuurus > 1.0):
    print ("kiri on spämm")
else :
    print ("kiri ei ole spämm")