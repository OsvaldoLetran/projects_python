import random


class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ''


    def choose(self):
        self.choice = input('{name}, select rock, paper or scissor: '.format(name = self.name))
        print('{name} selects {choice}'.format(name = self.name, choice = self.choice))


    def choose_pc(self):
        self.choice = random.choice(['rock', 'paper', 'scissor'])
        print(f'{self.name} selects {self.choice}')


    def to_num_choice(self):
        switcher = {
            'rock': 0,
            'paper': 1,
            'scissor': 2
        }
        return switcher[self.choice]


    def increment_point(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]

        p1.choose()
        p2.choose_pc()
        result = self.compare_choices(p1, p2)
        print('Round resulted in {result}'.format(result = self.get_result_as_string(result)))

        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()
        else:
            print('No points for anybody')


    def compare_choices(self, p1, p2):
        return self.rules[p1.to_num_choice()][p2.to_num_choice()]


    def get_result_as_string(self, result):
        res = {
            0 : 'draw',
            1 : 'win',
            -1 : 'loss'
        }
        return res[result]


class Game:
    def __init__(self):
        self.end_game = False
        self.participant = Participant('Player1')
        self.two_participant = Participant('Player2')


    def start(self):
        while not self.end_game:
            GameRound(self.participant, self.two_participant)
            self.check_end_condition()


    def check_end_condition(self):
        answer = input('Continue game: y/n ')

        if answer == 'y':
            GameRound(self.participant, self.two_participant)
            self.check_end_condition()
        else:
            print('Game ended, {p1name} has {p1points} and {p2name} has {p2points}'.format(
                p1name = self.participant.name, 
                p1points = self.participant.points, 
                p2name = self.two_participant.name, 
                p2points = self.two_participant.points
            ))
            self.determine_winner()
            self.end_game = True


    def determine_winner(self):
        result_string = "It's a draw"
        
        if self.participant.points > self.two_participant.points:
            result_string = 'Winner is {name}'.format(name = self.participant.name)
        elif self.participant.points < self.two_participant.points:
            result_string = 'Winner is {name}'.format(name = self.two_participant.name)

        print(result_string)


game = Game()
game.start()
