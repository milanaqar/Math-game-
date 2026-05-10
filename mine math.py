import random

# -----------------------------
# 1. MENU
# -----------------------------
def main_menu():
    choice = input(
        "--------- Math Odyssey ---------\n\n"
        "1. Έναρξη παιχνιδιού\n"
        "2. Οδηγίες\n"
        "3. Έξοδος\n\n"
        "📌 Επιλέξτε 1-3: "
    )
    return choice


# -----------------------------
# 2. DIFFICULTY SELECTION
# -----------------------------
def choose_difficulty():
    print("\n🌍 Επίλεξε νησί (δυσκολία):\n")
    print("1. Νάξος (Εύκολο)")
    print("2. Κρήτη (Μεσαίο)")
    print("3. Όλυμπος (Δύσκολο)\n")

    while True:
        diff = input("📌 Επιλογή 1-3: ")
        if diff in ["1", "2", "3"]:
            return diff
        print("Άκυρη επιλογή. Προσπάθησε ξανά.")


# -----------------------------
# 3. QUESTION GENERATOR
# -----------------------------
def generate_question(difficulty):
    if difficulty == "1":  # Easy – Naxos
        operations = ['+', '-']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

    elif difficulty == "2":  # Medium – Crete
        operations = ['+', '-', '*']
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

    else:  # Hard – Olympus
        operations = ['+', '-', '*', '/']
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)

        # Avoid division by zero
        if '/' in operations and num2 == 0:
            num2 = random.randint(1, 50)

    operation = random.choice(operations)

    # Division: force clean integer results
    if operation == '/':
        num1 = num1 * num2  # ensures num1 / num2 is integer

    return num1, num2, operation


# -----------------------------
# 4. GAME LOGIC
# -----------------------------
def play_game():
    difficulty = choose_difficulty()
    score = 0

    island_names = {"1": "Νάξος", "2": "Κρήτη", "3": "Όλυμπος"}
    print(f"\n🏝️ Ξεκινάς το ταξίδι σου στη {island_names[difficulty]}!\n")

    for i in range(1, 11):
        num1, num2, operation = generate_question(difficulty)

        print("\n-------------------------------------")
        print(f"Γύρος: {i}/10")

        answer = int(input(f"Πόσο κάνει {num1} {operation} {num2} : "))

        # Correct answer
        if operation == '+':
            correct = num1 + num2
        elif operation == '-':
            correct = num1 - num2
        elif operation == '*':
            correct = num1 * num2
        elif operation == '/':
            correct = num1 // num2

        # Check
        if answer == correct:
            print("✅ Σωστά!")
            score += 1
        else:
            print(f"❌ Λάθος! Η σωστή απάντηση είναι {correct}.")

    print("\n-------------------------------------")
    print(f"⭐ Το τελικό σου σκορ είναι: {score}/10")


# -----------------------------
# 5. INSTRUCTIONS
# -----------------------------
def show_instructions():
    print("\n--------- Οδηγίες ---------\n")
    print("1️⃣  Το παιχνίδι έχει 10 γύρους.")
    print("2️⃣  Σε κάθε γύρο εμφανίζεται μία μαθηματική πράξη.")
    print("3️⃣  Αν απαντήσεις σωστά, παίρνεις 1 πόντο.")
    print("4️⃣  Στο τέλος εμφανίζεται το συνολικό σου σκορ.")
    print("5️⃣  Διάλεξε νησί (δυσκολία): Νάξος, Κρήτη ή Όλυμπος.\n")


# -----------------------------
# 6. MAIN LOOP
# -----------------------------
while True:
    choice = main_menu()

    if choice == '1':
        play_game()
    elif choice == '2':
        show_instructions()
    elif choice == '3':
        print("Ευχαριστούμε που παίξατε!")
        break
    else:
        print("Άκυρη επιλογή. Παρακαλώ δοκιμάστε ξανά.")
