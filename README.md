🌐 Tuay Turizm
Tuay Turizm, otel bilgilerini dinamik olarak görüntülemek ve yönetmek için geliştirilmiş bir Django projesidir. Bu proje, otellerin adları, fiyatları, konumları ve açıklamaları gibi bilgileri içerir ve bunları kullanıcılara sunar. Ayrıca otel detaylarını ve birden fazla resmi içeren sayfalar oluşturur.
<br> <br>
📋 İçindekiler <br>
Kurulum <br>
Kullanım <br>
Proje Yapısı <br>
Özellikler <br>
Katkıda Bulunma <br>
Lisans <br>
İletişim <br> <br>
🚀 Kurulum <br>
Projeyi yerel ortamınıza kurmak için aşağıdaki adımları izleyin: <br>
<br><br>
1. Bu depoyu yerel makinenize klonlayın: <br>
   git clone https://github.com/Hamza-Sengul/tuay_turizm.git <br><br>

2. Proje dizinine gidin: <br>
   cd tuay_turizm <br><br>

3. Sanal bir ortam oluşturun: <br>
   python -m venv venv <br><br>

4. Sanal ortamı aktif hale getirin: <br>
   -Windows: <br>
     venv\Scripts\activate <br>
   -macOS/Linux: <br>
     source venv/bin/activate <br><br>

5. Gerekli bağımlılıkları yükleyin: <br>
   pip install -r requirements.txt <br><br>

6. Veritabanı işlemlerini tamamlayın: <br>
   python manage.py migrate <br><br>

7. Geliştirme sunucusunu başlatın: <br>
   python manage.py runserver <br><br>

8. Tarayıcınızda http://127.0.0.1:8000 adresine giderek projeyi görüntüleyin. <br><br>

🛠️ Kullanım <br>
🔑 Admin Paneli <br>
1. Admin paneline erişmek için: <br>
   http://127.0.0.1:8000/admin <br><br>

2. Admin kullanıcı oluşturun: <br>
   python manage.py createsuperuser <br><br>

3. Admin paneline giriş yaparak otel bilgilerini ekleyin ve yönetin. <br><br>

   🏨 Otel Bilgilerini Görüntüleme <br>
Anasayfa, dinamik olarak eklenebilen otellerin adlarını, fiyatlarını, konumlarını ve açıklamalarını içeren bir tabloyu görüntüler. <br><br>

📄 Otel Detayları <br>
Otel detay sayfası, otelin adı, fiyatı, konumu, açıklaması ve birden fazla resmi içerecek şekilde tasarlanmıştır. <br><br>

📂 Proje Yapısı <br><br>

tuay_turizm/ <br>
├── manage.py <br>
├── tuay_turizm/ <br>
│   ├── __init__.py <br>
│   ├── settings.py <br>
│   ├── urls.py <br>
│   └── wsgi.py <br>
├── app/ <br>
│   ├── migrations/ <br>
│   ├── __init__.py <br>
│   ├── admin.py <br>
│   ├── apps.py <br>
│   ├── models.py <br>
│   ├── tests.py <br>
│   ├── views.py <br>
│   ├── templates/ <br>
│   │   ├── index.html <br>
│   │   └── hotel_detail.html <br>
│   └── static/ <br>
│       ├── css/ <br>
│       └── js/ <br>
└── requirements.txt <br>

✨ Özellikler <br>
🏨 Dinamik otel ekleme ve görüntüleme <br>
📄 Otel detay sayfası <br>
🔧 Admin paneli ile yönetim <br>
📸 Birden fazla otel resmi görüntüleme <br>
🗂️ Veritabanı ile entegre yönetim <br>

📜 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

📞 İletişim
Proje ile ilgili sorularınız veya önerileriniz için lütfen Hamza Şengül ile iletişime geçin.
