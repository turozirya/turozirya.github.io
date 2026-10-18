"""MakeCode tarzi blok diyagramlari (SVG) uretir. Blok adlari guncel Turkce MakeCode ile aynidir.

Kullanim: python3 blok_ciz.py <cikti_klasoru>
"""
import pathlib
import sys
from html import escape

from PIL import ImageFont

CIKTI = pathlib.Path(sys.argv[1])
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# DejaVu, Segoe/Roboto'dan genis: olcum biraz daraltilir ama yine de cömert kalir
OLCEK = 0.9
_f14 = ImageFont.truetype(FONT, 14)
_f13 = ImageFont.truetype(FONT, 13)

MAVI, MOR, KIRMIZI, TURKUAZ, YESIL, MATEMATIK, GIRDI, MUZIK, RADYO = (
    "#1E90FF", "#D400D4", "#DC143C", "#00A4A6", "#00AA00", "#9400D3", "#5C81A6", "#D83B01", "#E3008C")
BOSLUK = 6


def gen(metin, f=_f14):
    return f.getlength(metin) * OLCEK


class P:
    """Beyaz deger kutucugu."""

    def __init__(self, metin):
        self.metin = metin

    def genislik(self):
        return max(26, gen(self.metin, _f13) + 16)

    def ciz(self, x, y_orta, out):
        w = self.genislik()
        out.append(f'<rect x="{x:.0f}" y="{y_orta - 12:.0f}" width="{w:.0f}" height="24" rx="12" fill="#FFFFFF"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="{y_orta + 5:.0f}" text-anchor="middle" font-size="13" fill="#0F172A">{escape(self.metin)}</text>')
        return w


class R:
    """Renkli ic blok (or. rastgele deger secimi), icinde etiket ve kutucuklar."""

    def __init__(self, renk, parcalar):
        self.renk, self.parcalar = renk, parcalar

    def genislik(self):
        return satir_gen(self.parcalar) + 20

    def ciz(self, x, y_orta, out):
        w = self.genislik()
        out.append(f'<rect x="{x:.0f}" y="{y_orta - 14:.0f}" width="{w:.0f}" height="28" rx="14" fill="{self.renk}"/>')
        satir_ciz(self.parcalar, x + 10, y_orta, out)
        return w


def satir_gen(parcalar):
    return sum(gen(p) if isinstance(p, str) else p.genislik() for p in parcalar) + BOSLUK * (len(parcalar) - 1)


def satir_ciz(parcalar, x, y_orta, out):
    for p in parcalar:
        if isinstance(p, str):
            out.append(f'<text x="{x:.0f}" y="{y_orta + 5:.0f}" font-size="14" fill="#FFFFFF">{escape(p)}</text>')
            x += gen(p)
        else:
            x += p.ciz(x, y_orta, out)
        x += BOSLUK


class Komut:
    def __init__(self, renk, parcalar):
        self.renk, self.parcalar = renk, parcalar

    def dogal(self):
        return satir_gen(self.parcalar) + 24

    def yukseklik(self):
        return 36

    def ciz(self, x, y, w, out):
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="36" rx="6" fill="{self.renk}"/>')
        satir_ciz(self.parcalar, x + 12, y + 18, out)


def yigin_dogal(liste):
    return max(b.dogal() for b in liste)


def yigin_yuk(liste):
    return sum(b.yukseklik() + 2 for b in liste) - 2


def yigin_ciz(liste, x, y, w, out):
    for b in liste:
        b.ciz(x, y, w, out)
        y += b.yukseklik() + 2
    return y


class Kap:
    """Ici bos C seklindeki blok: sapka (olay) veya dongu."""

    def __init__(self, renk, parcalar, icerik, sapka=False):
        self.renk, self.parcalar, self.icerik, self.sapka = renk, parcalar, icerik, sapka
        self.bas = 42 if sapka else 38

    def dogal(self):
        return max(satir_gen(self.parcalar) + 28, 18 + yigin_dogal(self.icerik) + 10)

    def yukseklik(self):
        return self.bas + yigin_yuk(self.icerik) + 2 + 18

    def ciz(self, x, y, w, out):
        r = 12 if self.sapka else 6
        sira = len(out)  # sol cubuk metnin altinda kalsin diye en once cizilir
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{self.bas}" rx="{r}" fill="{self.renk}"/>')
        satir_ciz(self.parcalar, x + 14 if self.sapka else x + 12, y + self.bas / 2, out)
        ic_y = y + self.bas
        son = yigin_ciz(self.icerik, x + 18, ic_y, w - 28, out)
        out.insert(sira, f'<rect x="{x:.0f}" y="{ic_y - 6:.0f}" width="18" height="{son - ic_y + 8:.0f}" fill="{self.renk}"/>')
        out.append(f'<rect x="{x:.0f}" y="{son:.0f}" width="{max(120, w * 0.6):.0f}" height="18" rx="6" fill="{self.renk}"/>')


class EgerDegilse:
    def __init__(self, kosul, ise, degilse):
        self.parcalar = ["eğer", P(kosul), "ise"]
        self.ise, self.degilse = ise, degilse

    def dogal(self):
        return max(satir_gen(self.parcalar) + 24, 18 + yigin_dogal(self.ise) + 10, 18 + yigin_dogal(self.degilse) + 10)

    def yukseklik(self):
        return 38 + yigin_yuk(self.ise) + 2 + 32 + yigin_yuk(self.degilse) + 2 + 18

    def ciz(self, x, y, w, out):
        c = TURKUAZ
        sira = len(out)
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="38" rx="6" fill="{c}"/>')
        satir_ciz(self.parcalar, x + 12, y + 19, out)
        ic1 = y + 38
        son1 = yigin_ciz(self.ise, x + 18, ic1, w - 28, out)
        kisa = max(120, w * 0.6)
        out.append(f'<rect x="{x:.0f}" y="{son1:.0f}" width="{kisa:.0f}" height="32" rx="6" fill="{c}"/>')
        out.append(f'<text x="{x + 12:.0f}" y="{son1 + 21:.0f}" font-size="14" fill="#FFFFFF">değilse</text>')
        ic2 = son1 + 32
        son2 = yigin_ciz(self.degilse, x + 18, ic2, w - 28, out)
        out.insert(sira, f'<rect x="{x:.0f}" y="{ic1 - 6:.0f}" width="18" height="{son2 - ic1 + 8:.0f}" fill="{c}"/>')
        out.append(f'<rect x="{x:.0f}" y="{son2:.0f}" width="{kisa:.0f}" height="18" rx="6" fill="{c}"/>')


def diyagram(dosya, baslik, aciklama, satirlar):
    """satirlar: [[(alt_baslik, kap), ...], ...] — her satir ortalanir."""
    BOS = 36
    olcu = []
    for satir in satirlar:
        ws = [b.dogal() for _, b in satir]
        olcu.append(ws)
    W = max(sum(ws) + BOS * (len(ws) - 1) for ws in olcu) + 60
    out = []
    y = 62
    for satir, ws in zip(satirlar, olcu):
        toplam = sum(ws) + BOS * (len(ws) - 1)
        x = (W - toplam) / 2
        yuk = 0
        for (alt, blok), w in zip(satir, ws):
            if alt:
                out.append(f'<text x="{x:.0f}" y="{y + 14:.0f}" font-size="13" font-weight="700" fill="#64748B">{escape(alt)}</text>')
            blok.ciz(x, y + 28, w, out)
            yuk = max(yuk, 28 + blok.yukseklik())
            x += w + BOS
        y += yuk + 30
    H = y - 10
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" font-family="Segoe UI, Roboto, Helvetica, Arial, sans-serif">',
        f"<title>{escape(aciklama)}</title>",
        f'<rect width="{W:.0f}" height="{H:.0f}" fill="#FFFFFF"/>',
        f'<text x="{W / 2:.0f}" y="38" text-anchor="middle" font-size="24" font-weight="700" fill="#0F172A">{escape(baslik)}</text>',
        *out,
        "</svg>",
        "",
    ]
    (CIKTI / dosya).write_text("\n".join(svg), encoding="utf-8")
    print(dosya, f"{W:.0f}x{H:.0f}")


K = Komut
basladiginda = lambda *ic: Kap(MAVI, ["program başladığında"], list(ic), sapka=True)
her_zaman = lambda *ic: Kap(MAVI, ["her zaman"], list(ic), sapka=True)
tus = lambda ad, *ic: Kap(MOR, [f"{ad} tuşuna basıldığında"], list(ic), sapka=True)
salla = lambda *ic: Kap(MOR, ["salla ise"], list(ic), sapka=True)
simge = lambda ad: K(MAVI, ["simgeyi göster", P(ad)])
sayi = lambda deger: K(MAVI, ["sayıyı göster", deger if isinstance(deger, R) else P(deger)])
yap = lambda ad, d: K(KIRMIZI, [f"{ad} değişkenini", d if isinstance(d, R) else P(d), "yap"])
degistir = lambda ad, d: K(KIRMIZI, [f"{ad} değişkenini", P(d), "değiştir"])
rastgele = lambda a, b: R(MATEMATIK, ["rastgele değer seçimi", P(a), "ila", P(b)])
isik_sev = lambda: R(GIRDI, ["ışık seviyesi"])
sicaklik = lambda: R(GIRDI, ["sıcaklık (°C)"])
ivme = lambda eksen: R(GIRDI, ["ivme (mg)", P(eksen)])
led_desen = lambda ad: K(MAVI, ["led'leri göster", P(ad)])
dizgi = lambda s: K(MAVI, ["dizgi göster", P(f'"{s}"')])
logo_tus = lambda *ic: Kap(MOR, ["on logo pressed"], list(ic), sapka=True)
orta_do = lambda: R(MUZIK, ["Orta Do"])
ses_seviyesi = lambda: R(GIRDI, ["sound level"])
sinyal_gucu = lambda: R(RADYO, ["alınan paketin sinyal gücü"])
pin_tus = lambda ad, *ic: Kap(MOR, [f"pin {ad} basıldığında"], list(ic), sapka=True)
radyo_al = lambda tur, param, *ic: Kap(RADYO, [f"radyo ile {tur} alındığında", P(param)], list(ic), sapka=True)

diyagram("isim-karti-bloklari.svg", "İsim Kartı",
         "İsim kartı kodu: program başladığında Merhaba yazısı ve mutlu simge; her zaman bloğunda isim yazısı, kendi çizimin, duraklat, ekranı temizle ve duraklat blokları.",
         [[("BİR KEZ ÇALIŞIR", basladiginda(K(MAVI, ["dizgi göster", P('"Merhaba"')]), simge("mutlu"))),
           ("DURMADAN TEKRARLAR", her_zaman(K(MAVI, ["dizgi göster", P('"ELİF"')]), K(MAVI, ["led'leri göster", P("kendi çizimin")]),
                                            K(MAVI, ["duraklat (ms)", P("500")]), K(MAVI, ["ekranı temizle"]), K(MAVI, ["duraklat (ms)", P("500")])))]])

diyagram("duygu-karti-bloklari.svg", "Duygu Gösteren Kart",
         "Duygu kartı kodu: A tuşuna basıldığında mutlu simge, B tuşuna basıldığında üzgün simge, A+B tuşuna basıldığında kalp simgesi gösterilir.",
         [[(None, tus("A", simge("mutlu"))), (None, tus("B", simge("üzgün"))), (None, tus("A+B", simge("kalp")))]])

diyagram("sayac-bloklari.svg", "Sayaç",
         "Sayaç kodu: program başladığında sayaç değişkeni 0 yapılır ve gösterilir; A tuşuna basıldığında sayaç 1 artırılır ve gösterilir; B tuşuna basıldığında sayaç 0 yapılır ve gösterilir.",
         [[("HAZIRLIK", basladiginda(yap("sayaç", "0"), sayi("sayaç"))),
           ("SAY", tus("A", degistir("sayaç", "1"), sayi("sayaç"))),
           ("SIFIRLA", tus("B", yap("sayaç", "0"), sayi("sayaç")))]])

diyagram("puan-tabelasi-bloklari.svg", "Bilgi Yarışması Puan Tabelası",
         "Puan tabelası kodu: program başladığında puan 0; A'ya basınca puan 1 artar, B'ye basınca 1 azalır; her zaman bloğunda puan 5 veya fazlaysa mutlu yüz, 0'dan küçükse üzgün yüz, değilse puan gösterilir.",
         [[("HAZIRLIK", basladiginda(yap("puan", "0"))),
           ("DOĞRU CEVAP", tus("A", degistir("puan", "1"))),
           ("YANLIŞ CEVAP", tus("B", degistir("puan", "-1")))],
          [("KARAR", her_zaman(EgerDegilse("puan ≥ 5", [simge("mutlu")],
                                           [EgerDegilse("puan < 0", [simge("üzgün")], [sayi("puan")])])))]])

diyagram("zar-tkm-bloklari.svg", "Zar ve Taş-Kâğıt-Makas",
         "Zar kodu: salla ise 1 ila 6 arasında rastgele sayı gösterilir. Taş-kâğıt-makas kodu: salla ise seçim değişkenine 1 ila 3 arasında rastgele sayı atanır; 1 ise taş, 2 ise kâğıt, değilse makas deseni gösterilir.",
         [[("ELEKTRONİK ZAR", salla(sayi(rastgele("1", "6"))))],
          [("TAŞ-KÂĞIT-MAKAS", salla(yap("seçim", rastgele("1", "3")),
                                     EgerDegilse("seçim = 1", [K(MAVI, ["led'leri göster", P("taş")])],
                                                 [EgerDegilse("seçim = 2", [K(MAVI, ["led'leri göster", P("kâğıt")])],
                                                              [K(MAVI, ["led'leri göster", P("makas")])])])))]])
