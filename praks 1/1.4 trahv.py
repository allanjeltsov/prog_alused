nimi = input("sisestage oma nimi")
lubatud_kiirus = int(input("sisestage lubatud kiirus (km/h)"))
tegelik_kiirus = int(input("sisestage tegelik kiirus (km/h)"))
trahv = (tegelik_kiirus - lubatud_kiirus) * 3 
        
tegelik_trahv = min(190, trahv)
print( nimi + ", kiiruse ületamise eest on teie trahv " + str( tegelik_trahv ))
