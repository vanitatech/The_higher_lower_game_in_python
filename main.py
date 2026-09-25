# Display art
from art import logo
from art import vs
from game_data import data
import random

def format_data():
    # Clear the screen
    print("\n" * 20)
    """Takes account data and returns printable format."""
    print(logo)
    print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]}")
    print(vs)
    print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]}")

def check_answer(user_input, check_A, check_B):
    """Takes a user's guess and the follower's counts and returns if they got it right or not"""
    if check_A > check_B:
        return user_input == "A"
    else:
        return user_input == "B"

score = 0
should_continue = True



while should_continue:
    """Choose two string randomly from the list"""
    A, B = random.sample(data,2)
    format_data()
    
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    check_A = A["follower_count"]
    check_B = B["follower_count"]
    
    is_correct = check_answer(user_input, check_A, check_B)
    if is_correct:
        score += 1
        print(f"You\'re right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False
