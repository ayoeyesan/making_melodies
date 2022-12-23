# Ayo Eyesan
# Making Meldoies

import note

class Melody:
    def __init__(self, filename):
        """ (str) -> (NoneType)
        Constructor opens the file, creates an instance attribute for the title and author, then
        creates an instance attribute called notes for a list that contains a sequence of Note
        objects, one for every note in the file
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> len(hot_cross_buns.notes)
        17
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print(happy_birthday.notes[0])
        0.5 B 4 NATURAL
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25

        """
        if type(filename) != str:
            raise AssertionError('Filename must be a string')
        notes_1 = []
        notes_2 = []
        self.notes = []
        self.line_counter = 0
        self.filename = filename
        fobj = open(self.filename, 'r')
        for line in fobj:
            self.line_counter += 1
            if self.line_counter == 1:
                self.title = line.strip('\n')
            if self.line_counter == 2:
                self.author = line.strip('\n')
            if self.line_counter >= 3:
                notes_1.append(line)
        fobj.close()
        true_counter = 0
        true_list = []
        for elm in notes_1:
            if 'true' in elm:
                true_counter += 1
                elm = elm.strip('true\n')
                notes_2.append(elm)
                true_list.append(elm)
                if true_counter == 2:
                    for elm in true_list:
                        notes_2.append(elm)
                    true_counter = 0
                    true_list = []
            if 'false' in elm:
                elm = elm.strip('false\n')
                notes_2.append(elm)
                if true_counter == 1:
                    true_list.append(elm)
        for elm in notes_2:
            x = elm.split(' ')
            self.notes.append(note.Note(float(x[0]), x[1], int(x[2]), x[3]))
    def play(self, player):
        """ (music player) -> (NoneTyppe)
        Calls the play method on each Note object of the notes instance attribute in order,
        passing the music player object each time as argument
        
        """
        if player != player:
            raise AssertionError('Input must be player')
        for elm in self.notes:
            elm.play(player)
    def get_total_duration(self):
        """ (NoneType) -> (float)
        Returns the total duration of the song as a float
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> tetris = Melody("tetris.txt")
        >>> tetris.get_total_duration()
        15.5
        >>> x = Melody(12345)
        >>> x.get_total_duration()
        AssertionError: Filename must be a string
        """
        total_duration = 0
        list_1 = []
        list_2 = []
        for elm in self.notes:
            list_1.append(str(elm))
        for elm in list_1:
            list_2.append(elm.split(' '))
        for l in list_2:
            total_duration += float(l[0])
        return total_duration
    def lower_octave(self):
        """ (NoneType) -> (int)
        Reduces the octave of all notes in the song by 1 and returns True, or returns False if octave
        reduced below 1

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        >>> tetris = Melody("tetris.txt")
        >>> tetris.lower_octave()
        True
        >>> tetris.notes[1].octave
        3
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.lower_octave()
        True
        >>> tetris.notes[3].octave
        3
        
        """
        list_1 = []
        list_2 = []
        list_3 = []
        for elm in self.notes:
            list_1.append(str(elm))
        for elm in list_1:
            list_2.append(elm.split(' '))
        for l in list_2:
            duration = float(l[0])
            pitch = str(l[1])
            octave = int(l[2]) - 1
            if octave < 1 or octave > 7:
                return False
            accidental = str(l[3])
            list_3.append(note.Note(duration, pitch, octave, accidental))
        self.notes = []
        for l in list_3:
            self.notes.append(l)
        return True
    def upper_octave(self):
        """ (NoneType) -> (int)
        Increases the octave of all notes in the song by 1 and returns True, or returns False if octave
        reduced below 1 or above 7

        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        >>> tetris = Melody("tetris.txt")
        >>> tetris.lower_octave()
        True
        >>> tetris.notes[1].octave
        5
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.lower_octave()
        True
        >>> tetris.notes[3].octave
        5
        
        """
        list_1 = []
        list_2 = []
        list_3 = []
        for elm in self.notes:
            list_1.append(str(elm))
        for elm in list_1:
            list_2.append(elm.split(' '))
        for l in list_2:
            duration = float(l[0])
            pitch = str(l[1])
            octave = int(l[2]) + 1
            if octave < 1 or octave > 7:
                return False
            accidental = str(l[3])
            list_3.append(note.Note(duration, pitch, octave, accidental))
        self.notes = []
        for l in list_3:
            self.notes.append(l)
        return True
    def change_tempo(self, change):
        """ (float) -> (NoneType)
        Returns nothing, multiplies the duration of each note by the given float.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(2)
        >>> happy_birthday.get_total_duration()
        26
        >>> tetris.notes[1].octave
        5
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.lower_octave(0.05)
        True
        >>> tetris.notes[3].octave
        0.65
        
        """
        if type(change) != float:
            raise AssertionError('Change input must be a float')
        list_1 = []
        list_2 = []
        list_3 = []
        for elm in self.notes:
            list_1.append(str(elm))
        for elm in list_1:
            list_2.append(elm.split(' '))
        for l in list_2:
            duration = float(l[0]) * change
            pitch = str(l[1])
            octave = int(l[2])
            if octave < 1 or octave > 7:
                return False
            accidental = str(l[3])
            list_3.append(note.Note(duration, pitch, octave, accidental))
        self.notes = []
        for l in list_3:
            self.notes.append(l)
        return True