from yt_dlp import YoutubeDL
import json
from datetime import datetime

def get_playlist_info(playlist_url):
    ydl_opts = {
        'extract_flat': True,  # 再生リストの情報だけを取得
        'skip_download': True  # 動画のダウンロードをスキップ
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        
        playlist_info = {
            "timestamp": datetime.now().isoformat(),
            "playlist_title": info_dict.get('title', 'Unknown Title'),
            "playlist_url": playlist_url,
            "videos": []
        }
        
        entries = info_dict.get('entries', [])
        for entry in entries:
            video_info = {
                "url": f"https://www.youtube.com/watch?v={entry.get('id')}",
                "title": entry.get('title')
            }
            playlist_info["videos"].append(video_info)
        
        return playlist_info

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    playlist_info = get_playlist_info(playlist_url)
    
    # JSON形式で保存または表示
    json_output = json.dumps(playlist_info, indent=4, ensure_ascii=False)
    print(json_output)
    
    # ファイルに保存する場合
    json_title = "[PLAYLIST]"+str(playlist_info["playlist_title"])+".json"
    with open(json_title, "w", encoding="utf-8") as f:
        f.write(json_output)
