import random

# -----------------------------
# 1. MENU
# -----------------------------
@app.route("/")
def main_menu():
    return render_template("index.html")

# -----------------------------
# 2. DIFFICULTY SELECTION
# -----------------------------
@app.route("/choose_difficulty")
def choose_difficulty():
    return render_template("choose_difficulty.html")

# -----------------------------
# 3. QUESTION GENERATOR
# -----------------------------
def generate_question(difficulty):
    if difficulty == "easy":  # Easy – Naxos
        operations = ['+', '-']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

    elif difficulty == "medium":  # Medium – Crete
        operations = ['+', '-', '*']
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

    else:  # Hard – Olympus
        operations = ['+', '-', '*', '/']
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    
    if num2 == 0:
        num2 = 1 

        operation = random.choice(operations)

        # Avoid division by zero
        if '/' in operations and num2 == 0:
            num2 = random.randint(1, 50)

    operation = random.choice(operations)

    # Division: force clean integer results
    if operation == '/':
        num1 = num1 * num2  # ensures num1 / num2 is integer

    correct = eval(f"{num1} {operation} {num2}")

    return num1, num2, operation, correct


# -----------------------------
# 4. GAME LOGIC
# -----------------------------

    @app.route ("/battle/<difficulty>")
    def start_battle(difficulty):
        session["difficulty"] = difficulty
        session["round"] = 1
        session ["score"] = 0
num1, num2, operation = generate_question(difficulty)
session["correct"] = correct

return render_template(
    "battle.html"
    round=seesion["round"],
    num1=num1,
    num2=num2,
    operation=op
)

@app.route("/answer", methods=["POST"])
def answer():
        user_answer = int (request.form["answer"])

        if user_answer == session["correct"]:
            session["score"] += 1

        session["round"] += 1

        if session ["round"] > 10:
            return redirect(url_for("result"))
        
        num1, num2, op, correct = generate_question(session["difficulty"])
        session ["correct"] = correct

        return render_template(
            "battle.html",
            round=session["round"],
            num1=num1,
            num2=num2,
            operation=op
        )

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
