vanus = int(input("Sisestage oma vanus "))
sugu = input("sisestage oma sugu m või n ")
trenni_tüüp = int(input("sisestage oma trennitüüp 1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening "))

maksimaalne_pulsisagedus = 0
if sugu == "m" or sugu == "M":
    maksimaalne_pulsisagedus = 220 - vanus

if sugu == "n" or sugu == "N":
    maksimaalne_pulsisagedus = 206 - 0.88* vanus
    
if trenni_tüüp == 1 :
    min_puls = 0.5 * maksimaalne_pulsisagedus
    max_puls = 0.7 * maksimaalne_pulsisagedus
elif trenni_tüüp == 2 :
    min_puls = 0.7 * maksimaalne_pulsisagedus
    max_puls = 0.8 * maksimaalne_pulsisagedus
elif trenni_tüüp == 3 :
    min_puls = 0.8 * maksimaalne_pulsisagedus
    max_puls = 0.87 * maksimaalne_pulsisagedus
    
min_puls = round(min_puls)
max_puls = round(max_puls)
    
print("Pulsisagedus peaks olema vahemikus " + str(min_puls) + " kuni " + str(max_puls))