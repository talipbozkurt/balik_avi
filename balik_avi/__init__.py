import check50
import check50.c
import re
import os

@check50.check()
def exists():
    """balik_avi.c dosyası mevcut mu?"""
    check50.exists("balik_avi.c")

@check50.check(exists, points=5)
def syntax_check():
    """Yasaklı syntax kontrolü (For içinde int tanımı vb.) (5 Puan)"""
    with open("balik_avi.c", "r", encoding="utf-8") as f:
        content = f.read()
        
    # C99 öncesi stil zorunluluğu: for(int i=0) tespiti
    if re.search(r"for\s*\(\s*int\s+", content):
        raise check50.Failure("Eksi 5 Puan: For döngüsü içinde 'int' tanımlaması yapılmış.\nDeğişkeni döngüden önce tanımlayınız (Örn: int i; for(i=0...))")

@check50.check(exists, points=40)
def compiles():
    """Kod derleniyor mu? (40 Puan)"""
    check50.c.compile("balik_avi.c", lcs50=False)

@check50.check(compiles, points=10)
def test_start():
    """Oyun başlangıç mesajları doğru mu? (10 Puan)"""
    output = check50.run("./balik_avi").stdout()
    
    if "BALIK AVI" not in output:
        raise check50.Failure("Çıktıda oyun başlığı bulunamadı.")
    
    # Beklenen: Kartlar dağıtılıyor...
    if "Kartlar dağıtılıyor" not in output and "Kartlar dagitiliyor" not in output:
        raise check50.Failure("'Kartlar dağıtılıyor...' mesajı eksik.")
        
    # Beklenen: Oyuncu kartları: ...
    if "Oyuncu kartları" not in output and "Oyuncu kartlari" not in output:
        raise check50.Failure("Oyuncunun kartları yazdırılmamış.")

@check50.check(compiles, points=20)
def test_game_loop():
    """Oyun döngüsü ve kullanıcı girişi doğru çalışıyor mu? (20 Puan)"""
    # Oyunu başlatıyoruz ve kullanıcıdan bir kart istemesini bekliyoruz
    # Örn: Elimizde muhtemelen olan veya olmayan bir sayı girelim. 
    # Not: Rastgelelik olduğu için kesin bir senaryo zordur, ancak input alıp devam ettiğini kontrol edebiliriz.
    
    prog = check50.run("./balik_avi")
    
    # Programın input beklemesi lazım, rastgele bir sayı (örn: 2) gönderelim
    prog.stdin("2")
    
    output = prog.stdout()
    
    # Kontrol 1: Bilgisayarın cevabı var mı?
    found_positive = "var" in output.lower() or "verildi" in output.lower()
    found_negative = "yok" in output.lower() or "balık avı" in output.lower() or "balik avi" in output.lower()
    
    if not (found_positive or found_negative):
        raise check50.Failure("Kullanıcı kart sorduktan sonra bilgisayarın cevabı (Var/Yok/Balık Avı) algılanamadı.")

    # Kontrol 2: Tur bilgisi
    if "TUR" not in output and "Tur" not in output:
         raise check50.Failure("Tur bilgisi (Örn: --- TUR 1 ---) ekrana yazdırılmalı.")

@check50.check(compiles, points=25)
def test_full_flow():
    """Oyun akışı ve format (25 Puan)"""
    # 3-4 el oynayarak programın çökmediğini ve akışın sürdüğünü test edelim
    prog = check50.run("./balik_avi")
    
    # Birkaç tahmin gönderelim.
    input_seq = ["1", "2", "3", "4", "5", "6"]
    
    try:
        for inp in input_seq:
            # Input gönder
            prog.stdin(inp)
            
        # Program hala çalışıyor veya düzgün bitmiş olmalı, çökmemeli
        out = prog.stdout()
        
    except Exception as e:
        raise check50.Failure(f"Oyun ardışık girişler sırasında hata verdi veya beklenmedik şekilde sonlandı: {e}")

    # Final kontrolleri
    if "Masadaki kalan kart sayısı" not in out and "Masa" not in out:
        raise check50.Failure("Her turda masadaki kalan kart sayısı gösterilmeli.")

