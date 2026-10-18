---
title: "16. Hafta – Fonksiyonlar ve listeler"
description: Tekrar eden kod parçalarını fonksiyonlarla kısaltıyor, birden çok değeri bir listede birlikte tutuyoruz.
sidebar:
  order: 16
hafta: 16
seviye: Blok
sure: 2 ders saati
kazanimlar:
  - Kendi fonksiyonunu oluşturup çağırır.
  - Bir liste oluşturur ve içine değer ekler.
  - Listeden rastgele bir değer seçen bir program yazar.
makecode: ""
video: ""
---

## Bu hafta ne öğreneceğiz?

Şimdiye kadar aynı blok dizisini birden çok yerde tekrar tekrar kullandık (örnek: 9. haftadaki refleks oyununda "simge göster, bekle, temizle" birkaç kez geçti). Bu hafta iki yeni araçla kod tekrarını azaltacağız: **fonksiyonlar** (kendi bloğunu yaratma) ve **listeler** (birden çok değeri tek bir kutuda tutma).

**Malzemeler:** micro:bit v2, USB kablo, bilgisayar.

---

## 1. Fonksiyon: kendi bloğunu yarat

**Gelişmiş** kategorisinin altında **Fonksiyonlar** alt kategorisi var; orada tek bir düğme görürsün: **Fonksiyon Yarat...**. Bu düğmeye basıp bir isim verdiğinde (örnek: "simgeGosterVeTemizle"), MakeCode senin için iki şey oluşturur:

1. İçine blok koyabileceğin bir **tanım** alanı (fonksiyonun ne yapacağı).
2. Programının her yerinde kullanabileceğin, o isimde **yeni bir blok**.

4. haftadaki Duygu Kartı'nı hatırla: A'ya basınca mutlu, B'ye basınca üzgün, A+B'ye basınca kalp simgesi gösteriliyordu. Üçünde de aynı iş tekrarlanıyor: **simge göster, biraz bekle, ekranı temizle** — sadece gösterilen simge değişiyor. Fonksiyon düzenleme ekranında bir **girdi** ekleyip ona "simge" adını verirsen, bu değişen kısmı fonksiyonun dışarıdan alacağı bir **parametre** yaparsın.

:::caution[Girdi türü: sadece dizgi/sayı/mantıksal/dizi]
Fonksiyon girdisi eklerken **"görsel" (simge) türü seçilemez** — sadece dizgi, sayı, mantıksal (doğru/yanlış) ve dizi seçebilirsin. Bu yüzden "simge" girdisini **dizgi** yapıp ("mutlu", "üzgün", "kalp" gibi), fonksiyonun içinde hangi simgenin gösterileceğine **eğer-değilse** ile karar vermen gerekir.
:::

![simgeGosterVeTemizle fonksiyonu: simge dizgi parametresi "mutlu" ise mutlu yüz, "uzgun" ise üzgün yüz, değilse kalp simgesi gösterilip 500 ms beklenir ve ekran temizlenir. A tuşuna basılınca "mutlu", B tuşuna basılınca "uzgun", A+B tuşuna basılınca "kalp" parametresiyle çağrılır.](./fonksiyon-ornegi.png)

**Canlı dene:** <a href="https://makecode.microbit.org/_31EAwViCVRfq" target="_blank" rel="noopener noreferrer">Bu projeyi MakeCode'da aç</a> ve simülatörde çalıştığını gör.

:::tip[Neden işimize yarar?]
"simgeGosterVeTemizle" içindeki blokları **üç yerde** tekrar tekrar sürüklemek yerine, her seferinde tek satırda "çağır simgeGosterVeTemizle" yazıp parantezin içine hangi simgeyi istediğini (dizgi olarak) söylersin. Bekleme süresini değiştirmek istersen (örnek: 500'den 800'e), sadece fonksiyonun içini bir kez değiştirirsin — üç yerde ayrı ayrı değil.
:::

---

## 2. Liste: birden çok değeri bir kutuda tutmak

Bir değişken tek bir değer tutar (5. hafta). **Liste** ise birden çok değeri sırayla tutar. **Değişkenler** kategorisi yerine **Gelişmiş → Diziler** alt kategorisinde bulunur:

| Blok | Ne yapar |
| --- | --- |
| dizini ... (+ ile eleman ekle) | Yazdığın değerlerle yeni bir liste oluşturur |
| sonuna değer ekle | Listenin sonuna bir eleman ekler |
| liste dizisi uzunluğu | Listede kaç eleman olduğunu söyler |
| listenin indeksli öğe değeri | Belirli bir sıradaki (0'dan başlayan) elemanı okur |
| rastgele değerini al | Listeden rastgele bir eleman seçer |

![Program başladığında görevler listesi [Zıpla, Şarkı söyle, Dans et] olarak ayarlanır. A tuşuna basılınca görevler listesinden rastgele seçilen bir görev ekranda gösterilir.](./gorev-secici-bloklari.png)

**Canlı dene:** <a href="https://makecode.microbit.org/_HYFCzoAsrRUb" target="_blank" rel="noopener noreferrer">Bu projeyi MakeCode'da aç</a> ve simülatörde çalıştığını gör.

**Rastgele görev seçici:** program başladığında **görevler** değişkenine, içinde üç dizgi olan bir **dizini ... yap** bloğuyla "Zıpla", "Şarkı söyle", "Dans et" listesi atanır (listedeki eleman sayısını **+** düğmesiyle artırırsın). A tuşuna basıldığında, listeden **rastgele değerini al** ile seçilen görev ekranda **dizgi göster** ile gösterilir.

:::note[0'dan başlar]
Bilgisayarlarda sıralama genelde 0'dan başlar: listenin ilk elemanı "0. sıradaki", ikincisi "1. sıradaki" elemandır. Bu, ilk derste kafa karıştırabilir — birlikte birkaç örnekle netleştirin.
:::

---

## Kendini dene

1. Kendi "selamVer" fonksiyonunu yaz ve iki farklı olaydan (A tuşu, B tuşu) çağır.
2. Görevler listesine kendi fikrini ekle (örnek: "Şarkı söyle" yerine "Şiir oku").
3. Listenin uzunluğunu ekranda gösteren bir blok ekle (**liste dizisi uzunluğu**).
4. `simgeGosterVeTemizle` fonksiyonuna ikinci bir girdi (**süre**) ekle, her çağrıda farklı bir bekleme süresi kullan (örnek: A'da 500 ms, B'de 1000 ms).

---

## Mini quiz

1. Fonksiyon oluşturmak için hangi kategoriye gidilir?  
   a) Değişkenler  
   b) Gelişmiş → Fonksiyonlar  
   c) Radyo
2. `simgeGosterVeTemizle` fonksiyonuna eklenen **simge** girdisi (parametre) ne işe yarar?  
   a) Fonksiyon her çağrıldığında farklı bir simge kullanılmasını sağlar  
   b) Fonksiyonu tamamen siler  
   c) Hiçbir işe yaramaz, sadece süslemedir
3. Bir listeye yeni eleman eklemek için hangi blok kullanılır?  
   a) sonuna değer ekle  
   b) liste dizisi uzunluğu  
   c) rastgele değerini al
4. Listelerde ilk eleman genelde hangi sıra numarasıyla anılır?  
   a) 1  
   b) 0  
   c) -1
5. "rastgele değerini al" bloğu ne yapar?  
   a) Listeyi siler  
   b) Listeden rastgele bir eleman seçer  
   c) Listeyi sıralar

<details>
<summary>Cevap anahtarı</summary>

1-b · 2-a · 3-a · 4-b · 5-b

</details>

---

## Öğretmen notu

- **1. ders saati:** Tekrar eden kod sorununu gösterme (4. haftadaki Duygu Kartı'nı hatırlatma, 10 dk), fonksiyon oluşturma ve girdi (parametre) ekleme adımlarını birlikte yapma (20 dk).
- **2. ders saati:** Liste kavramı ve 0'dan başlama (10 dk), rastgele görev seçiciyi kurma (15 dk), kendini dene (15 dk).
- "0'dan başlama" kavramı bu yaş grubu için en çok kafa karıştıran noktadır; parmaklarla sayma (0,1,2...) ya da sınıftaki öğrencileri sıraya dizip "0. öğrenci kim?" gibi bedensel bir örnekle somutlaştırmak işe yarar.
- Fonksiyonun "neden işe yaradığını" hissettirmek için önce fonksiyonsuz (tekrarlı) bir kodu, sonra fonksiyonlu hâlini yan yana göstermek etkili olur.
- Bu hafta Gelişmiş kategorisi ilk kez kullanılıyor; öğrenciler kategori listesinin kalabalıklaştığını fark edecek, bu normaldir.
- 17. haftada dokunmatik pinlerle blok döneminin son yeni konusuna geçiyoruz.
