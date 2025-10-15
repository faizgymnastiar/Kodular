# Kodular IoT Monitoring (Wokwi + MQTT)

Proyek ini adalah aplikasi *Monitoring IoT berbasis Kodular* yang terhubung dengan *Wokwi* menggunakan *MQTT (broker.hivemq.com)* dan meniru tampilan dashboard web versi sebelumnya.

---

## 🔧 Konfigurasi MQTT
Gunakan broker berikut:
MQTT_BROKER_URL = mqtt://broker.hivemq.com:1883
MQTT_USERNAME =
MQTT_PASSWORD =
MQTT_BASE_TOPIC = /sistem_iot
Tambahkan *MQTT extension* (Paho/Arduino MQTT) ke project Kodular.

---

## 📱 Struktur Screen
Proyek ini terdiri dari:

| Screen | Fungsi |
|--------|---------|
| ⁠ LoginScreen ⁠ | Autentikasi admin (admin/admin) |
| ⁠ AdminDashboard ⁠ | Tampilan utama sensor, relay, dan status MQTT |
| ⁠ HistoryScreen ⁠ | Menampilkan riwayat sensor & ekspor CSV |
| ⁠ Sidebar ⁠ | Navigasi antar screen |

---

## 📋 Komponen & Blok
Semua panduan ada di folder berikut:
•⁠  ⁠[⁠ components/ ⁠](components/) – daftar komponen tiap screen.
•⁠  ⁠[⁠ blocks/ ⁠](blocks/) – panduan blok Kodular satu per satu.

---

## 🚀 Cara Menggunakan
1.⁠ ⁠Buka [Kodular.io Creator](https://creator.kodular.io/).
2.⁠ ⁠Buat project baru.
3.⁠ ⁠Ikuti isi file di folder ⁠ components/ ⁠ dan ⁠ blocks/ ⁠.
4.⁠ ⁠Jalankan MQTT dan lihat data sensor Wokwi muncul di dashboard.

---

📦 *Author*: Faiz Gymnastiar & GPT-5 Assistant  
📅 *Terakhir diperbarui:* Oktober 2025
