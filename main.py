import flet as ft
import yt_dlp
import os

def main(page: ft.Page):
    page.title = "YT MP4 Downloader"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    judul = ft.Text("MP4 DOWNLOADER 🚀", size=28, weight="bold", color="red")
    url_input = ft.TextField(label="Tempel Link YouTube Disini", width=400, border_color="red")
    status = ft.Text("Siap Gas!", color="grey")
    progress = ft.ProgressBar(width=400, visible=False)

    def mulai_download(e):
        if not url_input.value:
            status.value = "Isi linknya dulu, Bos!"
            page.update()
            return

        status.value = "Sedang Mengunduh Video... Mohon Tunggu."
        status.color = "blue"
        progress.visible = True
        page.update()

        try:
            # Path download untuk Android (Folder Download HP)
            # Jika di Windows, otomatis simpan di folder aplikasi
            path = '/storage/emulated/0/Download/%(title)s.%(ext)s' if os.name != 'nt' else '%(title)s.%(ext)s'

            ydl_opts = {
                # Mengambil MP4 kualitas terbaik yang sudah ada suaranya (biasanya 720p ke bawah langsung)
                # Atau menggabungkan video+audio MP4 terbaik
                'format': 'best[ext=mp4]/best',
                'outtmpl': path,
                'noplaylist': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url_input.value])
            
            status.value = "✅ BERHASIL! Cek Folder Download."
            status.color = "green"
        except Exception as err:
            status.value = f"❌ Gagal: Coba cek koneksi/link."
            status.color = "red"
        
        progress.visible = False
        page.update()

    btn = ft.ElevatedButton("DOWNLOAD SEKARANG", on_click=mulai_download, bgcolor="red", color="white")

    page.add(judul, ft.Divider(height=20), url_input, btn, progress, status)

ft.app(target=main)