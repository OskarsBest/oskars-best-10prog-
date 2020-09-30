import math
a = float(input("Mala a:"))
b = float(input("Mala b:"))
c = float(input("Mala c:"))
if a>0. and b>0. and c>0.:
    if a<(b+c) and b<(a+c) and c<(a+b):
        print("var izveidot")
        per = a + b + c
        pper = per/2.
        lauk = math.sqrt(pper*(pper-a)*(pper-b)*(pper-c))
        print("Perimetrs= {} Laukums= {}".format(per,lauk))
        aa = a*a
        bb = b*b
        cc = c*c
        if aa == (bb+cc):
            print("Taisnlenķa trīssturis")
        elif aa> (bb+cc):
             print("Platlenķa trīssturis")
        else: 
             print("Šaurlenķa trīssturis")
                    