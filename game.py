from board import Board


class Game:

    def __init__(self):
        self.board = Board()
        self.last = "Computer"
    
    def user_go(self):
        positions = {'1': (0,0), '2': (0,1), '3': (0,2), '4': (1,0),\
            '5': (1,1), '6': (1,2), '7':(2,0), '8':(2,1), '9': (2,2)}
        pos = input("Enter position which you want to mark: ")
        if pos not in positions:
            print("Incorrect input! Please enter a number from 1 to 9.")
            self.user_go()
        else:
            try:
                cell = positions[pos]
                self.board.make_move(cell)
                return True
            except IndexError:
                print("This position is already marked.")
                self.user_go()

    def computer_go(self):
        cell = self.board.make_a_tree()
        self.board.make_move(cell)


    def main(self):
        print("GAME STARTS")
        while self.board.has_winner() == 0:
            print("Board:")
            print(self.board)
            if self.last == "Computer":
                self.user_go()
                self.last = "User"
            elif self.last == "User":
                self.computer_go()
                self.last = "Computer"
        print("Board:")
        print(self.board)
        print("\nResult:")
        if self.board.has_winner() == 1:
            print("NOUGHT WINS")
        elif self.board.has_winner() == -1:
            print("CROSS WINS")
        elif self.board.has_winner() == 2:
            print("DRAW")



if __name__ == "__main__":
    game1 = Game()
    game1.main()