import unittest  # @UnresolvedImport
from youtube import YoutubePage

class YoutubeTest(unittest.TestCase):
    def setUp(self):
        self.youtube_page = YoutubePage('https://www.youtube.com/watch?v=fvxqnQmahTA')
        
    def test_parsing(self):
        self.assertEqual(self.youtube_page.title,u'Minions - Banana Song (Full Song)')
        self.assertEqual(self.youtube_page.description,u'The "Banana Song" taken from the amazing new upcoming movie "Despicable Me 2".')
        
if(__name__ == '__main__'):
    unittest.main()