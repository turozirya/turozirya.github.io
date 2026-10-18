---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "21. Hafta – Butonlar ve if-elif-else"
description: 4. haftadaki duygu kartını bu kez MicroPython ile, if-elif-else koşullarıyla yazıyoruz.
sidebar:
  order: 21
hafta: 21
seviye: Python
sure: 2 ders saati
kazanimlar:
  - is_pressed() ve was_pressed() farkını açıklar.
  - if, elif, else yapısını doğru girintiyle yazar.
  - Buton durumuna göre dallanan bir program yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

4. haftada **A tuşuna basıldığında** ve 6. haftada **eğer-ise** bloklarını öğrenmiştik. Bu hafta ikisini birden MicroPython'da yazacağız: butonları okuma ve `if`/`elif`/`else` ile karar verme.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. is_pressed() ve was_pressed() farkı

| Fonksiyon | Soruyor | Blok karşılığı |
| --- | --- | --- |
| `button_a.is_pressed()` | "Şu an basılı mı?" (sürekli kontrol) | A tuşu basılı mı |
| `button_a.was_pressed()` | "Son kontrolden sonra basıldı mı?" (bir kerelik) | A tuşuna basıldığında |

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
```

:::tip[Neden iki farklı fonksiyon var?]
`was_pressed()` "basıldı mı, bir kere söyle" der — hızlı dokunuşları bile yakalar. `is_pressed()` "şu an basılı mı" der — parmağın tuştan kalkınca `False` olur. Hangisini seçeceğin, projenin ihtiyacına göre değişir.
:::

---

## 2. if, elif, else

Bloktaki **eğer-ise / değilse / yoksa eğer** yapısının MicroPython karşılığı:

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    elif button_b.was_pressed():
        display.show(Image.SAD)
    else:
        display.clear()
```

- `if` → "eğer"
- `elif` → "değilse eğer" (elif = "else if"in kısaltması)
- `else` → "yoksa" (hiçbir koşul doğru değilse)

:::caution[İki nokta ve girinti]
Her `if`/`elif`/`else` satırı **`:`** ile biter ve altındaki satırlar girintilidir — 20. haftada öğrendiğimiz kural burada da geçerli.
:::

---

## 3. Duygu kartının Python sürümü

4. haftadaki duygu kartını (A→mutlu, B→üzgün, A+B→kalp) MicroPython'da yazalım:

```python
from microbit import *

while True:
    if button_a.was_pressed() and button_b.was_pressed():
        display.show(Image.HEART)
    elif button_a.was_pressed():
        display.show(Image.HAPPY)
    elif button_b.was_pressed():
        display.show(Image.SAD)
```

**Dikkat:** A+B kontrolü, A ve B'nin tek tek kontrolünden **önce** yazılmalı; yoksa Python önce "A'ya mı basıldı" sorusuna "evet" der ve hiçbir zaman A+B'yi kontrol etmeye sıra gelmez.

---

## Kendini dene

1. Duygu kartına üçüncü bir durum ekle: hiçbir tuşa basılmazsa 2 saniyede bir göz kırpan bir simge göster.
2. `was_pressed()` yerine `is_pressed()` kullanarak aynı kodu yaz, farkı gözlemle (ipucu: basılı tutunca ne oluyor?).
3. A tuşuna her basışta bir sayaç artırıp göstren, 5'e gelince farklı bir simge gösteren kod yaz.
4. Bilerek `elif` yerine `else` yazıp (fazladan bir `else` ekleyerek) ne tür hata aldığını incele, düzelt.

---

## Mini quiz

1. `button_a.was_pressed()` ne sorar?
   a) Şu an basılı mı  b) Son kontrolden sonra basıldı mı  c) Kart açık mı
2. `elif` kelimesi neyin kısaltmasıdır?
   a) "else if"  b) "end line if"  c) "equal if"
3. Duygu kartında A+B kontrolü neden önce yazılır?
   a) Rastgele öyle, önemi yok  b) Yoksa sadece A veya B kontrolüne düşer, A+B'ye hiç sıra gelmez  c) Python öyle istiyor, sebepsiz
4. Her if/elif/else satırı neyle biter?
   a) Noktalı virgülle  b) İki noktayla (:)  c) Parantezle
5. Hiçbir koşul doğru değilse hangi blok çalışır?
   a) if  b) elif  c) else

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-a · 3-b · 4-b · 5-c

</details>

---

## Öğretmen notu

- **1. ders saati:** is_pressed/was_pressed farkını canlı gösterme (basılı tutma vs. kısa dokunma, 10 dk), if-elif-else söz dizimi (10 dk), basit örnek birlikte yazma (15 dk).
- **2. ders saati:** Duygu kartını birlikte kodlama ve A+B sırası tuzağını gösterme (15 dk), kendini dene (20 dk).
- A+B sırası hatası (3. mini quiz sorusu), bu haftanın en önemli "aha" anıdır — bilerek yanlış sırayla yazdırıp sonucu gözlemletmek güçlü bir öğretim yöntemidir.
- Blok dönemindeki "eğer-ise/değilse/yoksa eğer" ile bu haftanın if-elif-else'i birebir eşleştiğini vurgulamak, geçişi kolaylaştırır.
- 22. haftada değişkenler ve veri türlerine geçiyoruz; bu hafta koşulları iyi oturtan öğrenciler orada daha hızlı ilerler.
