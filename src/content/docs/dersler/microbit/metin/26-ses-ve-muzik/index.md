---
# Yayına hazır olunca bu satırı sil:
draft: true
title: "26. Hafta – Ses ve müzik"
description: 13. haftadaki melodi kutusu ve gürültü ölçeri music modülü ve mikrofon fonksiyonuyla MicroPython'da yazıyoruz.
sidebar:
  order: 26
hafta: 26
seviye: Python
sure: 2 ders saati
kazanimlar:
  - music modülüyle nota ve melodi çalar.
  - microphone fonksiyonuyla ses seviyesini okur.
  - Ses girdisine tepki veren bir program yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

13. haftada hoparlör ve mikrofon bloklarını kullanmıştık. Bu hafta aynı işleri `music` modülü ve mikrofon fonksiyonuyla yazıyla yapacağız.

**Malzemeler:** micro:bit v2 (hoparlör/mikrofon için v2 şart), USB kablo, bilgisayar.

---

## 1. music modülü

```python
from microbit import *
import music

music.play(music.BA_DING)
```

`music` da bir modül olduğu için `import music` ile eklenir — 24. haftadaki `import random` ile aynı mantık.

| İş | Kod | Blok karşılığı |
| --- | --- | --- |
| Tek nota çalma | `music.pitch(440, 500)` | ton çal (Hz) ... için (ms) |
| Hazır melodi çalma | `music.play(music.BIRTHDAY)` | melodi çal ... bitene kadar çal |
| Nota adıyla çalma | `music.play(['C4:4', 'D4:4', 'E4:4'])` | — (notaları metin olarak yazarız) |

```python
from microbit import *
import music

while True:
    if button_a.was_pressed():
        music.pitch(440, 500)      # Orta La notası, 500 ms
    if button_b.was_pressed():
        music.play(music.BIRTHDAY)
```

:::tip[Nota yazımı: C4:4]
`music.play()` içindeki `'C4:4'` gibi metinler, nota adı + oktav + süre anlamına gelir. Şimdilik ayrıntısına girmeden hazır melodileri (`music.BIRTHDAY`, `music.ENTERTAINER` gibi) kullanmak yeterli; kendi melodini yazmak isteyen öğrenciler için bir ileri seviye alıştırma olarak bırakılabilir.
:::

---

## 2. Mikrofon: microphone.sound_level()

```python
from microbit import *

while True:
    if microphone.sound_level() > 150:
        display.show(Image.HAPPY)
    else:
        display.show(microphone.sound_level())
```

Bu, 13. haftadaki gürültü ölçerin Python sürümü — `microphone.sound_level()` bloktaki (İngilizce kalan) **sound level** ile aynı değeri döndürür.

---

## 3. Proje: Alkış lambası

Mikrofon eşiğini geçen ani bir ses (alkış), bir simgeyi 1 saniye göstersin:

```python
from microbit import *

while True:
    if microphone.sound_level() > 180:
        display.show(Image.YES)
        sleep(1000)
        display.clear()
```

---

## Kendini dene

1. `music.pitch()` ile farklı bir frekans ve süre dene (örnek: 880 Hz, 300 ms).
2. `music.play()` ile hazır gelen başka bir melodiyi dene (`music.ENTERTAINER`, `music.PRELUDE` gibi).
3. Alkış lambasının eşiğini değiştirip sınıfta ne kadar hassas olduğunu test et.
4. İleri seviye: kendi 4 notalık melodini `music.play(['C4:4', 'E4:4', 'G4:4', 'C5:4'])` biçiminde yazmayı dene.

---

## Mini quiz

1. Müzik fonksiyonlarını kullanmak için hangi satır gerekir?
   a) `import microbit`  b) `import music`  c) Hiçbiri, otomatik gelir
2. Tek bir nota çalmak için hangi fonksiyon kullanılır?
   a) `music.play()`  b) `music.pitch()`  c) `microphone.sound_level()`
3. `microphone.sound_level()` neyi döndürür?
   a) Nota adı  b) Ses seviyesini gösteren bir sayı  c) Sıcaklık
4. Alkış lambası projesinde hangi yapı kullanılır?
   a) Eşik değerle karşılaştırma (if)  b) Liste  c) Fonksiyon tanımlama
5. `music.BIRTHDAY` nedir?
   a) Bir değişken  b) Hazır bir melodi  c) Bir hata mesajı

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-a · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** music modülünü içe aktarma ve pitch/play farkı (15 dk), hazır melodilerle deneme (15 dk).
- **2. ders saati:** Mikrofon ve sound_level (10 dk), alkış lambası projesi (15 dk), kendini dene (15 dk).
- Ses seviyesi eşiğini sınıf gürültüsüne göre ayarlamak gerekir; önceden sessiz bir ortamda test edip, ders sırasında sınıf gürültüsüyle yeniden kalibre etmek öğretici bir deneyim olur.
- Nota yazım sistemi (`'C4:4'`) bu yaş grubu için soyut kalabilir; zorunlu tutmayın, meraklı öğrencilere ekstra/ileri seviye olarak sunun.
- 27. haftada fonksiyon, liste ve radyoyu birleştirip blok dönemindeki 14-17. haftaların Python karşılığını tamamlayacağız; 28. hafta final projesiyle bitireceğiz.
