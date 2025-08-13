# 🎬 AUTO CLIP - Generator Video dengan Subtitle Otomatis

Aplikasi Python untuk mengunduh video dari YouTube secara otomatis dan menambahkan subtitle menggunakan transkripsi AI dari Whisper.

## 📋 Fitur Utama

- ✅ **Download otomatis** dari YouTube
- ✅ **Transkripsi AI** menggunakan Whisper (akurasi tinggi)
- ✅ **Subtitle otomatis** dengan styling profesional
- ✅ **Progress bar** untuk monitoring proses
- ✅ **Output HD** dengan kualitas terjaga

## 🚀 Cara Menjalankan

### Persyaratan Sistem
- Python 3.8 atau lebih baru
- FFmpeg (untuk processing audio/video)

### Instalasi

1. **Clone repository ini**
   ```bash
   git clone [URL_REPOSITORY]
   cd AUTO-CLIP
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Windows:**
   Download dari [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) dan tambahkan ke PATH.

### Cara Menggunakan

1. **Edit file `dea.py`**
   - Ganti `VIDEO_URL` dengan link YouTube yang ingin diproses
   - Sesuaikan `MODEL_WHISPER` jika diperlukan

2. **Jalankan aplikasi**
   ```bash
   python dea.py
   ```

3. **Hasil**
   - Video akan tersimpan di folder `downloads/`
   - File output: `[judul_video]_subtitled.mp4`

## 📁 Struktur Folder

```
AUTO-CLIP/
├── dea.py                            
├── requirements.txt                  
├── downloads/                        
│   ├── [judul_video].mp4
│   └── [judul_video]_subtitled.mp4
└── output_shorts/                
```

## ⚙️ Konfigurasi

### Model Whisper
- `tiny` - Cepat tapi kurang akurat
- `base` - Balance antara kecepatan dan akurasi
- `small` - Akurasi baik
- `medium` - Akurasi sangat baik
- `large` - Akurasi tertinggi (default)

### Customisasi Subtitle
Edit bagian ini di `dea.py` untuk mengubah tampilan subtitle:
```python
subtitle = (TextClip(text, 
                   fontsize=48,          # Ukuran font
                   font="Arial-Bold",    # Jenis font
                   color="white",        # Warna teks
                   stroke_color="black", # Warna outline
                   stroke_width=2)       # Ketebalan outline
```

## 🛠️ Troubleshooting

### Error: "ffmpeg not found"
Pastikan FFmpeg sudah terinstall dan tersedia di PATH sistem.

### Error: "CUDA out of memory"
Gunakan model Whisper yang lebih kecil atau tambahkan parameter:
```python
result = model.transcribe(temp_audio, verbose=False, fp16=False)
```
## 🌐 Komunitas & Sosial Media

Ingin berdiskusi, bertanya, atau berbagi ide? Bergabunglah dengan komunitas kami!

💬 Telegram Group: [t.me/airdropindependen](https://t.me/independendropers)

🐦 Twitter/X: [twitter.com/deasaputra12](https://x.com/Deasaputra_12)

🎮 Discord Server: [discord.gg/airdropindependen](https://discord.gg/Tuy2bR6CkU)


## Buy Me a Coffee

- **EVM:** 0x905d0505Ec007C9aDb5CF005535bfcC5E43c0B66
- **TON:** UQCFO7vVP0N8_K4JUCfqlK6tsofOF4KEhpahEEdXBMQ-MVQL
- **SOL:** BmqfjRHAKXUSKATuhbjPZfcNciN3J2DA1tqMgw9aGMdj

Thank you for visiting this repository, don't forget to contribute in the form of follows and stars.
If you have questions, find an issue, or have suggestions for improvement, feel free to contact me or open an *issue* in this GitHub repository.

**deasaputra**
