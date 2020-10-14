import math
a = int(input("Mala a:"))
b = int(input("Mala b:"))
c = int(input("Mala c:"))
if a>0. and b>0. and c>0.:
    if a<(b+c) and b<(a+c) and c<(a+b):
        g2 = open("prove.txt","w",encoding="utf-8")
        print("VAR",file=g2)
        g2.close()
    else:
        g2 = open("prove.txt","w",encoding="utf-8")
        print("NEVAR",file=g2)
        g2.close()

      
                    