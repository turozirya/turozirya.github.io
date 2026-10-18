---
title: "11. Hafta – Işık ve sıcaklık sensörleri"
description: micro:bit'in ön yüzündeki LED'ler ortam ışığını, arkasındaki çip sıcaklığı ölçer; bu bilgilerle gece lambası ve termometre yapıyoruz.
sidebar:
  order: 11
hafta: 11
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - micro:bit'in ışık seviyesi ve sıcaklık ölçebildiğini açıklar.
  - Bir sensör değerini bir eşik (sınır) değerle karşılaştırarak karar verir.
  - Sensör okumasına göre otomatik tepki veren bir program yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

micro:bit'in üstünde göremediğimiz iki "duyu organı" var: ön yüzdeki kırmızı LED'ler aynı zamanda ışığı **ölçebilir**, kartın üzerindeki çip de kendi **sıcaklığını** ölçer. Bu hafta bu iki sensörü okuyup bir **eşik değere** göre karar veren programlar yazacağız: karanlıkta kendiliğinden yanan bir lamba ve bir termometre.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar. (İsteğe bağlı: el feneri veya karartmak için kutu, sıcaklık farkı için elini kartın üzerine koyma.)

---

## 1. Sensör nedir?

**Sensör**, çevredeki bir bilgiyi (ışık, sıcaklık, ses, hareket...) sayıya çeviren parçadır. Önceki haftalarda butonlar da bir tür sensördü (basılı/basılı değil). Bu hafta öğreneceğimiz sensörler **sayı** döndürür:

| Blok | Kategori | Ne ölçer? | Değer aralığı |
| --- | --- | --- | --- |
| ışık seviyesi | Girdi | Ön yüzdeki LED'lere gelen ışık | 0 (karanlık) – 255 (çok parlak) |
| sıcaklık (°C) | Girdi | Çipin kendi sıcaklığı (yaklaşık oda sıcaklığı) | Santigrat derece |

:::tip[Bunlar da birer blok]
Daha önce **duraklat (ms)** veya **sayıyı göster** bloğuna bir sayı yazıyorduk. Bu hafta sayıyı biz yazmıyoruz; **ışık seviyesi** ve **sıcaklık (°C)** blokları bu sayıyı kendileri ölçüp getiriyor. Bu bloklar diğer blokların "içine" (boş kutucuğun olduğu yere) yerleştirilir.
:::

---

## 2. Eşik değer: "Ne zaman karanlık sayılır?"

Bir lambanın otomatik yanması için bilgisayara "karanlık" demek yetmez; bir **sayı** sınırı vermemiz gerekir: "ışık seviyesi 30'dan küçükse karanlıktır." Bu sınıra **eşik değer** denir.

![Gece lambası kodu: program başladığında sicaklikGosteriliyor değişkeni false yapılır. Her zaman bloğunda sicaklikGosteriliyor false ise ışık seviyesi 30'dan küçükse led'lerde ampul deseni yanar, değilse ekran temizlenir. A tuşuna basıldığında sicaklikGosteriliyor true yapılır, ekran temizlenir, sıcaklık (°C) değeri gösterilir, 2000 ms beklenir ve sicaklikGosteriliyor tekrar false yapılır.](./gece-lambasi-bloklari.png)

**Canlı dene:** <a href="https://makecode.microbit.org/_8s5fbH62Rfm6" target="_blank" rel="noopener noreferrer">Bu projeyi MakeCode'da aç</a> ve simülatörde çalıştığını gör.

**program başladığında:** `sicaklikGosteriliyor` değişkenini `yanlış` yap.

**Gece lambası:** her zaman bloğunda → eğer `sicaklikGosteriliyor` **yanlış** ise: eğer **ışık seviyesi** < 30 ise ampul deseni göster, değilse ekranı temizle.

**Termometre:** A tuşuna basıldığında:

1. `sicaklikGosteriliyor` değişkenini `doğru` yap.
2. Ekranı temizle (eski ampul deseni kalmasın).
3. **sıcaklık (°C)** değerini ekranda göster.
4. `duraklat (ms)` 2000 (okunacak kadar bekle).
5. `sicaklikGosteriliyor` değişkenini `yanlış` yap.

:::caution[En sık hata: Mesaj görünmeden siliniyor]
`her zaman` ve `A tuşuna basıldığında` blokları **aynı anda, birbirinden bağımsız** çalışır. Sadece "A tuşuna basıldığında sıcaklığı göster" yazarsan, oda aydınlıkken `her zaman` bloğu saniyede yüzlerce kez **ekranı temizle**'yi çalıştırdığı için sıcaklık görünür görünmez silinir. Çözüm, bir **bayrak değişken** (`sicaklikGosteriliyor`) ile `her zaman` bloğuna "şu an mesaj gösteriliyor, ekrana dokunma" demektir — 9. haftadaki `hazir` değişkeniyle aynı teknik.
:::

:::note[Eşik değeri simülatörle bul]
MakeCode simülatöründe ışık seviyesini sürükleyerek değiştirebilirsin. 30 doğru bir sınır mı, yoksa senin odan için 50 mi daha uygun? Simülatörde deneyerek bul.
:::

---

## 3. Python'da sensör okuma

MicroPython'da bu iki sensör de hazır fonksiyonlarla okunur (25. haftada ayrıntılı göreceğiz):

```python
from microbit import *

while True:
    if display.read_light_level() < 30:
        display.show(Image.ARROW_N)  # ampul yerine örnek simge
    else:
        display.clear()

    if button_a.was_pressed():
        display.scroll(temperature())
```

`display.read_light_level()` ışık seviyesini, `temperature()` sıcaklığı döndürür — tıpkı bloklardaki **ışık seviyesi** ve **sıcaklık (°C)** gibi.

Dikkat ettiysen Python kodunda **bayrak değişkene gerek yok**. `display.scroll(...)` çağrısı bitene kadar döngü bir sonraki adıma geçmez (yani **bloklamalı/senkron** çalışır); bloklardaki `her zaman` ve `A tuşuna basıldığında` ise birbirinden bağımsız, aynı anda çalışan iki ayrı akıştır. Aynı programın iki farklı dilde neden farklı davrandığını görmek, "eşzamanlılık" kavramına ilk bakıştır.

---

## Kendini dene

1. Eşik değeri 30'dan 60'a çıkar; lamba daha mı erken yoksa daha mı geç yanıyor?
2. Sıcaklık 20°C'den büyükse "sıcak" (gülen yüz), değilse "serin" (nötr yüz) gösteren bir program yaz.
3. Gece lambasına bir "alacakaranlık" durumu ekle: ışık 30'dan küçükse ampul, 30–100 arasında ise nötr yüz, 100'den büyükse ekranı temizle. (İpucu: eğer-değilse içine bir eğer-değilse daha koy.)
4. Sıcaklığı her saniye kontrol edip, bir önceki okumadan 2 derece fazla ısınırsa uyarı simgesi gösteren bir "mini alarm" yap.

---

## Mini quiz

1. ışık seviyesi bloğu hangi kategoridedir?  
   a) Mantık  
   b) Girdi  
   c) Müzik
2. Işık seviyesi değeri 0 olduğunda ortam nasıldır?  
   a) Çok parlak  
   b) Tamamen karanlık  
   c) Ilık
3. "Eşik değer" ne işe yarar?  
   a) Sensör sayısını bir sınırla karşılaştırıp karar vermeye yarar  
   b) Kartı yeniden başlatır  
   c) Rengi değiştirir
4. sıcaklık (°C) bloğu neyi ölçer?  
   a) Oda nemini  
   b) Çipin kendi sıcaklığını  
   c) El sıcaklığını tam olarak
5. Python'da ışık seviyesini okuyan fonksiyon hangisidir?  
   a) temperature()  
   b) display.read_light_level()  
   c) button_a.is_pressed()

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-a · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Sensör kavramı ve ışık/sıcaklık sensörlerinin tanıtımı (10 dk), eşik değer kavramı ve simülatörde ışık seviyesini sürükleyerek deneme (15 dk), gece lambası kodunu birlikte kurma (15 dk).
- **2. ders saati:** Termometre bloğunu ekleme (10 dk), kendini dene 1-2 (15 dk), kendini dene 3-4 ileri seviye öğrenciler için (15 dk).
- Gerçek ortamda ışık seviyesi sınıf ışığına göre çok değişir; "doğru" eşik değeri yoktur, öğrencilerin simülatörde/kartta deneyerek kendi sınırlarını bulması asıl öğrenme hedefidir.
- Sıcaklık sensörü çipin kendi sıcaklığını ölçtüğü için oda sıcaklığından biraz yüksek çıkabilir (kart az ısınır); bu "hatalı" değil, gerçek sensörlerin sınırlı olduğunu tartışmak için iyi bir fırsattır.
- Bu haftadan sonra 12. haftada pusula ve logoya dokunma sensörleriyle devam ediyoruz.
