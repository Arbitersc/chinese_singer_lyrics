# 华语热门歌手专辑歌词合集 chinese_singer_lyrics

基于【大语言模型的联网搜索功能】去获取对应歌手的所有歌词。
所以理论上，仓库中的简陋代码 `download_music.py` 稍微修改 `get_hunyuan_res` 函数功能就可以接入任何模型进行爬取。

## 目前已获取歌手歌词

- [周杰伦歌曲歌词](./lyrics/zhoujielun.jsonl)
- [林俊杰歌曲歌词](./lyrics/linjunjie.jsonl)
- [陶喆歌曲歌词](./lyrics/taozhe.jsonl)
- [方大同歌曲歌词](./lyrics/fangtong.jsonl)
- [王力宏歌曲歌词](./lyrics/wanglihong.jsonl)
- [陈奕迅歌曲歌词](./lyrics/chenyixun.jsonl)

有什么想获取的歌手也可以提交issue，看到有时间就弄一下。

## 歌词信息存储格式

```json
{
  "musician": "方大同",
  "album": "危险世界",
  "album_date": "2014年4月11日",
  "song": "天气先生",
  "lyric": "Maybe we won't see the sunrise\nMaybe we won't see the moon shine\nEven if the whole world is just you and I\nIt's ok girl everything will be fine\nIt's ok girl\nMaybe the sun won't shine\nIt's ok girl\nMaybe the rain won't fall\nIt's ok girl\nBut maybe our love will find a way\nAnd rise above it all\nMaybe there comes a day\nWhen all of the skies turn grey\nMaybe today our love can fly high\nYou and I will soar\nEverybody's talking bout how to stop\nEverybody's talking bout where to start\nEverybody's talking straight from the heart\nEverybody's talking everybody's talking about it\n爱你并不是巧合\n万年只有你一个\n遇上你的那一刻\n改变了所有规则\n让我描述你的美\n譲我擦掉你滴泪\n有我安慰你入睡\n你是我最珍贵\n这个世界 谁知未来\n你我之间 非常的时代\n我们的爱 是否会在\nI just wanna tell you girl oh\nMaybe the sun won't shine\nMaybe the rain won't fall\nBut maybe our love will find a way\nAnd rise above it all\nMaybe there comes a day\nWhen all of the skies turn grey\nMaybe today our love can fly high\nYou and I will soar\nEverybody's talking bout how to stop\nEverybody's talking bout where to start\nEverybody's talking straight from the heart\nEverybody's talking everybody's talking about it\n慢慢靠近我耳朵\n在我耳边轻轻说\n永远爱的人是我\n说我担心的太多\n让我感受你温柔\n让我爱你的理由\n昨日今天和今后\nI'll be in love with you\n这个世界 谁知未来\n你我之间 非常的时代\n我们的爱 是否会在\nI just wanna tell you girl oh\nMaybe the sun won't shine\nMaybe the rain won't fall\nBut maybe our love will find a way\nAnd rise above it all\nMaybe there comes a day\nWhen all of the skies turn grey\nMaybe today our love can fly high\nYou and I will soar\n一百多年 不如一面 在你身边\n再多留几天 珍惜这时间\n最终的起点\n我会一直想起\n一直一直想起\n岁月留下的回忆\nMaybe the sun won't shine\nMaybe the rain won't fall\nBut maybe our love will find a way\nAnd rise above it all\nMaybe there comes a day\nWhen all of the skies turn grey\nMaybe today our love can fly high\nYou and I will soar\nEverybody's talking bout how to stop\nEverybody's talking bout where to start\nEverybody's talking straight from the heart\nEverybody's talking everybody's talking about it"
}
```
