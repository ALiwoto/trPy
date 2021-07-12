# anilistWrapPY
> A smol anilist wrapper for my personal use :p

## Media
![image](https://user-images.githubusercontent.com/63096193/125343065-4303d180-e373-11eb-8166-7a1345a82ab3.png)
```
>>> from anilistWrapPY.Media.request import GetMedia
>>> GetMedia("Talentless Nana")
AniListMedia(data={'Page': {'media': [{'id': 117343, 'title': {'romaji': 'Munou na Nana', 'english': 'Talentless Nana', 'native': '無能なナナ'}, 'type': 'ANIME', 'format': 'TV', 'status': 'FINISHED', 'description': "It is the year 20XX. Earth has been assaulted by monsters known as 'the Enemy of Humanity'. In order to deal with this threat, special schools comprised of teenagers with extraordinary abilities were formed. These people, who came to be known as 'the Talented', have abilities that defy the rules of reality. Among these superpowered individuals was an outlier, someone who was sent to one 
of these schools despite having no innate special abilities whatsoever. This is the story of our protagonist, who attempts to defeat the Enemies of Humanity through the use of intelligence and manipulation.\n", 'episodes': 13, 'bannerImage': 'https://s4.anilist.co/file/anilistcdn/media/anime/banner/117343-w0m2gfOlQphZ.jpg', 'externalLinks': [{'url': 'https://munounanana.com/'}, {'url': 'https://twitter.com/munounanana'}, {'url': 'https://www.animelab.com/shows/talentless-nana'}, {'url': 'https://www.funimation.com/shows/talentless-nana/'}, {'url': 'https://www.youtube.com/playlist?list=PLwLSw1_eDZl2t0ExBn76ZdBomplZbeaay'}], 'duration': 24, 'chapters': None, 'volumes': None, 'genres': ['Drama', 'Horror', 'Psychological', 'Supernatural', 'Thriller'], 'synonyms': [], 'averageScore': 71, 'airingSchedule': {'nodes': []}, 'siteUrl': 'https://anilist.co/anime/117343'}, {'id': 99536, 'title': {'romaji': 'Munou na Nana', 'english': 'Talentless Nana', 'native': '無能なナナ'}, 'type': 'MANGA', 'format': 'MANGA', 'status': 'RELEASING', 'description': 'An academy on an island in unnavigable waters. There, students trained tirelessly, to fight back against the enemies of humanity. The protagonist, a student newly transferred there, also sets out with the intention of eradicating all enemies of humankind. An unpredictable, intellectual suspense story of justice and evil.<br><br>(Source: Crunchyroll)', 'episodes': None, 'bannerImage': 'https://s4.anilist.co/file/anilistcdn/media/manga/banner/99536-razqvMNL5k6E.jpg', 'externalLinks': [{'url': 'https://www.crunchyroll.com/comics/manga/talentless-nana/volumes'}], 'duration': None, 'chapters': None, 'volumes': None, 'genres': ['Drama', 'Horror', 'Psychological', 'Supernatural', 'Thriller'], 'synonyms': ['Munouna Nana'], 'averageScore': 71, 'airingSchedule': {'nodes': []}, 'siteUrl': 'https://anilist.co/manga/99536'}, {'id': 123803, 'title': {'romaji': 'Munou na Nana: Mini Anime', 'english': None, 'native': '無能なナナ ミニアニメ'}, 'type': 'ANIME', 'format': 'ONA', 'status': 'FINISHED', 'description': 'Mini anime for <i>Munou na Nana</i> released weekly on the official Twitter and website.', 'episodes': 12, 'bannerImage': None, 'externalLinks': [{'url': 'https://twitter.com/munounanana'}, {'url': 'https://munounanana.com/special/mini-anime.html'}], 'duration': 3, 'chapters': None, 'volumes': None, 'genres': [], 'synonyms': ['Talentless Nana: Mini Anime'], 'averageScore': 55, 'airingSchedule': {'nodes': []}, 'siteUrl': 'https://anilist.co/anime/123803'}, {'id': 131753, 'title': {'romaji': 'Zhiqu Yang Xuetang: Dong Zhi Wu Pian', 'english': 'Pleasant Goat Fun Class: Animals & Plants', 'native': '智趣羊学堂之动植物篇'}, 'type': 'ANIME', 'format': 'ONA', 'status': 'FINISHED', 'description': None, 'episodes': 26, 'bannerImage': None, 'externalLinks': [{'url': 'http://www.22dm.com/drama/dr_25.html'}, {'url': 'https://v.qq.com/detail/z/zsfymr17g4saqgq.html'}], 'duration': 6, 'chapters': None, 'volumes': None, 'genres': ['Adventure', 'Comedy'], 'synonyms': ['喜羊羊与灰太狼之智趣羊学堂（上部）'], 'averageScore': None, 'airingSchedule': {'nodes': []}, 'siteUrl': 'https://anilist.co/anime/131753'}, {'id': 94068, 'title': {'romaji': 'Inmitsu Gakuen', 'english': 'The indecent honey school', 'native': '淫蜜学園'}, 'type': 'MANGA', 'format': 'MANGA', 'status': 'FINISHED', 'description': '0-8. Inmitsu Gakuen\r\n9. Kansen Byoutou: Nurenure Seishiki Jisshuu no Maki\r\n10. Utsutsu na Present (Reality Present)\r\n11. Gohoubi Toilet\r\n12. Disasters High\r\n13. Shouten Hijack\r\n14. Odemukae\r\n15-16. Wartburg no Reijou-tachi\r\n17. Ryoujoku no Elevator\r\n18. 
Shinya Hoiku: Inran Haha no Tsudoi\r\n19. Hentai Eigyou: Midara na Sales Lady\r\n20. Seiho Lady: Keiyaku no Himitsu\r\n21. Shanai Choukyou: Midara na Eigyou Lady\r\n22. Shinya Hoiku: Career Woman no Mikata', 'episodes': None, 'bannerImage': None, 'externalLinks': [], 'duration': None, 'chapters': 23, 'volumes': 1, 'genres': ['Hentai'], 'synonyms': ['Kansen Byoutou: Nurenure Seishiki Jisshuu no Maki', 
'Reality Present', 'Gohoubi Toilet', 'Disasters High', 'Shouten Hijack', 'Odemukae', 'Wartburg no Reijou-tachi', 'Ryoujoku no Elevator', 'Shinya Hoiku: Inran Haha no Tsudoi', 'Hentai Eigyou: Midara na Sales Lady'], 'averageScore': None, 'airingSchedule': {'nodes': []}, 'siteUrl': 'https://anilist.co/manga/94068'}]}})
>>> 
```


-------------------------------------------------------------------------------------------------------------------------------------------------------------
## Anime
![image](https://user-images.githubusercontent.com/63096193/125342684-cf61c480-e372-11eb-98fb-dd557f3e32a9.png)
```
>>> from anilistWrapPY.Anime.request import GetAnime
>>> GetAnime("Higehiro")
AniListAnime(data={'Page': {'media': [{'id': 114232, 'title': {'romaji': 'Hige wo Soru. Soshite Joshikousei wo Hirou.', 'english': 'Higehiro: After Being Rejected, I Shaved and Took in a High School Runaway', 'native': 'ひげを剃る。そして女子高生を拾う。'}, 'description': 'On his way home from drinking his sorrows away after being rejected by his crush, the 26 year old salaryman, Yoshida, finds a high school girl named Sayu sitting on the side of the road. Yoshida is completely drunk out of his mind and ends up letting Sayu stay at his place overnight. Not having the heart to put Sayu out on the streets since she ran away from home, Yoshida allows her to stay at his place... And so began the awkward, irritable, and slightly heartwarming relationship between a runaway high school girl and a salaryman living together.<br>\n<br>\n(Source: Crunchyroll)', 'startDate': {'year': 2021}, 'episodes': 13, 'season': 'SPRING', 'type': 'ANIME', 'format': 'TV', 'status': 'FINISHED', 'duration': 24, 'siteUrl': 
'https://anilist.co/anime/114232', 'studios': {'nodes': [{'name': 'project No.9'}, {'name': 'Dream Shift'}, {'name': 'Pony Canyon'}, {'name': 'Magic Capsule'}]}, 'trailer': {'id': 'nFljVg8xELU', 'site': 'youtube', 'thumbnail': 'https://i.ytimg.com/vi/nFljVg8xELU/hqdefault.jpg'}, 'externalLinks': [{'url': 'https://twitter.com/higehiro_anime/'}, {'url': 'http://www.higehiro-anime.com/'}, {'url': 'https://www.crunchyroll.com/higehiro-after-being-rejected-i-shaved-and-took-in-a-high-school-runaway'}, {'url': 'https://vrv.co/series/GXJHM3NW5/Higehiro-After-Being-Rejected-I-Shaved-and-Took-in-a-High-School-Runaway'}, {'url': 'https://www.youtube.com/playlist?list=PLwLSw1_eDZl04kRKOrkNNvS1Yht4lZ8QK'}], 'averageScore': 73, 'genres': ['Drama', 'Romance', 'Slice of Life'], 'bannerImage': 'https://s4.anilist.co/file/anilistcdn/media/anime/banner/114232-lWTVDRDLqAH1.jpg'}, {'id': 5983, 'title': {'romaji': 'Higepiyo', 'english': None, 'native': 'ひげぴよ'}, 'description': 'Higepiyo is a little chick with a mustache, who is seeking to aquire masculinity with his friend Hiroshi but ends up being entangled with a skin of heated milk.', 'startDate': {'year': 2009}, 'episodes': 39, 'season': 'SPRING', 'type': 'ANIME', 'format': 'TV_SHORT', 'status': 'FINISHED', 'duration': 5, 'siteUrl': 'https://anilist.co/anime/5983', 'studios': {'nodes': [{'name': 'Aniplex'}, {'name': 'Kinema Citrus'}]}, 'trailer': None, 'externalLinks': [], 'averageScore': 61, 'genres': ['Comedy'], 'bannerImage': None}]}})
>>> 
```

