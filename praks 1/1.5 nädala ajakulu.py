ainepunktid = int(input("sisestage ainepunktide arvu "))
nadalate_arv = int(input("sisestage nädalate arvu "))
nädalaajakulu = (26 * (ainepunktid / nadalate_arv))
umardatud = round(nädalaajakulu)
print("teie nädala ajakulu on " + str(umardatud))