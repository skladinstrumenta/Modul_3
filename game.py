"""
    The main file that runs for the game

"""

from datetime import datetime
from game_exceptions import EnemyDown, ExitGame, GameOver
from models import Enemy, Player, PlayerHard
from settings import HARD, validator_input, validator_mode


def play():
    """in this function all given calculations for the game are calculated

    Returns:
        str: Player-name, Player-score, date and time, play-mode
    """
    name = input("Enter your name: ")

    try:
        validator_input(name)
    except ExitGame:
        print("You're exit from Game!")
        return 0
    mode = validator_mode()
    if mode == "N":
        player = Player(name)
        level = 1
        enemy_obj = Enemy(level)
    elif mode == "H":
        player = PlayerHard(name, HARD)
        level = 1*HARD
        enemy_obj = Enemy(level)
    while player.lives:
        try:
            player.attack(enemy_obj)
        except EnemyDown:
            level += 1
            if mode == "N":
                print(f"Congratulations, you defeated your opponent, \
and you get +5 points for winning.\n\
You have moved to a new level! LEVEL - {level}")
                player.score += 5
                print(f"YOUR SCORE - {player.score}")
                enemy_obj = Enemy(level)
                continue
            elif mode == "H":
                print(f"Congratulations, you defeated your opponent, \
and you get +{5*HARD} points for winning.\n\
You have moved to a new level! LEVEL - {level}")
                player.score += 5*HARD
                print(f"YOUR SCORE - {player.score}")
                enemy_obj = Enemy(level)
                continue
        try:
            player.defence(enemy_obj)
        except GameOver:
            def save_top():
                """This function save the top 10 scores

                Returns:
                    str: list-strings of scores
                """
                with open("scores.txt", "a+", encoding="utf-8")as apend:
                    apend.write(
                        f"{player.name.upper()} : {player.score} : {datetime.now()} : ({mode})\n")
                    apend.seek(0)
                    list = []
                    for line in apend:
                        list.append(line.split(": "))
                    def sortbyscore(stroka):
                        return stroka[1]
                    sortlist = sorted(list, key=sortbyscore, reverse=True)
                    sort_top = sortlist[0:10]
                    return "".join(": ".join(li) for li in sort_top)
            top = save_top()
            with open("scores.txt", "w", encoding="utf-8") as top_write:
                top_write.write(top)                
            print("GAME OVER")
    return player.score


if __name__ == "__main__":
    try:
        print(f"Your score - {play()}")
    except GameOver:
        print("GAME OVER")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")
