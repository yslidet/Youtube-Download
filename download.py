import yt_dlp
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Download Youtube Video"
    )
    parser.add_argument(
        "video_url", type=str, help="YouTube URL to download"
    )
    parser.add_argument(
        "resolution", type=int, help="Set Maximum resolution (e.g.720, 1080, 1440, 2160 ~ 4K)"
    )
    return parser.parse_args()

# Replace this with your desired YouTube video URL
# video_url = "https://www.youtube.com/watch?v=bF_WRPrpISw&list=PLjgiUg70jHBDAgdVjBFLzxxbMOhACU9Zt"
# resolution = "720" 

def download_video(video_url, resolution):
    try: 
        ydl_opts = {
                'format': f'bestvideo[height<={resolution}]+bestaudio[acodec^=aac]/best[height<={resolution}]',
                'merge_output_format': 'mp4',
                'outtmpl': 'output/%(title)s.%(ext)s',  # Save with video title
                'quiet': False,
                'noplaylist': True,  # Avoids downloading entire playlists accidentally
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            output_filename = ydl.prepare_filename(info_dict)
            ydl.download([video_url]) 
            

        print(f"Download complete! \n> Saved at {output_filename}")

    except Exception as e:
        print(f"An error: {e}")

def main():
    args = parse_args()
    download_video(args.video_url, args.resolution)

if __name__ == "__main__":
    main()
