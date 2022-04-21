sayi1 = int(input("Birinci Sayıyı Giriniz: "))
sayi2 = int(input("İkinci Sayıyı Giriniz: "))

def bolen1():
  list1 = [i for i in range(1,sayi1+1) if sayi1 % i == 0]
  return list1
  
def bolen2():
  list2 = [i for i in range(1,sayi2+1) if sayi2 % i == 0]
  return list2

def ebob ():
  list3 = [j for i in bolen1() for j in bolen2() if i == j]
  return list3.pop()
  
def ekok(): # ekok için sadece ebobu kullanarak formül uyguladım.
    return sayi1 * sayi2 / ebob()

print("Ebob: ",int(ebob()))
print("Ekok: ",int(ekok()))