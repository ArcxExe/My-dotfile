

 
cards = [2,3,4,5,6,7,8,9,10,"Volet","Dam","Korole","Tyz"]
masti = ["ч","к","б","в"]
coloda = []
for i in cards:
    for a in masti:
        coloda.append(str(cards[i])+str(masti[a]))

print(coloda)


