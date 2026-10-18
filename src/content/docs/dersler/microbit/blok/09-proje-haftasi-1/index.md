---
title: "9. Hafta – Proje haftası 1"
description: Şimdiye kadar öğrendiğimiz bütün blokları bir refleks oyununda birleştiriyoruz.
sidebar:
  order: 9
hafta: 9
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - Değişken, koşul, rastgele sayı ve buton bloklarını birlikte kullanır.
  - Bir problemi küçük adımlara (alt görevlere) bölerek çözer.
  - Kendi kodunu test edip hatasını (bug) bulur ve düzeltir.
makecode: ""
video: ""
---

## Bu hafta ne yapacağız?

2–8. haftalarda birer birer öğrendiğimiz blokları (butonlar, değişkenler, koşullar, rastgele sayı, döngüler) bu hafta tek bir projede birleştiriyoruz: **refleks oyunu**. Bu, yeni bir konu haftası değil; bildiklerimizi kullanarak gerçek bir şey inşa ettiğimiz bir **proje haftası**.

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Önce plan, sonra kod

Her projede olduğu gibi önce ne yapacağımızı adım adım yazarız, sonra bloklara dökeriz:

1. Oyun "yıldız" simgesini gösterip bekler (oyuncu hazırlanır).
2. Rastgele bir süre (1–3 saniye) bekler — oyuncu ne zaman geleceğini bilmez.
3. Ekranda "evet" simgesi gösterir ve aynı anda bir sayaç (süre) saymaya başlar.
4. Oyuncu A düğmesine basınca sayaç durur ve süre (yaklaşık tepki hızı) ekranda gösterilir.
5. Eğer oyuncu simge çıkmadan düğmeye basarsa (erken basma), "X" simgesi gösterilir ve oyun baştan başlar.

Bu adımların hangisi **değişken**, hangisi **rastgele sayı**, hangisi **koşul** gerektiriyor? Kodu yazmadan önce bunu tahmin etmek, projeyi kolaylaştırır.

---

## 2. Hangi blok nerede işimize yarıyor?

| İhtiyaç | Hangi haftadan? | Blok |
| --- | --- | --- |
| Bekleme süresini tutmak | 5. hafta (Değişkenler) | değişken yarat, … değişkenini … yap |
| Rastgele bekleme | 7. hafta (Rastgele sayılar) | rastgele değer seçimi |
| Düğmeye basılma | 4. hafta (Butonlar) | A tuşuna basıldığında |
| Erken mi geç mi basıldı kontrolü | 6. hafta (Koşullar) | eğer … ise / değilse |
| Süreyi artırarak saymak | 8. hafta (Döngüler) | her zaman / … kere tekrarla |

<div class="etkinlik">
Projelerde yeni blok öğrenmeyiz; <strong>bildiğimiz blokları doğru sırada birleştiririz</strong>. Gerçek mühendislik işi budur.
</div>

---

## 3. Refleks oyununu kur

**program başladığında:**

1. `hazir` değişkenini `yanlış` yap.

**her zaman:** (`hazir` yanlış olduğu sürece tekrar eder)

1. Yıldız simgesini göster.
2. 1 ile 3 arasında rastgele bir sayı seç, o kadar saniye bekle.
3. Ekranı temizle.
4. `baslangic` değişkenini 0 yap (sayaç sıfırlansın).
5. `hazir` değişkenini `doğru` yap (artık oyuncu basabilir).
6. Evet simgesini göster.

**A tuşuna basıldığında:**

1. `hazir` doğru ise: `baslangic` değişkenini 1 artır, süreyi göster, `hazir` değişkenini `yanlış` yap.
2. Değilse (erken basılmışsa): X simgesini göster.

:::tip[Basitten başla]
Önce sadece "düğmeye basınca simge göster" kısmını yaptır, çalıştığını simülatörde gör. Sonra rastgele beklemeyi ekle, sonra erken basma kontrolünü ekle. Her adımda test et — hepsini birden yazıp sonunda hatayı aramak çok daha zor olur.
:::

---

## Kendini dene

1. Oyunu zorlaştır: bekleme süresini 1–3 yerine 2–5 saniye yap.
2. En iyi (en kısa) süreyi bir değişkende saklayıp ekranda "rekor" olarak göster.
3. Oyuna 3 hak tanı: 3 kez erken basarsa oyun bir melodiyle bitsin.
4. Kendi projeni seç: 2–8. haftalardaki blokları kullanarak kendi küçük oyununu tasarla (örnek: sayı tahmin oyunu, basit alarm, ışıklı metronom).

---

## Mini quiz

1. Bu hafta neden yeni blok öğrenmedik?  
   a) Bloklar bozuldu  
   b) Bildiklerimizi birleştirip proje yaptık  
   c) Zaman yetmedi
2. Rastgele bekleme süresi için hangi blok kullanılır?  
   a) eğer-ise  
   b) rastgele değer seçimi  
   c) tekrarla
3. Erken basmayı yakalamak için hangi yapı gerekir?  
   a) Döngü  
   b) Koşul (eğer-değilse)  
   c) Değişken yaratma
4. Bir projeyi kodlamaya başlamadan önce ne yapmalıyız?  
   a) Hemen blok sürüklemeye başlamalı  
   b) Adımları sırayla planlamalı  
   c) Kartı kapatıp açmalı
5. "Her adımda test et" önerisi neden önemli?  
   a) Hatayı erken bulmak için  
   b) Kodu uzatmak için  
   c) Zorunlu değil, önemsiz

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-b · 3-b · 4-b · 5-a

</details>

---

## Öğretmen notu

- **1. ders saati:** Planlama (adımları tahtaya/kağıda yazma, 10 dk), hangi blok nerede tablosunu birlikte doldurma (10 dk), temel iskeleti kurma — sadece düğmeye basınca simge (20 dk).
- **2. ders saati:** Rastgele bekleme ve erken basma kontrolünü ekleme (20 dk), test ve hata ayıklama (10 dk), kendini dene / serbest proje (10 dk).
- Bu hafta öğretmenin rolü çözüm vermek değil, soru sormaktır: "Bu değişkeni neden ekledin?", "Bu koşul olmasa ne olur?"
- Hızlı bitirenler için "serbest proje" seçeneği (Kendini dene 4) hazır bulundurun; yavaş ilerleyenler için sadece 3. bölümdeki temel oyunu bitirmek yeterli bir hedeftir.
- 10. haftadan itibaren yeni sensörlere geçiyoruz; bu hafta özgüven kazanan öğrenciler yeni konulara daha rahat atılır.
