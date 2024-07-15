🌐 Tuay Turizm
Tuay Turizm, otel bilgilerini dinamik olarak görüntülemek ve yönetmek için geliştirilmiş bir Django projesidir. Bu proje, otellerin adları, fiyatları, konumları ve açıklamaları gibi bilgileri içerir ve bunları kullanıcılara sunar. Ayrıca otel detaylarını ve birden fazla resmi içeren sayfalar oluşturur.

📋 İçindekiler
Kurulum
Kullanım
Proje Yapısı
Özellikler
Katkıda Bulunma
Lisans
İletişim
🚀 Kurulum
Projeyi yerel ortamınıza kurmak için aşağıdaki adımları izleyin:

1. Bu depoyu yerel makinenize klonlayın:
   git clone https://github.com/Hamza-Sengul/tuay_turizm.git

2. Proje dizinine gidin:
   cd tuay_turizm

3. Sanal bir ortam oluşturun:
   python -m venv venv

4. Sanal ortamı aktif hale getirin:
   -Windows:
     venv\Scripts\activate
   -macOS/Linux:
     source venv/bin/activate

5. Gerekli bağımlılıkları yükleyin:
   pip install -r requirements.txt

6. Veritabanı işlemlerini tamamlayın:
   python manage.py migrate

7. Geliştirme sunucusunu başlatın:
   python manage.py runserver

8. Tarayıcınızda http://127.0.0.1:8000 adresine giderek projeyi görüntüleyin.

🛠️ Kullanım
🔑 Admin Paneli
1. Admin paneline erişmek için:
   http://127.0.0.1:8000/admin

2. Admin kullanıcı oluşturun:
   python manage.py createsuperuser

3. Admin paneline giriş yaparak otel bilgilerini ekleyin ve yönetin.

   🏨 Otel Bilgilerini Görüntüleme
Anasayfa, dinamik olarak eklenebilen otellerin adlarını, fiyatlarını, konumlarını ve açıklamalarını içeren bir tabloyu görüntüler.

📄 Otel Detayları
Otel detay sayfası, otelin adı, fiyatı, konumu, açıklaması ve birden fazla resmi içerecek şekilde tasarlanmıştır.

📂 Proje Yapısı

tuay_turizm/
├── manage.py
├── tuay_turizm/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   ├── index.html
│   │   └── hotel_detail.html
│   └── static/
│       ├── css/
│       └── js/
└── requirements.txt

✨ Özellikler
🏨 Dinamik otel ekleme ve görüntüleme
📄 Otel detay sayfası
🔧 Admin paneli ile yönetim
📸 Birden fazla otel resmi görüntüleme
🗂️ Veritabanı ile entegre yönetim

📜 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

📞 İletişim
Proje ile ilgili sorularınız veya önerileriniz için lütfen Hamza Şengül ile iletişime geçin.
