# Kryptonex
Python Şifre Çözüm Terminali

# 🔐 KRYPTONEX v1.0 | Şifre Çözüm Terminali

![Python](https://shields.io)
![Architecture](https://shields.io)
![Platform](https://shields.io)

**KRYPTONEX**, siber güvenlik analizleri, **CTF (Capture The Flag)** yarışmaları ve kriptografik veri incelemeleri için Python 3 ve **Nesne Tabanlı Programlama (OOP)** mimarisiyle geliştirilmiş modern bir masaüstü şifre çözüm aracıdır.

---

## 🚀 Öne Çıkan Özellikler

* **🧠 Akıllı Algoritma Tespiti:** Girilen şifreli veya kodlanmış metnin yapısını analiz ederek uygun çözücü sınıfını otomatik seçer.
* **🔓 7 Farklı Çözücü Modülü:**
  * **Base64** (UTF-8 karakter destekli)
  * **Onaltılık (Hexadecimal)** (Boşluk toleranslı)
  * **İkili Sistem (Binary - 8 Bit)**
  * **URL Kodlama (Percent-Encoding)**
  * **Mors Alfabesi** (Harf ve rakam tam destekli)
  * **ROT13**
  * **Sezar Şifrelemesi** (Brute-Force — Tüm 25 anahtar ihtimalini alt alta listeler)
* **🏗️ Bağımsız Katman Mimarisi:** Arayüz katmanı (`main.py`) ve iş mantığı motoru (`backend.py`) tamamen ayrı sınıflar halinde tasarlanmıştır.
* **💻 Modern Terminal Arayüzü:** CustomTkinter tabanlı karanlık hacker teması, tek tıkla yapıştırma/kopyalama ve salt-okunur çıktı koruması.

---

## 🛠️ Kurulum ve Çalıştırma

### 🐉 Kali Linux / Debian
```bash
git clone https://github.com
cd Kryptonex
sudo apt update && sudo apt install python3-tk -y
pip3 install customtkinter --break-system-packages
python3 main.py
```

### 🪟 Windows
```bash
git clone https://github.com
cd Kryptonex
pip install customtkinter
python main.py
```

---

## 📂 Proje Yapısı

```text
Kryptonex/
├── main.py        # CustomTkinter tabanlı kullanıcı arayüzü (Frontend)
├── backend.py     # OOP tabanlı şifre çözüm sınıfları ve otomatik algılama motoru
└── README.md      # Proje dokümantasyonu
```

---

## 👨‍💻 Geliştirici

* **Ahmet Serhan Şima** — [@serhansima283-hub](https://github.com)
