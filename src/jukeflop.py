"""
JukeFlop
"""

from music_api import MusicAPI

class JukeFlop():
    """
    JukeFlop
    """
    def __init__(self, c, m_id):
        self.music = MusicAPI()
        self.cmd = c
        self.music_id = m_id

    def command(self):
        """
        determines which jukeflop action to take based on arguments
        """
        if self.cmd == 'test':
            self.run_test()
        elif self.cmd == 'play':
            print('play funciton goes here')
        elif self.cmd == 'stop':
            print('stop function goes here')


    def run_test(self):
        """
        used for debuggin / testing basic functionality
        """
        print('COMMAND: ', self.cmd, ' | MUSIC_ID: ', self.music_id)
        self.music.test_api(self.music_id)
