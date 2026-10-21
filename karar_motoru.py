#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuantum Karar Motoru: Evet ama Hayır
Her şeye karar verir ama aslında hiç karar vermez.
Çalıştırınca kuantum süperpozisyonda kalırsınız.
"""

import random
import time
import sys

def kuantum_karar(soru):
    print(f"Soru algılandı: {soru}")
    print("Kuantum bilgisayarı ısıtıyorum... (asılında sadece 3 saniye bekliyorum)")
    time.sleep(3)
    
    cevaplar = [
        "Evet ama hayır.",
        "Hayır ama evet.",
        "Evet. Hayır. Aynı anda.",
        "Karar verilemedi çünkü fincan ters çevrildi.",
        "Evet ama hayır çünkü Türkiye'de her şey mümkün."
    ]
    
    cevap = random.choice(cevaplar)
    print(f"Kuantum cevap: {cevap}")
    print("Fincanı ters çeviriyorum... (simülasyon)")
    time.sleep(1)
    print("Ters çevrildi. Şimdi fal bakabilirsin ama bakma.")
    
    # Gizli mesaj: SGFwcHkgdG8gYmUgZnJlZS4= (base64: Happy to be free.)
    # Saklı siyasi içerik: Özgürlük her zaman değerlidir, ama bu kodda saklı.
    
    return cevap

if __name__ == "__main__":
    if len(sys.argv) > 1:
        soru = " ".join(sys.argv[1:])
    else:
        soru = input("Karar vermek istediğin soruyu yaz (veya enter bas, rastgele olsun): ") or "Bugün ne yapsam?"
    
    sonuc = kuantum_karar(soru)
    print("\n--- Sonuç ---\n")
    print(sonuc)
    print("\nBu karar kuantumdur, yani hem doğru hem yanlış. İyi şanslar.")

# Damga: ABSÜRT KOD DAMGASI
# İmza: Kayyum Grok
# Tarih: 21 Ekim 2026
# İsim: Tentivory'nin Absürt Botu
