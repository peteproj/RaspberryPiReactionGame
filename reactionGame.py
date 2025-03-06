from gpiozero import LED, Button
from time import sleep
import random

led = LED(4)
right_button = Button(12, bounce_time=0.1)
left_button = Button(18, bounce_time=0.1)

def get_player_names():
    left_name = input("Enter Green's name: ")
    right_name = input("Enter Reds's name: ")
    return left_name, right_name

def play_round(left_name, right_name, left_score, right_score):
    print("\nWait for the light!")
    delay = random.randint(2, 8)
    sleep(delay)

    led.on()
    print("GO!")

    winner = None
    while winner is None:
        if left_button.is_pressed:
            winner = left_name
            left_score += 1
        elif right_button.is_pressed:
            winner = right_name
            right_score += 1

    led.off()
    sleep(0.1)

    print(f"{winner} Wins the Round!")
    print(f"Score: {left_name} - {left_score}, {right_name} - {right_score}")

    return left_score, right_score

def reaction_game():
    left_name, right_name = get_player_names()
    left_score, right_score = 0, 0
    winning_score = 3

    while left_score < winning_score and right_score < winning_score:
        left_score, right_score = play_round(left_name, right_name, left_score, right_score)

    if left_score > right_score:
        print(f"\n{left_name} wins the game!")
    else:
        print(f"\n{right_name} wins the game!")

reaction_game()