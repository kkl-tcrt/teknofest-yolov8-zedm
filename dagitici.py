import os
import shutil
import random

# 1. Klasör isimlerini belirliyoruz
kaynak = 'foto' 
hedef = '.' 

# 2. Train ve Val klasörlerini sıfırdan oluşturuyoruz
for t in ['train', 'val']:
    for alt in ['images', 'labels']:
        os.makedirs(os.path.join(hedef, t, alt), exist_ok=True)

# 3. 'foto' içindeki tüm resimleri listeliyoruz
resimler = [f for f in os.listdir(kaynak) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
print(f"Toplam {len(resimler)} adet resim bulundu. İşlem başlıyor...")

# 4. Rastgele karıştırıyoruz (Generalization için kritik)
random.shuffle(resimler)

# 5. %80 Train, %20 Val ayrımı
sinir = int(len(resimler) * 0.8)
train_set = resimler[:sinir]
val_set = resimler[sinir:]

def karsiya_yukle(liste, tip):
    basari = 0
    for r_adi in liste:
        # Resmi kopyala
        shutil.copy(os.path.join(kaynak, r_adi), os.path.join(hedef, tip, 'images', r_adi))
        
        # Aynı isimli etiketi (.txt) bul ve kopyala
        e_adi = r_adi.rsplit('.', 1)[0] + '.txt'
        e_yolu = os.path.join(kaynak, e_adi)
        if os.path.exists(e_yolu):
            shutil.copy(e_yolu, os.path.join(hedef, tip, 'labels', e_adi))
            basari += 1
    return basari

# 6. Kopyalamayı başlat
t_say = karsiya_yukle(train_set, 'train')
v_say = karsiya_yukle(val_set, 'val')

print(f"Başarıyla tamamlandı!")
print(f"Train: {t_say} resim/etiket | Val: {v_say} resim/etiket")