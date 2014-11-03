# YoutubeBot - a reddit bot for posting information about youtube links

This is a simple reddit bot that does the following:
* searches for reddit comments with a link to a youtube video
* replies to those comments with the name of that video and a short description of it

### Why did I make it?

Laziness.  Often, I am reading reddit and someone comments with a youtube video.  I often want to know what the video is but am too lazy to open the link in a new tab.  This bot solves that problem.

### License

This code is available under a GNU General Public License.  In particular, I make no claims about its usability - it is possible that if you run this program it will crash your computer, delete all your files, and run over your dog.  I take no responsibility if you run it.

### Use

Simply run main.py as a cron job every 10 minutes or so.  You will need to fill in the following fields in a config.py file:
* USERNAME: the reddit username of your bot
* PASSWORD: the password for your reddit bot
* SUBREDDITS: the subreddits you want the bot to comment in
* MAX_REQUESTS: the maximum number of requests you want it to make per run.  Set it to 30.
* REPLIED_FILE: a file that keeps track of the comments you've replied to already.  I name mine replied.txt.  Make sure it exists.