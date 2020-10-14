a = "Oskars Kipens"
g2 = open("prove.txt","w",encoding="utf-8")
for i in range(5):
    print(i*" ",a,file=g2)
g2.close()