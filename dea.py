import os
import yt_dlp
import whisper
import tempfile
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from tqdm import tqdm

# ==== KONFIGURASI ====
VIDEO_URL = "https://youtu.be/QJItR7K"  # Ganti dengan link video kamu
OUTPUT_DIR = "downloads"
MODEL_WHISPER = "large"  # large = akurasi tinggi
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==== DOWNLOAD VIDEO ====
print("📥 Mengunduh video...")
ydl_opts = {
    "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
    "merge_output_format": "mp4",
    "noplaylist": True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(VIDEO_URL, download=True)
    video_path = ydl.prepare_filename(info_dict).replace(".webm", ".mp4").replace(".m4a", ".mp4")
    title = info_dict.get("title", "video")
print(f"✅ Video diunduh: {video_path}")

# ==== TRANSKRIPSI DENGAN PROGRESS BAR ====
print("🗣️ Transkripsi audio dengan Whisper...")
model = whisper.load_model(MODEL_WHISPER)

# Ekstrak audio sementara
temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
os.system(f'ffmpeg -i "{video_path}" -vn -acodec pcm_s16le -ar 16000 -ac 1 "{temp_audio}" -y')

# Proses transkripsi
result = model.transcribe(temp_audio, verbose=False)
text_segments = result["segments"]
print("✅ Transkripsi selesai.")

# ==== BUAT SUBTITLE DI VIDEO ====
print("🎬 Menambahkan subtitle...")
video_clip = VideoFileClip(video_path)

subtitle_clips = []
for seg in tqdm(text_segments, desc="Menambahkan subtitle"):
    start = seg["start"]
    end = seg["end"]
    text = seg["text"].strip()

    subtitle = (TextClip(text, fontsize=48, font="Arial-Bold", color="white", stroke_color="black", stroke_width=2, method="caption", size=(video_clip.w * 0.9, None))
                .set_start(start)
                .set_end(end)
                .set_position(("center", "bottom")))

    subtitle_clips.append(subtitle)

final = CompositeVideoClip([video_clip, *subtitle_clips])
output_final = os.path.join(OUTPUT_DIR, f"{title}_subtitled.mp4")
final.write_videofile(output_final, codec="libx264", audio_codec="aac", fps=30)
print(f"✅ Video final dengan subtitle disimpan di: {output_final}")
