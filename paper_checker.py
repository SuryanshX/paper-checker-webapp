import os

def save_result(path, correct, wrong, not_attempted):
    score1 = (correct * 2) - (wrong * 0.5)
    score2 = (correct * 1) - (wrong * 0.25)
    result_text = f"""✅ Result:
Correct Answers: {correct}
Wrong Answers: {wrong}
Not Attempted: {not_attempted}

System 1 (SSC: +2, -0.5) → Final Score = {score1}
System 2 (+1, -0.25) → Final Score = {score2}
"""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(result_text)
    except Exception as e:
        print(f"⚠️ Could not save result: {e}")
    return result_text

def paper_checker():
    print("👉 Instructions:")
    print("Press 'c' for Correct, 'w' for Wrong, 'n' for Not Attempted")
    print("Press 'q' to finish and see result\n")

    correct = 0
    wrong = 0
    not_attempted = 0

    # File will be saved in the current working directory (see steps below)
    result_path = os.path.join(os.getcwd(), "result.txt")
    print(f"📂 Results will be saved to: {result_path}\n")

    while True:
        key = input("Enter (c/w/n/q): ").strip().lower()

        if key == 'c':
            correct += 1
        elif key == 'w':
            wrong += 1
        elif key == 'n':
            not_attempted += 1
        elif key == 'q':
            break
        else:
            print("❌ Invalid input, try again.")
            continue

        # autosave after every entry (so progress never lost)
        save_result(result_path, correct, wrong, not_attempted)

    # final save & print
    final_text = save_result(result_path, correct, wrong, not_attempted)
    print("\n" + final_text)
    print(f"✅ Final result saved to: {result_path}\n")


if __name__ == "__main__":
    paper_checker()

