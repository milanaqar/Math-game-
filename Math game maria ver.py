import random
import time

print("=====Ας παίξουμε ... Μαθηματικά!=====")


# Instruction
def show_instructions():
    print("\n--------- Οδηγίες ---------\n")
    print("1. Επιλέγεις μαθηματική πράξη.")
    print("2. Το παιχνίδι έχει 3 επίπεδα:")
    print("   - Α: Εύκολο (1–10)")
    print("   - Β: Μέτριο (1–20)")
    print("   - Γ: Δύσκολο (1–20 + αντίστροφη μέτρηση)")
    print("3. Κάθε παιχνίδι έχει 10 γύρους.")
    print("4. Αν απαντήσεις σωστά, παίρνεις 1 βαθμό.")
    print("5. Στο τέλος εμφανίζεται η συνολική σου βαθμολογία.\n")

# Main menu
def arxiko_menu():
    while True:
         choice = input("*****Μαθηματικό παιχνίδι*****\n\n"
                     "1. Έναρξη παιχνιδιού\n"
                     "2. Οδηγίες\n"
                     "3. Έξοδος\n\n"
                     "📌 Επιλέξτε 1-3: ")
         
         if choice == '1':
              choose_operation()
         elif choice == '2':
              show_instructions()
         elif choice == '3':
              print("Θα τα ξαναπούμε!")
              break
         else:
             print("Άκυρη επιλογή. Παρακαλώ δοκίμασε ξανά (1-3).")
             print("-------------------------------")

# Timer for Г επιλογη          
def countdown(seconds):                                        #Συνάρτηση αντίστροφης μέτρησης
    while seconds > 0:
       print(f"Απομένουν: {seconds} δευτερόλεπτα", end="\r")
       time.sleep(1)
       seconds -= 1
       print("Τέλος χρόνου! Μπαμ! 💥")

# Difficultty levels
def choose_level():
    print("\n--- Επιλογή Επίπεδου ---")
    print("Α) Εύκολο")
    print("Β) Μέτριο")
    print("Γ) Δύσκολο")
    epipedo = input("\nΔιάλεξε επίπεδο (Α, Β, Γ): ").upper()
    return epipedo


# Questions 
def ask_question(num1, num2, praxi):             
    if praxi == "+":
        correct = num1 + num2

    elif praxi == "-":
        if num1 < num2:
            num1, num2 = num2, num1
        correct = num1 - num2

    elif praxi == "*":
        correct = num1 * num2

    answer = int(input(f"Γράψε πόσο κάνει {num1} {praxi} {num2}: "))
    return answer == correct, correct 


# Chooce operation, rounds questions, correct answer, score
def choose_operation():                                            # Maybe to make it different function or use something else for better stucture code 
    while True:
        score = 0
        print("\n--- Επιλογή Πράξης ---")
        print("1. Πρόσθεση (+)")
        print("2. Αφαίρεση (-)")
        print("3. Πολλαπλασιασμός (x)")
        print("4. Έξοδος")
    
        epilogi = input("\nΕπίλεξε πράξη (1-4): ")
    
        if epilogi == '1':
            praxi ="+"
        elif epilogi == "2":
            praxi = "-"
        elif epilogi == "3":
            praxi = "*"
        elif epilogi == "4":
             print("Έξοδος...")       # Doesnt exit, show main menu again, maybe because of while true
             break
        else:
            print("Άκυρη επιλογή. Παρακαλώ δοκίμασε ξανά (1-4).")
            continue

        epipedo = choose_level()
    
        for i in range(1,11):
            print(f"\nΓύρος {i}/10")
            
            if epipedo == "Α":
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
            elif epipedo == "Β":
                num1 = random.randint(1,20)
                num2 = random.randint(1,20)
            elif epipedo == "Γ":
                print("Έχεις 10 δευτερόλεπτα!")
                countdown(10)
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
            else:
                print("Άκυρη επιλογή επιπέδου!")
                break
        
            is_correct, correct = ask_question(num1, num2, praxi)
        
            if is_correct:
                print("✅ Σωστά! Κερδίζεις έναν βαθμό!")
                score += 1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {correct}")
        
                print(f"\n⭐ Η τελική σου βαθμολογία είναι: {score}/10\n")

               
print("\n-------------------------------------")
arxiko_menu()

