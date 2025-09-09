from youtube_search import YoutubeSearch
from langchain_community.document_loaders import YoutubeLoader

videos = YoutubeSearch("미국 대선", max_results=5).to_dict()

for video in videos:
    video['video_url'] = ("https://www.youtube.com" + video["url_suffix"])
    loader = YoutubeLoader.from_youtube_url(video['video_url'], language=["en", "ko"], add_video_info=True)
    video['content'] = loader.load()
    

print(videos)