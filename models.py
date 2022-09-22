"""This modul of all models in this game
"""
from random import randint
from game_exceptions import EnemyDown, GameOver
from settings import PL_LIVES, valid_input_value


class Enemy:
    """class for creating Enemy objects
    """
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """creating a random enemy selection

        Returns:
            int: random number
        """
        return randint(1, 3)

    def decrease_lives(self):
        """decrease in the lives of the enemy, if the lives are over - 
        the creation of a new enemy
        Raises:
            EnemyDown: raises an exception to create a new Enemy object
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """This parent class for creating Player objects for mode - Normal
    """
    allowed_atacks = None
    score = 0

    def __init__(self, name):
        self.name = name
        self.lives = PL_LIVES

    @staticmethod
    def fight(attack, defense):
        """returns the result of the attack/defense
        Args:
            attack (int): number
            defense (int): number
        Returns:
            int: result of fight
        """
        if attack == defense:
            return 0
        elif (attack == 1 and defense == 2) or\
            (attack == 2 and defense == 3) or\
                (attack == 3 and defense == 1):
            return 1
        else:
            return -1

    def decrease_lives(self):
        """This method reduces the player's lives, and if the lives are over, \
            throws an exception about the end of the game
        Raises:
            GameOver: GameOver: throws a game over exception
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        """takes input (1, 2, 3) from the player;
        accepts enemy attack from object enemy_obj;
        call the fight() method;
        If the result is 0, enter "It's a draw!"
        If 1 = "You attacked successfully!" that change the number of opponent's lives by 1;
        If -1 = "You missed!"
        """
        print(f"""____________________________\n
{self.name} lives - {self.lives}\n 
ENEMY lives - {enemy_obj.lives}\n
Your Attack NOW""")
        enemy_atack = enemy_obj.select_attack()
        self.allowed_atacks = valid_input_value()
        result = self.fight(self.allowed_atacks, enemy_atack)
        if result == 0:
            print("it's Draw\n____________________________")
        elif result == 1:
            print("You attacked successfully!\n____________________________")
            self.score += 1
            enemy_obj.decrease_lives()
        elif result == -1:
            print("You missed!\n____________________________")
        print("Your score:", self.score)

    def defence(self, enemy_obj):
        """takes input (1, 2, 3) from the Enemy;
        accepts enemy attack from Player;
        call the fight() method;
        If the result is 0, enter "It's a draw!"
        If 1 = "Enemy attacked successfully!" that change 
        the number of opponent's lives by 1;
        If -1 = "You defended yourself!"
        """
        print(f"""____________________________\n
{self.name} lives - {self.lives}\n 
ENEMY lives - {enemy_obj.lives}\n
Your Defence NOW""")
        enemy_atack = enemy_obj.select_attack()
        self.allowed_atacks = valid_input_value()
        result = self.fight(enemy_atack, self.allowed_atacks)
        if result == 0:
            print("it's Draw\n____________________________")
        elif result == 1:
            print("Enemy attacked successfully!\n____________________________")
            self.decrease_lives()
        elif result == -1:
            print("You defended yourself!\n____________________________")
        print("Your score:", self.score)


class PlayerHard(Player):
    """This child class for creating Player objects for mode - Normal

    Args:
        Player (class): name and mode(hard)
    """
    def __init__(self, name, hard):
        super().__init__(hard)
        self.name = name
        self.hard = hard

    def attack(self, enemy_obj):
        """reassign the attack method of the parent class Player
        """
        print(f"""____________________________\n
{self.name} lives - {self.lives}\n 
ENEMY lives - {enemy_obj.lives}\n
Your Attack NOW""")
        enemy_atack = enemy_obj.select_attack()
        print(enemy_atack)
        self.allowed_atacks = valid_input_value()
        result = self.fight(self.allowed_atacks, enemy_atack)
        if result == 0:
            print("it's Draw\n____________________________")
        elif result == 1:
            print("You attacked successfully!\n____________________________")
            self.score += 1*self.hard
            enemy_obj.decrease_lives()
        elif result == -1:
            print("You missed!\n____________________________")
        print("Your score:", self.score)
