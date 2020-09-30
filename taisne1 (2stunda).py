x1=float(input("Ievadi A punkta x koordinati:"))
y1=float(input("Ievadi A punkta y koordinati:"))  
x2=float(input("Ievadi B punkta x koordinati:"))
y2=float(input("Ievadi B punkta y koordinati:"))  
x3=float(input("Ievadi C punkta x koordinati:"))
y3=float(input("Ievadi C punkta y koordinati:"))
if (x2-x1)==0:
    print("x="+str(x1))
elif (y2-y1)==0:   
    print("y="+str(y1))
else:
    a=(y2-y1)/(x2-x1)
    b=y1-a*x1
    print("y="+str(a)+"x+"+str(b))
print("Paralēlā taisne")

if (x2-x1)==0:
    print("x="+str(x3))
elif (y2-y1)==0:   
    print("y="+str(y3))
else:
    b2=y3-a*x3
    print("y="+str(a)+"x+"+str(b))

print("Perpendikulārā taisne")
if (x2-x1)==0:
    print("y="+str(y3))
elif (y2-y1)==0:   
    print("x="+str(x3))
else:
    a2=-1/a
    b2=y3-a2*x3
    print("y={:-3f}x + {:.3f}"+str(b2).format(a2))
