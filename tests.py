import unittest  # @UnresolvedImport
from youtube import YoutubePage, youtube_url

class YoutubeTest(unittest.TestCase):
    def setUp(self):
        self.youtube_page = YoutubePage('https://www.youtube.com/watch?v=fu7D0KKmZGM')
        
    def test_parsing(self):
        self.assertEqual(self.youtube_page.title,u'Tiny Hamster in a Tiny Playground')
        self.assertEqual(self.youtube_page.description,u"My tiny dwarf hamster is back again. This time Chicken (yup, that's her name) is exploring her handmade playground. Watch her slide, swing and play. Thanks D...")

    def test_youtube_url(self):
        self.assertEqual(youtube_url('www.youtube.com/watch?v=asdfads'), 'http://www.youtube.com/watch?v=asdfads')
        self.assertEqual(youtube_url('http://www.youtube.com/watch?v=asdfads'), 'http://www.youtube.com/watch?v=asdfads')
        self.assertEqual(youtube_url('https://www.youtube.com/watch?v=asdfads'), 'http://www.youtube.com/watch?v=asdfads')
        self.assertEqual(youtube_url('''Tough? Whaddya mean tough? You sayin they're hard to chew? You tryin to say they are rigid? Maybe have no intelligence?  
[THAT'S IT!](https://www.youtube.com/watch?v=0gVurt8TjeA)
People are simply repulsing if they think these poor birds deserve to be treated like dirt.'''), 'http://www.youtube.com/watch?v=0gVurt8TjeA')
        self.assertEqual(youtube_url('This comment does not have a youtube url'), None)

        
if(__name__ == '__main__'):
    unittest.main()