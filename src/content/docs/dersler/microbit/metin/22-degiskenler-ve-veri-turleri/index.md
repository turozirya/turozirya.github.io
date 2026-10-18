---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "22. Hafta – Değişkenler ve veri türleri"
description: Python'da sayı ile metin farklı "türdendir"; bunu anlamadan sayaç ve hesap makinesi yapamayız.
sidebar:
  order: 22
hafta: 22
seviye: Python
sure: 2 ders saati
kazanimlar:
  - int ve str veri türlerini ayırt eder.
  - str() ve int() ile tür dönüşümü yapar.
  - Değişkenlerle toplama, çıkarma gibi işlemler yapan bir program yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

5. haftada bloklarla değişken yaratmıştık. MicroPython'da değişken yaratmak çok daha kısa: `isim = deger`. Ama bu hafta yeni bir fikirle tanışıyoruz: her değerin bir **türü** vardır ve bazen bu türleri birbirine çevirmemiz gerekir.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Değişken yaratmak

```python
sayac = 0
isim = "Elif"
```

Blok döneminde **değişken yarat** + **... değişkenini ... yap** iki ayrı blok gerektiriyordu; Python'da tek satır yeterli: `=` işareti "şuna eşit yap" (ata) demektir.

---

## 2. Veri türleri: int ve str

| Tür | Anlamı | Örnek |
| --- | --- | --- |
| `int` (integer) | Tam sayı | `5`, `-3`, `100` |
| `str` (string) | Metin/yazı | `"Elif"`, `"5"` (tırnaklı sayı bile metindir!) |

```python
yas = 12          # int
ad = "Elif"       # str
beşMetin = "5"    # bu da str — tırnak içinde!
```

:::caution[Tırnak işareti her şeyi değiştirir]
`5` bir sayıdır, toplanabilir: `5 + 3` → `8`. `"5"` bir metindir, toplanamaz; `"5" + "3"` Python'da hata verir (ya da metinleri yan yana ekler, sayı gibi toplamaz). Bu, bu haftanın en sık karıştırılan noktasıdır.
:::

---

## 3. Tür dönüşümü: str() ve int()

Bazen bir sayıyı ekranda metin olarak göstermek, bazen de bir metni sayıya çevirmek gerekir:

```python
yas = 12
display.scroll("Yaşım: " + str(yas))   # sayıyı metne çevirip birleştirdik
```

`str(yas)` olmadan `"Yaşım: " + yas` satırı **hata verir** — çünkü metin ile sayı doğrudan birleştirilemez. `str()` sayıyı metne, `int()` ise metni (eğer gerçekten sayıysa) sayıya çevirir.

---

## 4. Proje: Sayaç ve hesap makinesi

**Sayaç** (5. haftanın Python sürümü):

```python
from microbit import *

sayac = 0
while True:
    if button_a.was_pressed():
        sayac += 1          # sayac = sayac + 1 ile aynı
        display.show(sayac)
    if button_b.was_pressed():
        sayac = 0
        display.show(sayac)
```

**Mini hesap makinesi:** A tuşuna her basışta birinci sayı artar, B tuşuna her basışta ikinci sayı artar, A+B'ye basılınca toplam gösterilir:

```python
from microbit import *

sayi1 = 0
sayi2 = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(str(sayi1 + sayi2))
        sleep(500)
    elif button_a.was_pressed():
        sayi1 += 1
        display.show(sayi1)
    elif button_b.was_pressed():
        sayi2 += 1
        display.show(sayi2)
```

---

## Kendini dene

1. Sayacı 1'er artırmak yerine 2'şer artır (`sayac += 2`).
2. Hesap makinesine çıkarma ekle: farklı bir olayla (örnek: logo basıldığında — 12. haftadan hatırlarsın, İngilizce bloktu) `sayi1 - sayi2` göster.
3. Bir değişkende adını (`str`), bir değişkende yaşını (`int`) tutup "Elif, 12 yaşında" gibi bir mesaj oluştur.
4. Bilerek `"5" + 3` yazıp çalıştır, hata mesajını oku; sonra `int("5") + 3` yaparak düzelt.

---

## Mini quiz

1. `yas = 12` satırında 12'nin veri türü nedir?
   a) str  b) int  c) hiçbiri
2. `"5"` ifadesinin veri türü nedir?
   a) int  b) str  c) float
3. Bir sayıyı metinle birleştirmek için önce ne yapılmalı?
   a) str() ile metne çevirmek  b) Hiçbir şey, direkt birleşir  c) Kartı yeniden başlatmak
4. `sayac += 1` satırı neyle aynıdır?
   a) `sayac = 1`  b) `sayac = sayac + 1`  c) `sayac = sayac - 1`
5. `int("7")` ifadesinin sonucu nedir?
   a) "7" (metin olarak kalır)  b) 7 (sayı olur)  c) Hata verir

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-a · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Değişken atama ve int/str kavramı (15 dk), tırnak işaretinin önemini canlı örnekle gösterme (10 dk), str()/int() dönüşümü (15 dk).
- **2. ders saati:** Sayaç kodunu birlikte yazma (10 dk), hesap makinesi projesi (20 dk), hata deneyi (10 dk).
- "5" ile 5 arasındaki fark, bu yaş grubunun en çok zorlandığı kavramlardan biridir; somut örnek olarak "yazı tahtasına yazılan 5 ile cebindeki 5 lira aynı şey değil" benzetmesi kullanılabilir.
- `+=` operatörü yeni görülüyor; `sayac = sayac + 1` ile aynı olduğunu önce uzun hâliyle gösterip sonra kısaltmak öğrenmeyi kolaylaştırır.
- 23. haftada döngülere (while/for/range) daha ayrıntılı gireceğiz; bu haftanın `while True` kullanımı orada derinleşecek.
