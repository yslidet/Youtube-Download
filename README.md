# One-Stop to Download Youtube Video 

## Highlights 
* To download youtube video with provided URL and resolution
* One-stop and one-line execution

```bash
# python download.py "url" resolution
# ^ resolution (e.g.720, 1080, 1440, 2160 ~ 4K)
python download.py "https://youtube.com/shorts/EDUqT2cZ1nY?si=Kx7XO-OL07-DOtEJ" 720
```


<img src=setup/demo_download_youtube.gif>



## Installation 
via [docker (preferred)]()
```bash
cd setup/
docker build \
   -t youtube_download:v1 \
   -f setup_dockerfile \
   .
```

via [pip]()
```bash
pip install yt_dlp
pip install ffmpeg
```

## Usage
^ start and run docker container 
```bash
# python download.py "url" resolution
# ^ resolution (e.g.720, 1080, 1440, 2160 ~ 4K)
python download.py "https://youtube.com/shorts/EDUqT2cZ1nY?si=Kx7XO-OL07-DOtEJ" 720
```



