
class EnigmaCipher:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self):
        self.rotors = []
        self.rotorsettings = [("III", 0),
                            ("II", 0),
                            ("I", 0)]
        self.reflectorsetting = "B"
        self.plugboardsetting = []

        # Create the plugboard
        self.plugboard = Plugboard(self.plugboardsetting)

        # Create each of the rotors
        for i in range(len(self.rotorsettings)):
            self.rotors.append(Rotor(self.rotorsettings[i]))

        # Create reflector
        self.reflector = Reflector(self.reflectorsetting)
        #self.shiftedAlphabet = self.GetShiftedAlphabet(key)
        
    def GetShiftedAlphabet(self,index):
        shifted_alphabet = self.alphabet[index:] + self.alphabet[:index]
        return shifted_alphabet

    def Encode(self,c):
        c = c.upper()

        if not(c.isalpha()):
            return c
        #we rotate the first rotor once
        self.rotors[0].Rotate()

        for i in range(len(self.rotors)-1):
            if self.rotors[i].turnover:
                self.rotors[i].turnover = False
                self.rotors[i+1].Rotate()

        index = self.plugboard.Forward(c)
        #print(index)
        for r in self.rotors:
            index = r.Forward(index)
            #print(index)

        index = self.reflector.Forward(index)

        for r in reversed(self.rotors):
            index = r.Reverse(index)

        c = self.plugboard.Reverse(index)
        return c

    def Reset(self):
        for r in self.rotors:
            r.Reset()
#    def Encrypt(self, message):
#        encrypted_message = ""
#        for c in message:
#            if c.isalpha():
#                if c.isupper():
#                    ind = self.alphabet.index(c)
#                    char = self.shiftedAlphabet[ind]
#                else:
#                    ind = self.alphabet.index(c.upper())
#                    char = self.shiftedAlphabet[ind].lower()
#                encrypted_message += char
#            else:
#                encrypted_message += c
#        return encrypted_message
#    def Decrypt(self,message):
#        decrypted_message = ""
#        for c in message:
#            if c.isalpha():
#                if c.isupper():
#                    ind = self.shiftedAlphabet.index(c)
#                    char = self.alphabet[ind]
#                else:
#                    ind = self.shiftedAlphabet.index(c.upper())
#                    char = self.alphabet[ind].lower()
#                decrypted_message += char
#            else:
#                decrypted_message += c
#        return decrypted_message

#cc = CaesarCipher(2)
#message = "This is a really long, complicated message. \n I wonder if this will work."
#em = cc.Encrypt(message)
#print(em)

#print(cc.Decrypt(em))

class Rotor:
    def __init__(self, settings):
        """ Setup an enigma transformation rotor """
        self.setting = settings[0]
        self.ringoffset = settings[1]
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings = {
                "I":    ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["R"], ["Q"]],
                "II":   ["AJDKSIRUXBLHWTMCQGZNPYFVOE", ["F"], ["E"]],
                "III":  ["BDFHJLCPRTXVZNYEIWGAKMUSQO", ["W"], ["V"]],
                "IV":   ["ESOVPZJAYQUIRHXLNFTGKDCMWB", ["K"], ["J"]],
                "V":    ["VZBRGITYUPSDNHLXAWMJQOFECK", ["A"], ["Z"]],
                "VI":   ["JPGVOUMFYQBENHZRDKASXLICTW", ["AN"], ["ZM"]],
                "VII":  ["NZJHGRCXMYSWBOUFAIVLPEKQDT", ["AN"], ["ZM"]],
                "VIII": ["FKQHTLXOCBJSPDZRAMEWNIUYGV", ["AN"], ["ZM"]]}
        self.turnovers = self.settings[self.setting][1]
        self.notch = self.settings[self.setting][2]
        self.sequence = None
        self.turnover = False
        self.Reset()
        #self.
    def Reset(self):
        """ Reset the rotor positions """
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.sequence = self.Sequence_settings()
        self.Ring_settings()

    def Sequence_settings(self):
        """ Set the intial sequence """
        return self.settings[self.setting][0]

    def Ring_settings(self):
        """ Apply the initial ring settings offset """
        for _ in range(self.ringoffset):
            self.rotate()
    def Rotate(self):
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.base = self.base[1:] + self.base[:1]
        if self.base[0] in self.turnovers:
            self.turnOver = True
    def Forward(self, index):
        #print("index:" + str(index))
        #print(self.alphabet[index])
        #print(self.shiftedAlphabet[index])
        #print("new index:" + str(self.shiftedAlphabet.index(self.alphabet[index])))
        return self.base.index(self.sequence[index])
    def Reverse(self, index):
        return self.sequence.index(self.base[index])

class Reflector:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self,setting):
        self.setting = setting
        self.base = self.alphabet
        self.settings = {"A":   "EJMZALYXVBWFCRQUONTSPIKHGD",
                        "B":    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                        "C":    "FVPJIAOYEDRZXWGCTKUQSBNMHL"}
        self.sequence = self.settings[setting]
    def Forward(self,index):
        return self.sequence.index(self.base[index])

class Plugboard:
    """ The plugboard (Steckerbrett in German) permitted variable wiring
    that could be reconfigured by the operator.
    It was introduced on German Army versions in 1930, and was soon adopted
    by the Navy as well. The plugboard contributed a great deal to the
    strength of the machine's encryption: more than an extra rotor would
    have done. Enigma without a plugboard (known as unsteckered Enigma)
    can be solved relatively straightforwardly using hand methods;
    these techniques are generally defeated by the addition of a plugboard,
    and Allied cryptanalysts resorted to special machines to solve it.

    """
    def __init__(self, mapping):
        """ mapping = [("A", "B"), ("C", "D")] """
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mapping = {}

        for m in self.base:
            self.mapping[m] = m

        for m in mapping:
            self.mapping[m[0]] = m[1]
            self.mapping[m[1]] = m[0]

    def Forward(self, c):
        """ Return the index of the character """
        return self.base.index(self.mapping[c])

    def Reverse(self, index):
        """ Return the character of the index """
        return self.mapping[self.base[index]]

enig = EnigmaCipher()
message = "Hello. This is a short sentence, but let's see if this machine can do it."
em = ""

for c in message:
    print("Letter in message:" + c)
    d = enig.Encode(c)
    
    em += d

print(em)

enig.Reset()
m = ""
for c in em:
    d = enig.Encode(c)
    m += d
print(m)
