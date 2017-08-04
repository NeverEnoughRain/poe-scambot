import threading
import winsound
import os

class BeepThread(threading.Thread):
    """Thread that handles audio notifications."""
    
    def __init__(self):
        """Initializes the thread with a reference to the creator thread."""
        threading.Thread.__init__(self)
        self.loc = os.getcwd() + "\\solemn.wav"
        self.start()
        
    def run(self):
        """Plays a sound less offensive to the ears than the default. Everything beep-related has been purged."""
        winsound.PlaySound(self.loc, winsound.SND_FILENAME)
    
    def kill(self):
        """Thread dies in 1 second anyways."""
        pass