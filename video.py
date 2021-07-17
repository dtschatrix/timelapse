import requests
from bs4 import BeautifulSoup
import os
from youtube_dl import YoutubeDL

def main():
    print("starting polling")
    run_videos()


def scarp_videos(videos) -> list:
    headers = {'User-agent': 'Mozilla/5.0'}
    main_site = "https://webcam.scs.com.ua"
    video_src = []
    for video_href in videos:
        r = requests.get(main_site + video_href["href"], headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        video_tags = soup.find_all("iframe", id="youtube")
        if video_tags:
            print("Total ", len(video_tags), "videos_found")
            for video_tag in video_tags[:10]:
                video_src.append(video_tag['src'])
            print(video_tag)
    return video_src


def first_ten_videos():
    web_url = "https://webcam.scs.com.ua/"
    headers = {'User-agent': 'Mozilla/5.0'}

    r = requests.get(web_url, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')

    list_hrefs = soup.find_all("a", class_="wr-image")

    if list_hrefs:
        return scarp_videos(list_hrefs)

def run_videos():
    os.chdir("video")
    f = open("links.txt", "w")
    ydl = YoutubeDL({'format': 'best', 'outtmpl': '%(id)s.%(ext)'})
    url = first_ten_videos()
    result =[]
    with ydl:
        for item in url:
            try:
                ydl.cache.remove()
                item_info = ydl.extract_info(item, download=False)
                if 'entries' in item_info:
                    video = item_info["entries"]
                else:
                    video = item_info
                result.append(video)
            except:
                pass
    
    for item in result:
        f.write(item["url"] + '\n')
    f.close()
    
    # os.chdir("video/video_samples/test")
    # subprocess.call(['ffmpeg', '-y', '-i', video['url'], '-c:v','copy', '-c:a', 'copy', 'whiteboysummer.mp4'])



if __name__ == "__main__":
    main()
