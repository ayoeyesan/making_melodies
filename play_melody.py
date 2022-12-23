import musicalbeeps
from melody import Melody

if __name__ == "__main__":
    player = musicalbeeps.Player()
    weasel = Melody("weasel.txt")
    weasel.upper_octave()
    weasel.play(player)
    
