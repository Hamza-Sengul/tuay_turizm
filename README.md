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

******************************

🌐 Tuay Tourism
Tuay Tourism is a Django project developed to dynamically display and manage hotel information. This project includes details such as hotel names, prices, locations, and descriptions, and presents them to users. It also creates pages with hotel details and multiple images.
<br> <br>
📋 Table of Contents <br>
Installation <br>
Usage <br>
Project Structure <br>
Features <br>
Contributing <br>
License <br>
Contact <br> <br>
🚀 Installation <br>
Follow these steps to set up the project in your local environment: <br>
<br><br>

Clone this repository to your local machine: <br>
git clone https://github.com/Hamza-Sengul/tuay_turizm.git <br><br>

Navigate to the project directory: <br>
cd tuay_turizm <br><br>

Create a virtual environment: <br>
python -m venv venv <br><br>

Activate the virtual environment: <br>

Windows: <br>
venv\Scripts\activate <br>
macOS/Linux: <br>
source venv/bin/activate <br><br>
Install the required dependencies: <br>
pip install -r requirements.txt <br><br>

Complete the database migrations: <br>
python manage.py migrate <br><br>

Start the development server: <br>
python manage.py runserver <br><br>

Open your browser and go to http://127.0.0.1:8000 to view the project. <br><br>

🛠️ Usage <br>
🔑 Admin Panel <br>

Access the admin panel at: <br>
http://127.0.0.1:8000/admin <br><br>

Create an admin user: <br>
python manage.py createsuperuser <br><br>

Log in to the admin panel to add and manage hotel information. <br><br>

🏨 Viewing Hotel Information <br>
The homepage displays a table containing dynamically added hotels' names, prices, locations, and descriptions. <br><br>

📄 Hotel Details <br>
The hotel detail page is designed to include the hotel's name, price, location, description, and multiple images. <br><br>

📂 Project Structure <br><br>

tuay_turizm/ <br>
├── manage.py <br>
├── tuay_turizm/ <br>
│ ├── init.py <br>
│ ├── settings.py <br>
│ ├── urls.py <br>
│ └── wsgi.py <br>
├── app/ <br>
│ ├── migrations/ <br>
│ ├── init.py <br>
│ ├── admin.py <br>
│ ├── apps.py <br>
│ ├── models.py <br>
│ ├── tests.py <br>
│ ├── views.py <br>
│ ├── templates/ <br>
│ │ ├── index.html <br>
│ │ └── hotel_detail.html <br>
│ └── static/ <br>
│ ├── css/ <br>
│ └── js/ <br>
└── requirements.txt <br>

✨ Features <br>
🏨 Dynamic hotel addition and viewing <br>
📄 Hotel detail page <br>
🔧 Management via the admin panel <br>
📸 Viewing multiple hotel images <br>
🗂️ Integrated management with the database <br>

📜 License
This project is licensed under the MIT License. For more information, see the LICENSE file.

📞 Contact
For any questions or suggestions about the project, please contact Hamza Şengül.
