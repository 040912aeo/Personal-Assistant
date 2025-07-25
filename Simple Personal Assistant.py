#!/usr/bin/env python3
import random
import os

def ask_questions():
    # Define your questions and the keys to store them in a dict
    questions = [
        ("name",        "What is your name? "),
        ("age",         "How old are you? "),
        ("color",       "What is your favorite color? "),
        ("food",        "What is your favorite food? "),
        ("city",        "Which city do you live in? "),
        ("shs",         "Which SHS did you attend? "),
        ("soccer_team", "What’s your favorite soccer team? ")
    ]
    # Shuffle so each run has a fresh order
    random.shuffle(questions)

    answers = {}
    for key, prompt in questions:
        ans = input(prompt).strip()
        while not ans:
            ans = input(f"Please enter a value for {key}: ").strip()
        answers[key] = ans
    return answers

def build_summary(data):
    return (
        f"\nHello, {data['name']}!\n"
        f"You are {data['age']} years old, love the color {data['color']}, "
        f"and enjoy eating {data['food']}.\n"
        f"Life must be awesome in {data['city']}!\n"
        f"I hear you went to {data['shs']} and cheer for {data['soccer_team']}.\n"
    )

def get_rating():
    while True:
        try:
            rating = int(input("On a scale of 1–5 stars, how would you rate this assistant? "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("That doesn’t look like a number. Try again.")

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
        f.write(f"\nAssistant Rating: {rating} ⭐\n")
    print(f"Saved to {filename}\n")

def main():
    print("👋 Welcome! Let’s get to know you.\n")
    while True:
        # 1) Gather user data
        user_data = ask_questions()

        # 2) Build and display summary
        summary = build_summary(user_data)
        print(summary)

        # 3) Ask for rating
        rating = get_rating()
        print(f"Thanks for the {rating}-star rating!\n")

        # 4) Offer file save
        save_choice = input("Would you like to save this summary to a file? (y/n) ").lower()
        if save_choice in ("y", "yes"):
            save_to_file(user_data["name"], summary, rating)

        # 5) Offer restart
        again = input("Do you want to start over? (y/n) ").lower()
        if again not in ("y", "yes"):
            print("\nGoodbye! Have an awesome day 🌟")
            break
        print("\n--- Restarting... ---\n")

if __name__ == "__main__":
    main()