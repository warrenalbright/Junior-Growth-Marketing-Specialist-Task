import os
from youtube_transcript_api import YouTubeTranscriptApi

def download_transcript(video_id, author_name, file_name):
    try:
        # Membuat folder jika belum ada
        output_dir = f"research/youtube-transcripts/{author_name}"
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"Sedang menarik transkrip untuk {file_name}...")
        
        # Mengambil transkrip dari YouTube
        srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'id'])
        
        # Menyimpan ke file teks
        file_path = os.path.join(output_dir, f"{file_name}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            for i in srt:
                f.write(f"{i['text']}\n")
                
        print(f"✅ Sukses! Tersimpan di: {file_path}")
    except Exception as e:
        print(f"❌ Gagal mengambil video {video_id}: {str(e)}")

# --- AREA EKSEKUSI DATA ---
# Besok kita tinggal masukkan ID Video YouTube para pakar di sini
# Contoh: URL https://www.youtube.com/watch?v=dQw4w9WgXcQ -> ID-nya adalah 'dQw4w9WgXcQ'
if __name__ == "__main__":
    # Test jalankan satu video contoh dari Jake Ward jika kamu punya ID-nya
    # download_transcript('ID_VIDEO_DI_SINI', 'jake-ward', 'ai-seo-playbook')
    pass