

class Player:

    def __init__(self, name):
        self.__points = 0
        self.__player_name = name
        self.__throws = 0
        self.__all_points = 0
        self.__hits = 0
        self.__thrown_points = 0
        self.__percentage = 0.0

    def get_name(self):
        return self.__player_name

    def add_points(self, points):
        self.__throws += 1
        self.__thrown_points = points
        if self.__points + self.__thrown_points > 50:
            print(self.__player_name + " gets penalty points!")
            self.__points = 25
            return True
        if self.__points + self.__thrown_points <= 50:
            self.__points += self.__thrown_points
            if 40 <= self.__points <= 49:
                remaining_points = 50 - self.__points
                print(self.__player_name + " needs only " +
                      str(remaining_points) +
                      " points. It's better to avoid knocking down the pins "
                      "with higher points.")
        self.__all_points += self.__thrown_points

    def average(self):
        average = self.__all_points / self.__throws
        if self.__thrown_points > average:
            print("Cheers " + self.__player_name + "!")

    def hit_percentage(self):
        if self.__thrown_points > 0:
            self.__hits += 1
        self.__percentage = (self.__hits / self.__throws) * 100

    def has_won(self):
        if self.__points == 50:
            return True
        else:
            return False

    def get_percentage(self):
        return self.__percentage

    def get_points(self):
        return self.__points

def main():

    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        
        if not in_turn.add_points(pts):
            in_turn.average()

        in_turn.hit_percentage()
                        
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p", end="")
        print(",", "hit percentage {:.1f}".format(player1.get_percentage()))
        print(player2.get_name() + ":", player2.get_points(), "p", end="")
        print(",", "hit percentage {:.1f}".format(player2.get_percentage()))
        print("")

        throw += 1


main()

