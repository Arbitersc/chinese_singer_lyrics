import re
import json
import requests

write_path = "./tmp.jsonl"

def get_hunyuan_res(messages):
    for _ in range(3):
        try:
            response = requests.post("http://hunyuanapi.woa.com/openapi/v1/chat/completions", json={
                "model": "hunyuan-2.0-instruct-20251111",
                # "model": "hunyuan",
                "messages": messages,
                "stream": False,
                "enable_enhancement": True,
                "force_search_enhancement": True,
            }, headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer xxxxxxxxxxxx",
            })
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(e)
        continue
    return None

def get_musician_album_list(musician):
    messages = [{
        "role": "user", "content": f"""请列出所有 {musician} 发行的专辑，按照以下markdown格式返回：
```markdown
- [专辑名]-[发行时间]
……
```"""
    }]
    for _ in range(3):
        try:
            album_list = get_hunyuan_res(messages)
            if album_list is None:
                continue
            album_list = re.findall(r"- \[(.*?)\]-\[(.*?)\]", album_list.strip())
            if len(album_list) == 0:
                continue
            return album_list
        except:
            continue
    return None

def get_album_song_list(musician, album, album_date):
    messages = [{
        "role": "user", "content": f"""请列出所有 {musician} 于 {album_date} 发行的专辑《{album}》的歌曲，按照以下markdown格式返回：
```markdown
- [[歌曲名]]
……
```"""
    }]
    for _ in range(3):
        try:
            song_list = get_hunyuan_res(messages)
            if song_list is None:
                continue
            song_list = re.findall(r"- \[\[(.*?)\]\]", song_list.strip())
            if len(song_list) == 0:
                continue
            return song_list
        except:
            continue
    return None

def get_lyric(musician, album, album_date, song):
    messages = [{
        "role": "user", "content": f"""请给出 {musician} 于 {album_date} 发行的专辑《{album}》中歌曲《{song}》的完整歌词，只保留歌词本身（移除创作者信息、歌曲信息、主副歌说明等信息），按照以下markdown格式返回必须包含"```markdown"：
```markdown
……
```"""
    }]
    for _ in range(3):
        try:
            lyric = get_hunyuan_res(messages)
            if lyric is None:
                continue
            lyric = re.findall(r"```markdown\n(.*?)\n```", lyric.strip(), re.DOTALL)[0]
            if len(lyric.split()) < 5:
                continue
            return lyric
        except:
            continue
    return None

def download_musician_lyric(musician):
    album_list = get_musician_album_list(musician)
    cnt = 0
    print(album_list)
    if album_list is None:
        return None
    for album, album_date in album_list:
        song_list = get_album_song_list(musician, album, album_date)
        if song_list is None:
            continue
        print(song_list)
        for song in song_list:
            lyric = get_lyric(musician, album, album_date, song)
            with open(write_path, "a") as f:
                f.write(json.dumps({
                    "musician": musician,
                    "album": album,
                    "album_date": album_date,
                    "song": song,
                    "lyric": lyric
                }, ensure_ascii=False) + "\n")
                f.flush()
                cnt += 1
                print(f"Downloaded {musician} {cnt} songs' lyric - {album} - {song}")

def main():
    musicians = [
        "周杰伦",
        "林俊杰",
        "陶喆",
        "方大同",
        "王力宏",
        "陈奕迅",
    ]
    for musician in musicians:
        download_musician_lyric(musician)


if __name__ == "__main__":
    main()
