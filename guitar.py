class Guitar:
    def __init__(self):    #constructor de clase
        self.n_strings = 6


    def play(self):
        return "pam pam pam pam pam"


# INHERITANCE (child class) HERENCIA
class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8


    def play_louder(self):
        return "pam pam pam pam pam".upper()


my_guitar = ElectricGuitar()
print("child class: ", my_guitar.n_strings)
print("child class plays: ", my_guitar.play_louder())
print("parent class: ", Guitar().n_strings)
print("parent class plays: ", Guitar().play())
