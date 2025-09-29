import random
import os

# File to store player progress
PROGRESS_FILE = "player_progress.txt"

# Questions for each level
QUESTIONS = {
    "Easy": [
        ("What is the capital of France?", "Paris"),
        ("2 + 2 equals?", "4"),
        ("Color of the sky on a clear day?", "Blue")
    ],
    "Medium": [
        ("What is the square root of 64?", "8"),
        ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
        ("Which planet is known as the Red Planet?", "Mars")
    ],
    "Hard": [
        ("What year did World War II end?", "1945"),
        ("What is the derivative of x^2?", "2x"),
        ("Who proposed the theory of relativity?", "Einstein")
    ]
}

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {"name": "", "level": "Easy", "score": 0}
    with open(PROGRESS_FILE, 'r') as file:
        lines = file.readlines()
        return {
            "name": lines[0].strip(),
            "level": lines[1].strip(),
            "score": int(lines[2].strip())
        }

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as file:
        file.write(f"{progress['name']}\n")
        file.write(f"{progress['level']}\n")
        file.write(f"{progress['score']}\n")

def ask_questions(level, num_questions=3):
    questions = random.sample(QUESTIONS[level], num_questions)
    score = 0
    for q, a in questions:
        print(f"\n{q}")
        user_ans = input("Your answer: ").strip()
        if user_ans.lower() == a.lower():
            print("Correct!")
            score += 5
        else:
            print(f"Wrong! The correct answer was: {a}")
    return score

def get_next_level(current_level):
    levels = list(QUESTIONS.keys())
    idx = levels.index(current_level)
    return levels[idx + 1] if idx + 1 < len(levels) else None

def main():
    print("=== Welcome to the Quiz Game ===")
    progress = load_progress()
    if not progress["name"]:
        progress["name"] = input("Enter your name: ")
    print(f"\nHello, {progress['name']}! Your current level is {progress['level']} with a score of {progress['score']}.")

    while progress["level"]:
        print(f"\n--- Level: {progress['level']} ---")
        earned = ask_questions(progress["level"])
        progress["score"] += earned
        print(f"\nYou earned {earned} points. Total score: {progress['score']}")
        save_progress(progress)

        next_level = get_next_level(progress["level"])
        if next_level:
            choice = input(f"Do you want to proceed to {next_level} level? (yes/no): ").strip().lower()
            if choice == 'yes':
                progress["level"] = next_level
            else:
                print("Exiting the game. Progress saved.")
                break
        else:
            print("Congratulations! You have completed all levels.")
            break

    print(f"\nThanks for playing, {progress['name']}! Final Score: {progress['score']}")
    save_progress(progress)

if __name__ == "__main__":
    main()
