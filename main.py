import praw
import config
from pprint import pprint
import pdb
from youtube import YoutubePage, youtube_url

num_requests = 0

def traverse_with_depth(comments, depth, max_depth, handler):
    """
    handle comments, but only up to a certain depth

    :param comment: a praw.objects.Comment object
    :param depth: the current depth in the search
    "param max_depth: the max depth we're willing to go
    :param handler: a function that takes a comment as an argument
    """
    if(depth > max_depth):
        return
    for comment in comments:
        handler(comment)
        if hasattr(comment, 'replies'):
            traverse_with_depth(comment.replies, depth + 1, max_depth, handler)

def print_youtube_info(comment):
    """
    handle a comment
    for now, print info about the youtube url if any

    :param comment: a praw.objects.Comment object 
    """
    global num_requests
    if not hasattr(comment, 'body'):
        return
    y_url = youtube_url(comment.body)
    if y_url:
        #check if we've already posted the youtube info
        if comment.id in get_replied_ids():
            print "Already replied"
            return
        page = YoutubePage(y_url)
        reply_text = make_reply(page)
        print reply_text
        if num_requests < config.MAX_REQUESTS:
            num_requests += 1
            try:
                comment.reply(reply_text)
                #record that we've posted the info
                record_replied(comment.id)
                print "Replied to comment!"
            except RateLimitExceeded:
                print "Oops - posted too often."

def make_reply(youtube_page):
    return (u"Youtube link: {}\n\n"
            u"Video title: {}\n\n"
            u"Video summary: {}").format(
                youtube_page.url, youtube_page.title, youtube_page.description
            )

def record_replied(id):
    with open(config.REPLIED_FILE, 'a') as replied_file:
        replied_file.write(id + '\n')

def get_replied_ids():
    with open(config.REPLIED_FILE, 'r') as replied_file:
        return replied_file.read().splitlines()

def main():
    global num_requests 

    user_agent = ("YoutubeTitleBot 1.0, "
                  "helpfully posting information for youtube links")
    r = praw.Reddit(user_agent = user_agent)
    r.login(config.USERNAME, config.PASSWORD)

    #just messing around for now
    submissions = r.get_subreddit(config.SUBREDDITS).get_hot(limit=10)
    num_requests += 2
    for submission in submissions:
        comments = submission.comments
        traverse_with_depth(comments, 0, 3, print_youtube_info)

if __name__ == '__main__':
    main()