class Guitar:
    def __init__(self, n_strings):    #constructor de clase
        self.n_strings = n_strings


    def play(self):
        return "pam pam pam pam pam"


# INHERITANCE (child class) HERENCIA
class ElectricGuitar(Guitar):
    def __init__(self, n_strings):
        super().__init__(n_strings)


    def play_louder(self):
        return "pam pam pam pam pam".upper()


guitar = Guitar(6)
my_guitar = ElectricGuitar(8)
print("child class: ", my_guitar.n_strings)
print("child class plays: ", my_guitar.play_louder())
print("parent class: ", guitar.n_strings)
print("parent class plays: ", guitar.play())
