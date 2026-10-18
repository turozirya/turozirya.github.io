---
title: "12. Hafta – Pusula ve dokunmatik logo"
description: micro:bit'in içindeki pusula kuzeyi bulur, altın logosu ise bir dokunma düğmesi gibi çalışır.
sidebar:
  order: 12
hafta: 12
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - Pusulanın neden kalibrasyon gerektirdiğini açıklar.
  - Pusula yönü değerini okuyup yöne çevirir.
  - Logoya dokunma olayını bir programda kullanır.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

micro:bit'in içinde gerçek bir pusula var — manyetik alanı ölçüp hangi yöne baktığını derece olarak söyler. Ayrıca kartın önündeki altın renkli **logo** da bir dokunma sensörüdür. Bu hafta ikisini birleştirip basit bir dijital pusula yapacağız.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Pusula neden kalibre edilir?

Pusula, Dünya'nın manyetik alanını ölçer. Ama kartın çevresindeki metal nesneler (sıra, bilgisayar hoparlörü) bu ölçümü bozabilir. Bu yüzden pusulayı kullanmadan önce **kalibre etmek** (ayarlamak) gerekir — kart, 8 yönün hepsini bir kez görsün diye öğrenciden kartı döndürmesini ister.

**pusulayı kalibre et** bloğu bu işlemi başlatır; genelde **program başladığında** bloğunun içine konur.

---

## 2. Logoya dokunma

Kartın ön yüzündeki altın logo, bir dokunmatik düğme gibi kullanılabilir. Bu blok şimdilik Türkçeye çevrilmemiş, İngilizce görünür: **on logo pressed**. ("Logo basıldığında" demektir.)

:::note[İngilizce blok]
MakeCode'daki bazı bloklar henüz Türkçeye çevrilmedi; **on logo pressed** bunlardan biri. Arayüzde İngilizce görsen de ne işe yaradığını artık biliyorsun.
:::

---

## 3. Dijital pusula

![Pusula kodu: program başladığında pusula kalibre edilir ve kalibreGosteriliyor değişkeni false yapılır. on logo pressed bloğunda kalibreGosteriliyor true yapılır, "Kalibre" yazısı gösterilir, 2000 ms beklenir ve kalibreGosteriliyor tekrar false yapılır. Her zaman bloğunda kalibreGosteriliyor false ise pusula yönü 90'dan küçükse K, 180'den küçükse D, 270'den küçükse G, değilse B harfi gösterilir.](./pusula-bloklari.png)

**Canlı dene:** <a href="https://makecode.microbit.org/_DT4KFk7TbCCR" target="_blank" rel="noopener noreferrer">Bu projeyi MakeCode'da aç</a> ve simülatörde çalıştığını gör.

**program başladığında:** pusulayı kalibre et, `kalibreGosteriliyor` değişkenini `yanlış` yap.

**on logo pressed:**

1. `kalibreGosteriliyor` değişkenini `doğru` yap.
2. `"Kalibre"` yazısını göster.
3. `duraklat (ms)` 2000 (okunacak kadar bekle).
4. `kalibreGosteriliyor` değişkenini `yanlış` yap.

**her zaman:** eğer `kalibreGosteriliyor` **yanlış** ise, **pusula yönü (°)** değerine göre dizgi göster:

| Pusula yönü (°) | Yazılan harf | Yön |
| --- | --- | --- |
| 0 – 89 | K | Kuzey |
| 90 – 179 | D | Doğu |
| 180 – 269 | G | Güney |
| 270 – 359 | B | Batı |

:::caution[En sık hata: Mesaj görünmeden siliniyor]
`her zaman` ve `on logo pressed` blokları **aynı anda, birbirinden bağımsız** çalışır. Bayrak değişken (`kalibreGosteriliyor`) olmadan, logoya dokununca gösterilen "Kalibre" yazısı, `her zaman` bloğunun saniyede yüzlerce kez yazdırdığı yön harfiyle anında üzerine yazılır. 11. haftadaki `sicaklikGosteriliyor` ile aynı teknik burada da işe yarıyor.
:::

:::tip[İç içe eğer-değilse]
Dört seçenek arasından seçmek için üç tane **eğer-değilse** iç içe kullanılır — 6. haftadaki puan tabelası kodunda da aynı yapıyı görmüştük.
:::

---

## Kendini dene

1. Harf yerine ok simgesi göster (K için yukarı ok gibi).
2. Pusula yönünü 4 yerine 8 yöne böl (KD, GD, GB, KB eklenerek).
3. "Mekke pusulası" fikri: belirli bir açıyı (örnek: 120°) sabit kabul edip, kart o açıya ne kadar yakınsa "sıcak", uzaksa "soğuk" diyen bir oyun yap.
4. Logo'ya basılı tutulduğunda (olay yerine "logo is pressed" koşuluyla) farklı bir tepki ekle.

---

## Mini quiz

1. Pusula neyi ölçer?  
   a) Sıcaklık  
   b) Dünya'nın manyetik alanına göre yön  
   c) Ses yüksekliği
2. Pusula neden kalibre edilir?  
   a) Pil tasarrufu için  
   b) Çevredeki metaller ölçümü bozabildiği için  
   c) Zorunlu değildir, süsleme amaçlıdır
3. Logoya dokunma bloğu Türkçe mi İngilizce mi görünür?  
   a) Türkçe  
   b) İngilizce (on logo pressed)  
   c) Hiçbiri, böyle bir blok yok
4. Pusula yönü (°) 200 olduğunda yön hangisidir?  
   a) Kuzey  
   b) Doğu  
   c) Güney
5. Dört yöne karar vermek için hangi yapı kullanılır?  
   a) Döngü  
   b) İç içe eğer-değilse  
   c) Değişken yaratma

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-c · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Pusula kavramı ve kalibrasyon ihtiyacı (10 dk), simülatörde/gerçek kartta kalibrasyon adımını deneme (10 dk), dört yön kodunu birlikte kurma (20 dk).
- **2. ders saati:** Logo dokunma olayını ekleme (10 dk), kendini dene 1-2 (15 dk), ileri seviye 3-4 (15 dk).
- Simülatörde kalibrasyon animasyonu gerçek kart kadar sezgisel olmayabilir; mümkünse gerçek kartla dışarıda veya pencere kenarında deneyin (iç mekânda metal eşyalar sapmaya sebep olabilir).
- "on logo pressed" gibi İngilizce blokları öğrencilere "her yazılım aracı sürekli güncellenir, çeviriler zamanla tamamlanır" diye normalleştirmek iyi bir fırsattır.
- 13. haftada sese geçiyoruz; bu hafta pusula ile ilgilenirken yorulan öğrenciler için güzel bir konu değişikliği olacak.
