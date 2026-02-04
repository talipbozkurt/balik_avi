# 📝 Balık Avı Ödevi - Öğrenci Kılavuzu

## 🎯 Görev

**Balık Avı** adlı kart oyununu C programlama diliyle geliştirin. **2 balık** oluşturan kazanır!

---

## 🚀 Hızlı Başlangıç (Codespaces)

### 1. Codespace Açın
GitHub Classroom'dan assignment'ı kabul ettikten sonra:
1. Repository sayfanızda **Code** → **Codespaces**
2. **Create codespace on main**
3. 1-2 dakika bekleyin

### 2. Kodunuzu Yazın
`balik_avi.c` dosyasını açın ve kodlamaya başlayın!

### 3. Test Edin
**Terminal'de:**
```bash
# Derle
clang -o balik_avi balik_avi.c

# Çalıştır
./balik_avi

# Otomatik test
python3 lab50.py .
```

### 4. GitHub'a Gönder
```bash
git add balik_avi.c
git commit -m "Ödev tamamlandı"
git push
```

---

## 📂 Dosya Yapısı

```
balik_avi/
├── balik_avi.c         ← SİZİN KODUNUZ (sadece bunu düzenleyin!)
├── lab50.py            ← Test motoru (DOKUNMAYIN!)
├── devcontainer.json   ← Codespaces ayarları (DOKUNMAYIN!)
└── README.md           ← Bu dosya
```

**⚠️ ÖNEMLI:** Sadece `balik_avi.c` dosyasını düzenleyin!

---

## 🎮 Oyun Kuralları

### 📦 Başlangıç
- **Deste:** 1-6 arası kartlar, her birinden **4 adet** (toplam 24 kart)
- **Dağıtım:** Her oyuncuya **6 kart**
- **Masa:** Kalan 12 kart masada (kapalı deste)

### 🎯 Oyun Hedefi
**Aynı numaradan 4 kart toplayarak "balık" oluşturun.**

🏆 **KAZANMA KOŞULLARI:**
- **2 balık** oluşturan **KAZANIR**
- Kartlar biterse **en fazla balık** yapan kazanır
- Eşitlik durumunda **berabere**

### 🔄 Oyun Akışı

#### 1️⃣ Oyuncunun Sırası
```
Hangi kart numarasını sormak istiyorsunuz? 2
```
- Oyuncu 1-6 arası bir numara seçer (elinde olan bir numara)
- **Bilgisayarda varsa:**
  - Tüm 2 numaralı kartlar oyuncuya verilir
  - Oyuncu **tekrar sorar** (sıra değişmez)
- **Bilgisayarda yoksa:**
  - Bilgisayar "Balık Avı!" der
  - Oyuncu masadan **1 kart çeker**
  - Sıra **bilgisayara geçer**

#### 2️⃣ Bilgisayarın Sırası
- Bilgisayar **rastgele** bir numara seçer (kendi elinden)
- **Oyuncuda varsa:**
  - Tüm o kartlar bilgisayara verilir
  - Bilgisayar **tekrar sorar**
- **Oyuncuda yoksa:**
  - Oyuncu "Balık Avı!" der
  - Bilgisayar masadan čeker
  - Sıra **oyuncuya geçer**

#### 3️⃣ Balık Oluşturma (Önemli!)
Elinizde **aynı karttan 4 tane** olduğunda:
```
🎉 Tebrikler! 2 numaralı karttan 4 adet topladınız. 1 balık kazandınız.
```
1. Bu 4 kart **elden çıkarılır**
2. Balık sayınız **+1** artar
3. **2 balık olduğunda KAZANIRSINIZ!**

### 🏁 Oyun Bitişi

Oyun şu durumlarda biter:
1. **Bir oyuncu 2 balık oluşturdu** → O oyuncu kazandı! 🏆
2. **Tüm kartlar bitti** → En fazla balık yapan kazandı
3. **Bir oyuncunun eli boşaldı** → Kartları sayılır

---

## 💻 Beklenen Çıktı Formatı

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
```

### Kart Var
```
Bilgisayarda 2 numaralı kart(lar) var! 2 2 verildi.

Yeni kartlarınız: 1 2 2 2 2 3 5 6
🎉 Tebrikler! 2 numaralı karttan 4 adet topladınız. 1 balık kazandınız.
Elinizden 2 numaralı kartlar çıkarıldı.

Oyuncunun yeni kartları: 1 3 5 6
Oyuncunun balık sayısı: 1 | Bilgisayarın balık sayısı: 0
Masadaki kalan kart sayısı: 12

Oyuncu yeniden soruyor.
```

### Balık Avı Durumu
```
Bilgisayarda 5 numaralı kart YOK.
Balık Avı ☹ Masadan bir kart çekiyorsunuz...
Masadan çekilen kart: 1

Oyuncunun yeni kartları: 1 3 5 6 1
```

### Bilgisayarın Sırası
```
--- TUR 2 ---
Bilgisayarın sırası.
Bilgisayar 6 numaralı kartı sordu.
Oyuncunun elinde 6 var! 6 verildi.
```

### Oyun Sonu
```
=== OYUN BİTTİ ===
Kazanan: OYUNCU!
Oyuncunun toplam balığı: 2
Bilgisayarın toplam balığı: 1
Masadaki kalan kart sayısı: 9
```

---

## 📊 Puanlama (100 Puan)

| Test | Puan | Açıklama |
|------|------|----------|
| ✅ Dosya var mı? | 0 | Zorunlu (puansız) |
| ✅ Syntax kontrolü | 5 | C99 öncesi syntax kuralları |
| ✅ **Derleme** | **40** | **En önemli!** Kod derlenip çalışıyor mu? |
| ✅ Başlangıç mesajları | 10 | Oyun başlığı, kart dağıtımı |
| ✅ Oyun döngüsü | 20 | Kullanıcı girişi, sıra değişimi |
| ✅ Oyun formatı | 25 | Tur bilgisi, masa kartları, balık sayıları |

---

## ⚠️ Dikkat Edilmesi Gerekenler

### 1. C99 Öncesi Syntax Kuralı (Eksi 5 Puan ❌)

**❌ YANLIŞ:**
```c
for (int i = 0; i < 10; i++) {  // For içinde int tanımı YASAK!
    printf("%d\n", i);
}
```

**✅ DOĞRU:**
```c
int i;  /* Önce fonksiyon başında tanımla */
for (i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```

### 2. Fonksiyon Kullanımı (Zorunlu!)

Kodunuz **fonksiyonlar kullanılarak** yazılmalıdır. Örnek:

```c
/* Desteyi hazırla */
void desteyi_hazirla(int deste[]);

/* Kartları dağıt */
void kartlari_dagit(int deste[], int *deste_indeksi, 
                    int oyuncu_el[], int *oyuncu_kart_sayisi,
                    int bilgisayar_el[], int *bilgisayar_kart_sayisi);

/* Kartları ekranda göster */
void kartlari_yazdir(int el[], int adet);

/* Kartları sırala */
void sirala(int el[], int adet);

/* Elde belirli bir kart var mı? */
int kart_sor(int el[], int adet, int hedef);

/* Elden kartı ver */
int kart_ver(int el[], int *adet, int hedef);

/* Ele kart ekle */
void kart_ekle(int el[], int *adet, int kart);

/* Balık kontrolü (4 aynı kart var mı?) */
int balik_kontrol(int el[], int *adet);
```

### 3. Diziler Kullanımı

```c
int deste[24];            // 24 kartlık deste
int oyuncu_el[30];        // Oyuncunun kartları (max 30)
int bilgisayar_el[30];    // Bilgisayarın kartları
```

### 4. Rastgelelik

```c
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));  // Rastgelelik için seed
    
    // Bilgisayar rastgele kart seçiyor
    int secim = rand() % 6 + 1;  // 1-6 arası
}
```

### 5. Geçersiz Girdi Kontrolü

```c
int secim;
printf("Hangi kart numarasını sormak istiyorsunuz? ");
scanf("%d", &secim);

if (secim < 1 || secim > 6) {
    printf("Geçersiz giriş! 1-6 arası bir sayı giriniz.\n");
    // Tekrar sor
}

// Kart elinde var mı kontrol et
if (kart_sor(oyuncu_el, oyuncu_kart_sayisi, secim) == 0) {
    printf("Elinizde %d numaralı kart yok!\n", secim);
    // Tekrar sor
}
```

### 6. Türkçe Karakter

Hem `ı` hem `i` kabul edilir:
- ✅ "Kartlar dağıtılıyor..."
- ✅ "Kartlar dagitiliyor..."
- ✅ "Balık Avı"
- ✅ "Balik Avi"

---

## 🐛 Sık Karşılaşılan Hatalar

### Hata 1: "For döngüsü içinde int tanımı"
```
Eksi 5 Puan: For döngüsü içinde 'int' tanımlaması yapılmış.
```
**Çözüm:** Tüm değişkenleri fonksiyon başında tanımlayın.

### Hata 2: "Derleme hatası"
```
error: use of undeclared identifier 'kart'
```
**Çözüm:** Değişkenleri kullanmadan önce tanımlayın.

### Hata 3: "Çıktıda oyun başlığı bulunamadı"
```
Çıktıda oyun başlığı 'BALIK AVI' bulunamadı.
```
**Çözüm:**
```c
printf("=== BALIK AVI KART OYUNU ===\n\n");
```

### Hata 4: "Kartlar dağıtılıyor mesajı eksik"
**Çözüm:**
```c
printf("Kartlar dağıtılıyor...\n\n");
```

### Hata 5: "Tur bilgisi gösterilmiyor"
**Çözüm:**
```c
printf("\n--- TUR %d ---\n\n", tur_sayisi);
```

---

## 📚 Fonksiyon Örnekleri

### Örnek 1: Desteyi Hazırla
```c
void desteyi_hazirla(int deste[]) {
    int i;
    int index = 0;
    int kart;
    
    /* 1-6 arası her karttan 4 tane */
    for (kart = 1; kart <= 6; kart++) {
        for (i = 0; i < 4; i++) {
            deste[index] = kart;
            index++;
        }
    }
    
    /* Karıştır (Fisher-Yates shuffle) */
    for (i = 23; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = deste[i];
        deste[i] = deste[j];
        deste[j] = temp;
    }
}
```

### Örnek 2: Kartları Yazdır
```c
void kartlari_yazdir(int el[], int adet) {
    int i;
    
    /* Önce sırala */
    sirala(el, adet);
    
    /* Yazdır */
    for (i = 0; i < adet; i++) {
        printf("%d ", el[i]);
    }
    printf("\n");
}
```

### Örnek 3: Balık Kontrolü
```c
int balik_kontrol(int el[], int *adet) {
    int kart;
    int i, j;
    int sayac;
    
    /* Her kart numarasını kontrol et */
    for (kart = 1; kart <= 6; kart++) {
        sayac = 0;
        
        /* Bu karttan kaç tane var? */
        for (i = 0; i < *adet; i++) {
            if (el[i] == kart) {
                sayac++;
            }
        }
        
        /* 4 tane varsa balık oluştu! */
        if (sayac == 4) {
            printf("🎉 Tebrikler! %d numaralı karttan 4 adet topladınız. ", kart);
            printf("1 balık kazandınız.\n");
            
            /* Bu kartları elden çıkar */
            kart_ver(el, adet, kart);
            
            return 1;  /* Balık oluştu */
        }
    }
    
    return 0;  /* Balık yok */
}
```

---

## 🎓 İpuçları

1. ✅ **Küçük adımlarla ilerleyin:**
   - İlk önce kart dağıtımını yapın
   - Sonra kullanıcı girişini ekleyin
   - En son bilgisayar stratejisini kodlayın

2. ✅ **Her adımda test edin:**
   ```bash
   clang -o balik_avi balik_avi.c && ./balik_avi
   ```

3. ✅ **printf() ile debug yapın:**
   ```c
   printf("DEBUG: Oyuncu kart sayısı: %d\n", oyuncu_kart_sayisi);
   ```

4. ✅ **Hata mesajlarını okuyun:**
   - Derleyici size satır numarası verir
   - Test çıktıları neyin yanlış olduğunu söyler

5. ✅ **Sık commit/push yapın:**
   - Her mantıklı değişiklikten sonra kaydedin
   - GitHub Actions'da sonucu kontrol edin

---

## 🚀 Başarı Kriterleri (Checklist)

Kodunuz şunları yapabilmeli:

- [ ] Derleniyor (40 puan - en önemli!)
- [ ] Oyun başlığı gösteriliyor
- [ ] 24 kartlık deste oluşturuluyor (1-6, her birinden 4 tane)
- [ ] Her oyuncuya 6 kart dağıtılıyor
- [ ] Kullanıcı 1-6 arası kart seçebiliyor
- [ ] Geçersiz girdiler kontrol ediliyor
- [ ] Bilgisayar cevap veriyor (Var/Yok/Balık Avı)
- [ ] Kart yoksa masadan çekiliyor
- [ ] 4 aynı kart olunca balık oluşuyor
- [ ] Balık sayıları gösteriliyor
- [ ] 2 balık yapan kazanıyor
- [ ] Tur bilgisi gösteriliyor
- [ ] Masa kartları gösteriliyor
- [ ] Oyun bitiş ekranı var

---

## 📞 Yardım

**Takıldığınızda:**
- Codespaces'te `python3 lab50.py .` çalıştırın
- Test çıktılarını **dikkatlice** okuyun
- GitHub Actions'daki hataları kontrol edin
- Örnek output'a bakın - tam olarak nasıl görünmeli?

**İyi çalışmalar! 🎮🐟**
