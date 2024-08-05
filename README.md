# Ytplaylist2urls
これはYoutubeの再生リストの動画のurlを抽出するプログラムです．

# 実行方法
1. Pythonが実行できるようにする
2. ```pip install yt-dlp```を実行し，yt-dlpをインストールする
3. main.pyを実行する
4. 「Enter the YouTube playlist URL:」の後に再生リストのurlを入力する
5. urlが入ったJSONが出力される


>Youtubeの再生リストは以下のフォーマットで与えれれます．
>```
>https://www.youtube.com/playlist?list=<playlist ID>
>```
>
>[参考：再生リストを共有する(Googleヘルプ)](https://support.google.com/youtube/answer/57793?hl=ja&co=GENIE.Platform%3DDesktop)
>
>もし```<playlist ID>```が分からないときには，再生リストの動画を一つクリックしてください．urlに含まれる```list=```の値が```<playlist ID>```になります．

# 実行結果
実行すると以下のようなJSONを取得することができます．
```json
{
    "timestamp": "2024-08-05T10:11:36.991441",
    "playlist_title": "01-The Beatles - Please Please me (full album)",
    "playlist_url": "https://www.youtube.com/playlist?list=PLycVTiaj8OI9COuVDJdw_RdBWy11ALc4T",
    "videos": [
        {
            "url": "https://www.youtube.com/watch?v=oxwAB3SECtc",
            "title": "I Saw Her Standing There (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=qhbcN3ew9z0",
            "title": "Misery (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=b3zNKWyLfus",
            "title": "Anna (Go To Him) (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=rJOhavaeJYk",
            "title": "Chains (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=Qr8OuW5JJgQ",
            "title": "Boys (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=2ttGjtfQ7EA",
            "title": "Ask Me Why (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=czw8eqepir8",
            "title": "Please Please Me (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=0pGOFX1D_jg",
            "title": "Love Me Do (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=MA5DkiVKSlM",
            "title": "P.S. I Love You (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=AWUTlM6hz0g",
            "title": "Baby It's You (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=uRQ7ecvU56k",
            "title": "Do You Want To Know A Secret (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=MkQ1eOcl5ug",
            "title": "A Taste Of Honey (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=vTsbYbN8VVI",
            "title": "There's A Place (Remastered 2009)"
        },
        {
            "url": "https://www.youtube.com/watch?v=2RicaUqd9Hg",
            "title": "Twist And Shout (Remastered 2009)"
        }
    ]
}

```

# 仕組み
yt-dlpでオプション設定を変更して動画のメタデータのみの取得を行っています．

# 参考
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [再生リストを共有する(Googleヘルプ)](https://support.google.com/youtube/answer/57793?hl=ja&co=GENIE.Platform%3DDesktop)


