# TEKNOFEST İnsansız Kara Aracı (İKA) - Otonom Sistem Projesi

Bu depo, TEKNOFEST 2026 İnsansız Kara Aracı (İKA) yarışması kapsamında geliştirilen otonom sürüş, nesne tespiti ve çevre algılama sisteminin yazılım kaynak kodlarını içermektedir. Projede YOLOv8 mimarisi ve ZED-M stereo kamera entegrasyonu kullanılarak parkur üzerindeki trafik işaretleri, aşama tabelaları ve engeller yüksek doğrulukla tespit edilmektedir.

## 🎯 Proje Özellikleri
- **Görüntü İşleme ve Nesne Tespiti:** YOLOv8 nano modeli kullanılarak 13 farklı sınıf (Stage_1'den Stage_11'e kadar olan tabelalar, Dur tabelası vb.) gerçek zamanlı olarak algılanır.
- **Stereo Kamera Entegrasyonu:** ZED-M kamera sensörleri kullanılarak derinlik ve çevre algılama verileri işlenir.
- **Yüksek Doğruluk Oranı:** Model, gerçek saha testlerinde ve gece/gündüz farklı aydınlatma koşullarında stabil başarım göstermektedir.

## 📊 Sistem Testleri ve Başarım Sonuçları

### Gerçek Zamanlı Tabela Algılama Testi
Burada otonom sistemin tabelaları video üzerinde nasıl anlık olarak tespit ettiği ve doğruluk oranları (Confidence Score) görülebilir:

![Otonom Sistem Testi](gorseller/Video%20Project.gif)

### Model Başarım Grafiği (Confusion Matrix)
Modelin eğitim sonrasındaki karmaşıklık matrisi aşağıda yer almaktadır. Sınıflar arasındaki ayrım doğruluğu mükemmele yakındır:

![Confusion Matrix](gorseller/veri.jpeg)

## 📁 Proje Yapısı ve Dosyalar

- `zedm.py`: ZED-M stereo kamera bağlantısını, veri akışını ve görüntü yakalama süreçlerini yöneten betik.
- `egit.py`: YOLOv8 modelinin özel veri seti (custom dataset) ile eğitilmesini sağlayan eğitim konfigürasyonları.
- `dagitici.py`: Toplanan verilerin ve etiketlerin eğitim/doğrulama (train/val) süreçleri için optimize edilmesini sağlayan dağıtıcı kodlar.
- `kameratest.py` & `ss.py`: Kamera testlerini gerçekleştiren ve veri seti toplamak için anlık ekran görüntüsü (screenshot) alan yardımcı araçlar.
- `data.yaml`: Modelin sınıf isimlerini ve veri yollarını barındıran yapılandırma dosyası.

## 🚀 Kurulum ve Çalıştırma

Projenin çalıştırılabilmesi için gerekli kütüphanelerin kurulması gerekmektedir:

```bash
pip install ultralytics opencv-python 
python zedm.py
