#modules
import random #for coin toss

board_values = [None,"1","2","3","4","5","6","7","8","9"]
def print_board(values):
    board_layout = ("   |   |   ",
                    " "+values[1]+" | "+values[2]+" | "+values[3]+" ",
                    "   |   |   ",
                    "-----------",
                    "   |   |   ",
                    " "+values[4]+" | "+values[5]+" | "+values[6]+" ",
                    "   |   |   ",
                    "-----------",
                    "   |   |   ",
                    " "+values[7]+" | "+values[8]+" | "+values[9]+" ",
                    "   |   |   ")    
    for i in range(0,len(board_layout)):
        print(board_layout[i])
def coin_toss():
    return random.choice(["X", "O"])
def reset(values):
    reset_values = [None,"1","2","3","4","5","6","7","8","9"]
    for i in range(0,len(values)):
        values[i]= reset_values[i]
    return values

#classes
class Game:
    def __init__(self, active):
        self.active = active
        print("Welcome to Tic-Tac-Toe!")
        input("Press enter to flip a coin for X or O")
        print("You are {}".format(random.choice(["X", "O"])))
    def play(self, turn):
        print_board(board_values)
        if (turn%2!=0):
            choice = input("X, pick a spot:")
            board_values[int(choice)] = "X"
        else:
            choice = input("O, pick a spot:")
            board_values[int(choice)] = "O"
    def win_check(self, values, turns):
        cr_top = (1,2,3) #cr-top
        cr_mid = (4,5,6) #cr-middle
        cr_bot = (7,8,9) #cr-bottom
        dn_lft = (1,4,7) #dn-left
        dn_mid = (2,5,8) #dn-middle
        dn_rgt = (3,6,9) #dn-right
        dgn_lr = (1,5,9) #dgn-left to right
        dgn_rl = (3,5,7) #dgn-right to left

        three_iar = (cr_top, cr_mid, cr_bot, dn_lft, dn_mid, dn_rgt, dgn_lr, dgn_rl)
        for i in three_iar:
            x_streak = 0
            o_streak = 0
            for char in i:
                if(values[char]=="X"):
                    x_streak+=1
                elif(values[char]=="O"):
                    o_streak+=1
            if(x_streak == 3):
                print_board(values)
                print("X Wins!")
                self.active = False
            elif(o_streak ==3):
                print_board(values)
                print("O Wins!")
                self.active = False
                           
        
#main
game = Game(True)
turn = 0
while (game.active == True):
    turn+=1
    game.play(turn)
    game.win_check(board_values, turn)
    if(turn==9):
        print_board(board_values)
        replay = input("Cats Game! Rematch?(y/n)")
        if(replay == "y"):
            reset(board_values)
            print("Switch!")
            turn=0
            continue
        else:
            game.active = False
    
  
