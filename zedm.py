import cv2

def kamerayi_bul_ve_ac():
    # 0'dan 5'e kadar tüm indeksleri dene
    for i in range(5):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW) # Windows için en hızlı açma yöntemi
        
        # ZED-M'in özel çözünürlüğünü ayarla
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        
        ret, frame = cap.read()
        if ret:
            # Eğer gelen görüntü çok genişse (3840 piksel), bu kesin ZED-M'dir!
            if frame.shape[1] > 1920:
                print(f" ZED-M Bulundu! İndeks: {i}")
                return cap, i
        cap.release()
    return None, None

cap, index = kamerayi_bul_ve_ac()

if cap:
    print(" Görüntü geliyor, çıkmak için 'q' tuşuna bas.")
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Ekrana sığması için görüntüyü %30 küçültüp gösterelim
        izleme = cv2.resize(frame, (1280, 360))
        cv2.imshow(f"ZED-M Canli Yayin - Indeks {index}", izleme)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print(" Kamera açılamadı! Kabloyu kontrol et veya başka USB portuna tak.")