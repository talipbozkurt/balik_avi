# 🎮 Balık Avı - Kart Oyunu Ödevi

## 📚 Genel Bilgiler

Bu ödev, **Balık Avı** adlı bir kart oyununu C programlama diliyle geliştirmenizi bekliyor. Oyun, siz ve bilgisayar arasında 2 balık oluşturmaya çalıştığınız bir strateji oyunudur.

---

## 🚀 Nasıl Başlarım?

### 1. GitHub Classroom'dan Assignment'ı Kabul Et
Öğretmeninizin verdiği linke tıklayın ve assignment'ı kabul edin.

### 2. GitHub Codespaces'i Aç
1. Repository sayfanızda **Code** butonuna tıklayın
2. **Codespaces** sekmesini seçin
3. **Create codespace on main** butonuna tıklayın
4. Codespace açılana kadar bekleyin (1-2 dakika)

**✅ Artık kodlamaya başlayabilirsiniz!** Hiçbir şey kurmanıza gerek yok.

### 3. Kodunuzu Yazın
- `balik_avi/balik_avi.c` dosyasını açın
- Kodunuzu yazın ve kaydedin

### 4. Codespaces'te Test Edin
**Terminal'de şu komutları çalıştırın:**

```bash
# Derleme
clang -o balik_avi balik_avi/balik_avi.c

# Çalıştırma
./balik_avi

# Otomatik testler (opsiyonel)
python3 balik_avi/lab50.py balik_avi
```

### 5. GitHub'a Gönder
```bash
git add balik_avi/balik_avi.c
git commit -m "Ödev tamamlandı"
git push
```

### 6. Sonuçları Kontrol Et
1. Repository sayfanıza gidin
2. **Actions** sekmesine tıklayın
3. En son commit'inizin test sonucunu görün

---

## 📊 Otomatik Puanlama Sistemi

Her `git push` yaptığınızda kodunuz **otomatik olarak** test edilir ve puanlanır.

### Puan Dağılımı (100 Puan)

| Test Adı | Puan | Açıklama |
|----------|------|----------|
| ✅ Dosya Kontrolü | 0 | Zorunlu (puansız) |
| ✅ Syntax Kontrolü | 5 | C99 öncesi syntax kuralları |
| ✅ Derleme | 40 | **En önemli!** Kod derlenip çalışıyor mu? |
| ✅ Başlangıç Mesajları | 10 | Oyun başlığı, kart dağıtımı |
| ✅ Oyun Döngüsü | 20 | Kullanıcı girişi, sıra değişimi |
| ✅ Oyun Formatı | 25 | Tur bilgisi, masa kartları, balık sayısı |

### Test Sonuçları Nereden Görülür?

**GitHub'da:**
1. Repository → **Actions** sekmesi
2. Son commit'inizin durumunu kontrol edin (✅ veya ❌)
3. Detaylar için tıklayın

**Örnek Çıktı:**
```
🚀 Yerel Test Motoru Başladı
==================================================
[*] exists                    (Kontrol) ✅ PASS
[*] syntax_check              (5 Puan)  ✅ PASS
[*] compiles                  (40 Puan) ✅ PASS
[*] test_start                (10 Puan) ✅ PASS
[*] test_game_loop            (20 Puan) ❌ FAIL
    👉 Bilgisayarın cevabı algılanamadı
[*] test_full_flow            (25 Puan) ✅ PASS
==================================================
Sonuç: 5/6 Test Başarılı
🏆 TOPLAM PUAN: 75 / 100
```

---

## 🎯 Oyun Kuralları

### Başlangıç
- **Deste:** 1-6 arası kartlar, her birinden **4 adet** (toplam 24 kart)
- **Dağıtım:** Her oyuncuya **6 kart**
- **Masa:** Kalan 12 kart masada (kapalı)

### Oyun Hedefi
**Aynı numaradan 4 kart toplayarak "balık" oluşturun.**
- **2 balık** oluşturan **kazanır** 🏆
- Kartlar biterse en fazla balık yapan kazanır
- Eşitlik durumunda **berabere**

### Oyun Akışı

#### 1️⃣ Oyuncunun Sırası
```
Hangi kart numarasını sormak istiyorsunuz? 2
```
- Oyuncu 1-6 arası bir numara seçer
- **Bilgisayarda varsa:** Tüm 2'leri alır ve **tekrar sorar**
- **Bilgisayarda yoksa:** "Balık Avı!" der, masadan 1 kart çeker, sıra bilgisayara geçer

#### 2️⃣ Bilgisayarın Sırası
- Bilgisayar rastgele bir numara sorar
- **Oyuncuda varsa:** Bilgisayar alır ve tekrar sorar
- **Oyuncuda yoksa:** Bilgisayar masadan çeker, sıra size geçer

#### 3️⃣ Balık Oluşturma
Elinizde **aynı karttan 4 tane** olduğunda:
```
🎉 Tebrikler! 2 numaralı karttan 4 adet topladınız. 1 balık kazandınız.
```
- Bu 4 kart **elden çıkar**
- **Balık sayısı +1** olur

### Oyun Sonu
- **2 balık** yapan kazanır
- Veya kartlar bittiğinde en fazla balık yapan kazanır

---

## ⚠️ Önemli Kurallar

### 1. C99 Öncesi Syntax (Eksi 5 Puan ❌)

**❌ YANLIŞ:**
```c
for (int i = 0; i < 10; i++) {  // For içinde int tanımı yasak!
    printf("%d\n", i);
}
```

**✅ DOĞRU:**
```c
int i;  /* Önce tanımla */
for (i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

### 2. Fonksiyon Kullanımı (Zorunlu)
Kodunuz **fonksiyonlar** kullanarak yazılmalı. Örnek:
```c
void desteyi_hazirla(int deste[]);
void kartlari_dagit(...);
int balik_kontrol(int el[], int *adet);
```

### 3. Diziler ve Rastgelelik
- Kartları **dizilerde** tutun
- Bilgisayar seçimi `rand()` ile yapılmalı

---

## 📝 Beklenen Çıktı Formatı

### Başlangıç
```
=== BALIK AVI KART OYUNU ===

Kartlar dağıtılıyor...

Oyuncu kartları: 1 2 2 3 5 6
Bilgisayar kartları: [Gizli]  
Bilgisayar kart sayısı: 6
Masadaki kalan kart sayısı: 12
```

### Her Tur
```
--- TUR 1 ---

Oyuncunun balık sayısı: 0 | Bilgisayarın balık sayısı: 0
Oyuncu kartları: 1 2 2 3 5 6
Hangi kart numarasını sormak istiyorsunuz? 2

Bilgisayarda 2 numaralı kart(lar) var! 2 2 verildi.

Yeni kartlarınız: 1 2 2 2 2 3 5 6
🎉 Tebrikler! 2 numaralı karttan 4 adet topladınız. 1 balık kazandınız.
Elinizden 2 numaralı kartlar çıkarıldı.

Oyuncunun yeni kartları: 1 3 5 6
Oyuncunun balık sayısı: 1 | Bilgisayarın balık sayısı: 0
```

### Balık Avı Durumu
```
Bilgisayarda 5 numaralı kart YOK.
Balık Avı ☹ Masadan bir kart çekiyorsunuz...
Masadan çekilen kart: 1
```

### Oyun Sonu
```
=== OYUN BİTTİ ===
Kazanan: OYUNCU!
Oyuncunun toplam balığı: 2
Bilgisayarın toplam balığı: 1
Masadaki kalan kart sayısı: 6
```

---

## 🛠️ Sık Karşılaşılan Hatalar

### ❌ "Derleme Hatası"
```
error: use of undeclared identifier 'x'
```
**Çözüm:** Tüm değişkenleri fonksiyon başında tanımlayın

### ❌ "For içinde int tanımı"
```
Eksi 5 Puan: For döngüsü içinde 'int' tanımlaması yapılmış.
```
**Çözüm:** Değişkeni döngüden **önce** tanımlayın

### ❌ "Çıktı formatı yanlış"
```
'Kartlar dağıtılıyor...' mesajı eksik.
```
**Çözüm:** Mesajları **tam olarak** örnekteki gibi yazdırın

---

## 🎓 Başarı İpuçları

1. ✅ **Küçük adımlarla ilerleyin** - Her fonksiyonu ayrı test edin
2. ✅ **Sık kaydedin ve push yapın** - İlerlemenizi takip edin
3. ✅ **Test çıktılarını okuyun** - Size neyi yanlış yaptığınızı söyler
4. ✅ **Örnek output'a bakın** - Tam olarak nasıl görünmeli?
5. ✅ **Codespaces'te test edin** - GitHub'a göndermeden önce

---

## 📞 Yardım

**Takıldığınız yerlerde:**
- GitHub Actions'daki hata mesajlarını okuyun
- Örnek output'u kontrol edin
- Codespaces'te `python3 balik_avi/lab50.py balik_avi` çalıştırın

**İyi çalışmalar! 🎮�**
