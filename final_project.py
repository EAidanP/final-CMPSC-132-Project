import random 
class Game:
    def __init__(self, p1_name, p2_name, p1_superpower, p2_superpower): #this is the definition of the game class which utilizes instances of the map and player class to execute the snakes and ladders game
        self.start = True 
        self.new_map = Map()
        self.p1 = Player(p1_name,p1_superpower, self.new_map) 
        self.p2 = Player(p2_name,p2_superpower, self.new_map)
        self.turn = 0
        self.winner = ''
    
    def update(self): #this is the update method which will run everytime it is called, and upon being called it will determine who's turn it it to roll a dice and then execute the updates on that player
        choice = input(":")
        if choice.lower() == 'roll':
            if self.turn %2 == 0:
                if self.p1.superpower == "block-opponent": #this is the block opponent superpower which has a chance each time player 1 or 2 has a turn to activate 
                    chance_1 = random.randint(1,25)
                    if chance_1 in range(1,4):
                        self.p1.update()
                        self.turn += 2
                        print(f"{self.p1.name} has skipped {self.p2.name}'s next turn")
                    else:
                        self.turn += 1
                        self.p1.update()
                else:
                    self.p1.update()
                    self.turn += 1
                
                if self.p1.position == 100: #this is the win condition if either player 1 or 2 lands exactly on the 100th spot the game is over
                    self.start = False
                    self.winner = self.p1.name
                else:
                    print(f'player 1 is on space {self.p1.position}')

            elif self.turn % 2 == 1:#this is the update method which will run everytime it is called, and upon being called it will determine who's turn it it to roll a dice and then execute the updates on that player
                if self.p2.superpower == "block-opponent":
                    chance_2 = random.randint(1,25)
                    if chance_2 in range(1,4):
                        self.p2.update()
                        self.turn += 2
                        print(f"{self.p2.name} has skipped {self.p1.name}'s next turn")
                    else:
                        self.p2.update()
                        self.turn += 1
                else:
                    self.p2.update()
                    self.turn += 1
            
                if self.p2.position == 100: #this is the win condition, if player 1 or 2 lands exactly on the 100th spot, then the game is over
                    self.start = False
                    self.winner = self.p2.name
                else:
                    print(f'player 2 is on space {self.p2.position}')
        

    def run(self): #this is the run method, which calls the update method, so long as the game is still going 
        while self.start:
            self.update()
        return self.winner 


class Player: #this is the player class which houses the attributes and methods necessary for the player object to complete its tasks on the snakes and ladders board
    def __init__(self,name,superpower,map):
        self.name = name
        self.superpower = superpower.lower() 
        self.position = 0
        self.map = map
    
    def update(self):#this is the player update method, which is called everytime the game update method is called, however it is only either called on player 1 or 2, not both
        roll = random.randint(1,6)
        if self.superpower == "multiply-roll": # this is the multiply roll super power which has a chance to double a players roll
            chance = random.randint(1,25)
            if chance in range(1,6):
                roll = roll * 2
                print(f'{self.name} doubled their roll')
        new_position = self.position + roll

        if new_position in self.map.ladders:
            new_position = self.map.ladders[new_position]

        elif new_position in self.map.snakes:
            if self.superpower == "skip-snakes": #this is the skip-snakes superpower logic which has a chance after everyturn, if the player lands on a snake, to not follow the snake down
                chance = random.randint(1,25)
                if chance in range(5,26): #if chance rolls for the player to fall down the snake 
                    new_position = self.map.snakes[new_position]
                else:
                    new_position = new_position
            else:
                new_position = self.map.snakes[new_position]


        if new_position > 100: #this is the logic for if the player goes over the board limit
            self.position = self.position
        else:
            self.position = new_position 
                
                

class Map:
    def __init__(self): #this is the map class, which houses the locations of all the snakes and ladders, it holds them in dicitonaries, with their start being the key and their end being the value
        self.snakes = {}
        self.ladders = {}

        for i in range(5):
            position_snake = random.randint(10,95)
            while position_snake in self.snakes.values() or position_snake in self.snakes or position_snake in self.ladders.values() or position_snake in self.ladders: #chehcking to make sure the start hasnt been used as a start or end for a snake or ladder already
                position_snake = random.randint(10,95)
            snake_length = random.randint(3,7)
            while position_snake - snake_length <= 5 or position_snake - snake_length in self.snakes.values() or position_snake - snake_length in self.snakes or position_snake - snake_length in self.ladders.values() or position_snake - snake_length in self.ladders:#chehcking to make sure the end hasnt been used as a start or end for a snake or ladder already
                snake_length = random.randint(3,7)
            self.snakes[position_snake] = position_snake - snake_length
        
        for i in range(5):
            position_ladder = random.randint(5,95)
            while position_ladder in self.ladders.values() or position_ladder in self.ladders or position_ladder in self.snakes.values() or position_ladder in self.snakes:#chehcking to make sure the start hasnt been used as a start or end for a snake or ladder already
                position_ladder = random.randint(5,95)
            ladder_length = random.randint(3,10)
            while position_ladder + ladder_length >= 95 or position_ladder + ladder_length in self.ladders.values() or position_ladder + ladder_length in self.ladders or position_ladder + ladder_length in self.snakes.values() or position_ladder + ladder_length in self.snakes:#chehcking to make sure the end hasnt been used as a start or end for a snake or ladder already
                ladder_length = random.randint(3,10)

            self.ladders[position_ladder] = position_ladder + ladder_length


def main():

    intro = (
        'This game is snakes and ladders, it is a 2 player game in which players roll a dice to adnvance spaces. \n'
        'each player will input their player name and superpower into the console after this message. \n'
        'after that the two players will take turns moving by inputing the word "roll", which rolls a die.\n'
        'the players will take turns moving until one of the two reaches the end, which is after 100 spaces. \n'
        'however,the winner must land eaxctly on the 100th space to win, and along the way players may run into snakes or ladders. \n'
        'ladders will move the player up a certain number of spaces and snakes will move the player back.' )
    print(intro) 

    player_1_name = input("what is the first player's name?: ")
    while len(player_1_name) == 0 or len(player_1_name.strip()) == 0:
        print('the players name must be a string of numbers, characters or other symbols')
        player_1_name = input("what is player 1's name?: ")
    
    print("Now choose a superpower. Possible superpowers:")
    print('skip-snakes: chance to avoid a snake')
    print('multiply-roll: chance to double your roll')
    print("block-opponent: chance to block the opponent's next turn")

    player_1_superpower = input("what superpower would player 1 like? (enter the eaxact name above): ")
    while player_1_superpower not in ["skip-snakes","multiply-roll","block-opponent"]:
        print('the players superpower must be from the list given, and spelled the same way')
        player_1_superpower = input("what is player 1's superpower?: ")
    
    player_2_name = input("what is the second player's name?: ")
    while len(player_2_name) == 0 or len(player_2_name.strip()) == 0:
        print('the players name must be a string of numbers, characters or other symbols')
        player_2_name = input("what is player 2's name?: ")
    
    print("Now choose a superpower. Possible superpowers:")
    print('skip-snakes: chance to avoid a snake')
    print('multiply-roll: chance to double your roll')
    print("block-opponent: chance to block the opponent's next turn")

    player_2_superpower = input("what superpower would player 2 like?(enter the eaxact name above): ")
    while player_2_superpower not in ["skip-snakes","multiply-roll","block-opponent"]:
        print('the players superpower must be from the list given, and spelled the same way')
        player_2_superpower = input("what is player 2's superpower?: ")

    new_game = Game(player_1_name,player_2_name,player_1_superpower,player_2_superpower) #creates a new game object
    winner = new_game.run() #sets the winner object equal to the output of the run method used on the new game object, which returns the winners name
    print(f'the winner is {winner}')


if __name__ == "__main__":
    main()