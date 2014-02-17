from urlparse import urlparse

class Post:
    
    @staticmethod
    #determines if a url is a youtube video
    #url is a string
    def isYoutubePost(url):
        host_name = urlparse(url).hostname
        print(host_name)

if __name__ == '__main__':
    Post.isYoutubePost("http://www.youtube.com/video")