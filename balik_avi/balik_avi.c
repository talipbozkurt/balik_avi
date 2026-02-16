#include "./myio.h"

#define KART_SAYISI 24
#define OYUNCU_BASLANGIC 6
#define MAX_EL 30
// Sabitler
#define KART_SAYISI 24 // Destede toplam kart (1-6 arası, her birinden 4 tane)
#define OYUNCU_BASLANGIC 6
#define MAX_EL 30 // Maksimum kart tutabilme kapasitesi

// Fonksiyon Prototipleri
void desteyi_hazirla(int deste[]);
void kartlari_dagit(int deste[], int *deste_indeksi, int oyuncu_el[],
                    int *oyuncu_kart_sayisi, int bilgisayar_el[],
                    int *bilgisayar_kart_sayisi);
void kartlari_yazdir(int el[], int adet);
void sirala(int el[], int adet);
int kart_sor(int el[], int adet, int hedef);
int kart_ver(
    int el[], int *adet,
    int hedef); // Verilen kartlari elden cikarir, kac tane verdigini doner
void kart_ekle(int el[], int *adet, int kart);
void kart_ekle_coklu(int el[], int *adet, int kart, int miktar);
int balik_kontrol(int el[], int *adet);

int main() {
  // Rastgelelik icin seed

  // Degiskenler
  int deste[KART_SAYISI];
  int oyuncu_el[MAX_EL];
  int bilgisayar_el[MAX_EL];

  // Kodunuzu buraya yaziniz...
  // Oyun dongusu ve mantigi burada kurulacak.

  printf("=== BALIK AVI KART OYUNU ===\n\n");

  return 0;
}
