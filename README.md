# Udemy 54.Ders Ödev-3

## Girilen 2 Sayının En Küçük Ortak Katını Bulan Program

### Aşağıdaki bilgiler ebob bulmak formülüne ait, buna ekok formülü ekleyip kodlamayı tamamladık.
Ekok Formülü:
```
sayi1 * sayi2 / ebob()
```
* Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazacağız.
* İlk önce 2 tane sayı alıyoruz.
* Daha sonra fonksiyonlarımızı oluşturuyoruz, 2 farklı sayı için 2 farklı fonksiyon oluşturduk, muhtemelen tek fonksiyonla da bu yapılabilir ancak şimdilik 2 farklı sayının bölenlerini çıkarabilmek için 2 farklı liste oluşturarak algoritmamı tasarladım o yüzden 2 farklı fonksiyon ortaya çıktı.
```
list1 =[]

for i in range(1,sayi+1):
  if (sayi % i == 0):
    list1.append(i)
print(list1)
```
Yukarıdaki kodu şu şekilde kısalttım (<b>List Comprehension</b>);
```
list1 = [i for i in range(1,sayi+1) if sayi % i == 0]
print(list1)
```
* Burada 1'den başladım 2 sayısından da başlanabilir.
* Buradaki olay şu; 1'den girilen sayıya kadar listenin içinde gez gezerken bölenlerini çıkar ve bu bölenleri boş bir listeye ekle.
* Bu kodlarla 2 farklı fonksiyon oluşturdum, daha sonra kolayca çağırmak için. Buradaki amaç; girilen sayının bölenlerini listelemek.
* Daha sonra bu 2 liste (bölenler listesi) arasında gezinti yaparak ortak olanları ayrı bir listede listeledim.
* İlk önce şöyle kodlamıştım;
```
list3 = []
for i in bolen1():
  for j in bolen2():
    if (i == j):
      list3.append(i)
```
*Daha sonra bunu da bir fonksiyona ekleyeyim ve bu fonksiyonu da <b>*list comprehension*</b> yöntemiyle kodlayayım dedim.
O da şöyle oldu;
```
def ortak ():
  list3 = [j for i in bolen1() for j in bolen2() if i == j]
  return list3
```
* Bu fonksiyonlardaki <b>*return*</b> ifadesini unutmamak lazım yoksa <b>*none*</b> sonucunu alırsın.
* Bu son fonksiyondaki olay şu; bölenlerini listele, listelerin içinde gez, bu iki listede olan ortak elemanları da ayrı bir listeye ekle, tabi bu ayrı liste baştan boş olmalı.
* Son olarak da çıktı alırken <b>print()</b> fonksiyonun içerisinde <b>ortak()</b> fonksiyonunu çağırarak , o fonksiyonda <b>pop()</b> fonksiyonunu kullandık, yani <b>pop()</b> fonksiyonu içerisine sayı yazmazsak yani kaçıncı elemanı çıkarmak istediğimizi söylemezsek listedeki son elemanı çıkarır ve bize gösterir. (Tabiki <b>print()</b> fonksiyonun içinde kullandığımız için.)

Bazı Ekok, Ebob Formülleri:
-----
1.
```
def ebob(x,y):
	while y:
		r=x
		x=y
		y=r%y
	return x

def ekok(x,y):
	return x*y/ebob(x,y)
```
2.
```
def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))

```
3.
```
def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))
```
-----