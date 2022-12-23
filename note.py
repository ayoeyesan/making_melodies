# Ayo Eyesan
# Making Meldoies

import musicalbeeps

class Note:
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        """ (float, str, int, str) -> (NoneType)
        Constructor creates instance attributes for each input value
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        B
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.accidental
        natural
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.duration
        2.0
        
        """
        if duration < 0 or type(duration) != float:
            raise AssertionError('Duration input not valid')
        if pitch != 'A' and pitch != 'B' and pitch != 'C' and pitch != 'D' and pitch != 'E' and pitch != 'F' and pitch != 'G' and pitch != 'R':
            raise AssertionError('Pitch input not valid')
        if type(octave) != int or octave < 1 or octave > 7: 
            raise AssertionError('Octave input not valid')
        if accidental != 'sharp' and accidental != 'SHARP' and accidental != 'natural' and accidental != 'NATURAL' and accidental != 'flat' and accidental != 'SHARP' :
            raise AssertionError('Accidental input not valid')
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
    def __str__(self):
        """ (NoneType) -> (str)
        Returns a string of the format 'DURATION PITCH OCTAVE ACCIDENTAL' ' where each of the
        four words refer to the appropriate instance attributes
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        >>> note = Note(2, "B", 4, "natural")
        >>> print(note)
        AssertionError: Duration input not valid
        >>> note = Note(2.0, "B", 4, "Natural")
        >>> print(note)
        AssertionError: Accidental input not valid
        
        """
        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave ) + ' ' + self.accidental
    def play(self, player):
        """ (music player) -> (NoneTyppe)
        Method constructs the note string that the play_note method accepts, then passes the note
        string and duration to it so that the note can be played through the speakers
        
        """
        if player != player:
            raise AssertionError('Input must be player')
        final_string = ''
        duration_2 = 0
        list_1 = Note.__str__(self).split(' ')
        duration_2 += float(list_1[0])
        final_string += str(list_1[1])
        final_string += str(list_1[2])
        if list_1[3] == 'sharp':
            final_string += '#'
        if list_1[3] == 'flat':
            final_string += 'b'
        if list_1[1] == 'R':
            final_string = 'pause'
        player.play_note(final_string, duration_2)