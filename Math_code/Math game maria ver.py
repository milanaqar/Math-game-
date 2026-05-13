import random
import time

print("=====Ας παίξουμε ... Μαθηματικά!=====")

#Επιλογή 2: Οδηγίες
#Ορισμός συνάρτησης
def show_instructions():
    print("\n")
    print("--------- Οδηγίες ---------\n")
    print("1. Ο παίκτης/η παίκτρια επιλέγει μαθηματική πράξη.\n"
          "2. Το παιχνίδι έχει 3 επίπεδα: Στο εύκολο δίνονται αριθμοί από το 0-10, στο μέτριο επίπεδο από το 0-20, ενώ στο δύσκολο υπάρχει και αντίστροφη μέτρηση.\n"
          "3. Το παιχνίδι έχει 10 γύρους.\n" 
          "4. Σε κάθε γύρο οι αριθμοί εμφανίζονται τυχαία.\n" 
          "5. Αν απαντήσεις σωστά, παίρνεις 1 βαθμό.\n" 
          "6. Στο τέλος εμφανίζεται η συνολική σου βαθμολογία.\n")

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
            
def countdown(seconds):                                        #Συνάρτηση αντίστροφης μέτρησης
                    while seconds > 0:
                        print(f"Απομένουν: {seconds} δευτερόλεπτα", end="\r")
                        time.sleep(1)
                        seconds -= 1
                    print("Τέλος χρόνου! Μπαμ! 💥")

# Επιλογή 1: Παιχνίδι Ορισμός συνάρτησης
def choose_operation():
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
        else:
             print("Έξοδος...")
             return 
    
        for i in range(1,11):
            print(f"\nΓύρος {i}/10")

            num1 = random.randint(1,20)
            num2 = random.randint(1,20)
        
            is_correct, correct = ask_question(num1, num2, praxi)
        
            if is_correct:
                print("✅ Σωστά! Κερδίζεις έναν βαθμό!")
                score += 1
    
            else:
                 print(f"❌ Λάθος! Η σωστή απάντηση είναι: {correct}")

def ask_question(num1, num2, praxi):             # Συνάρτηση πράξεων για αποφυγή επαναλήψεων
    if praxi == "+":
        epipedo = choose_level()
        first_choice(epilogi)

    elif praxi == "-":
        if num1 < num2:
            epipedo = choose_level()
            second_choice(epilogi)

    elif praxi == "*":
        epipedo = choose_level()
        third_choice(epilogi)

    answer = int(input(f"Γράψε πόσο κάνει {num1} {praxi} {num2}: "))
        
   

<<<<<<< HEAD:Math game maria ver.py


while True:
=======
def choose_level():
    print("\n--- Επιλογή Επίπεδου ---")
    print("Α) Επίπεδο: Εύκολο")
    print("Β) Επίπεδο: Μέτριο")
    print("Γ) Επίπεδο: Δύσκολο")
    epipedo = input("\nΔιάλεξε επίπεδο (Α, Β, Γ): ").upper()          # .upper() για να δέχεται και μικρά                 
    return epipedo



def first_choice(epilogi):
>>>>>>> c1f34d1a785d4fd47b88e2a983437053baf264c4:Math_code/Math game maria ver.py
    if epilogi == "1":
        print("\n--- Ας προσθέσουμε! ---")
        epipedo = choose_level()
        for i in range(1, 11):
             if epipedo == "Α":
                 num1, num2 = random.randint(1, 10), random.randint(1, 10)
                 print(f"Γύρος: {i}/1")
                 ask_question(num1, num2, "+")
             elif epipedo == "Β":
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                print(f"Γύρος: {i}/1")
                ask_question(num1, num2, "+")
             elif epipedo == "Γ":
                countdown (60)
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                print(f"Γύρος: {i}/10 — Έχεις 60 δευτερόλεπτα!")
                ask_question(num1, num2, "+")
             else:
                print("Άκυρη επιλογή!")
                break
   
                           

            
def second_choice(epilogi):
    if epilogi == "2":
        print("\n--- Ας αφαιρέσουμε! ---")
        epipedo = choose_level()
        if num1 < num2:
                num1, num2 = num2, num1
        for i in range(1, 11):
             if epipedo == "Α":
                 num1, num2 = random.randint(1, 10), random.randint(1, 10)
                 print(f"Γύρος: {i}/1")
                 ask_question(num1, num2,"-")
             elif epipedo == "Β":
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                print(f"Γύρος: {i}/1")
                ask_question(num1, num2, "-")
             elif epipedo == "Γ":
                countdown (60)
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                print(f"Γύρος: {i}/10 — Έχεις 60 δευτερόλεπτα!")
                ask_question(num1, num2, "-")
             else:
                print("Άκυρη επιλογή!")
<<<<<<< HEAD:Math game maria ver.py
            break
        
   
=======
                break    

>>>>>>> c1f34d1a785d4fd47b88e2a983437053baf264c4:Math_code/Math game maria ver.py


def third_choice(epilogi):
    if epilogi == "3":
        print("\n--- Ας πολλαπλασιάσουμε! ---")
        epipedo = choose_level()
        for i in range(1, 11):
            if epipedo == "Α":
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                ask_question (num1, num2, "*")
            elif epipedo=="Β":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                ask_question (num1, num2, "*")
            elif epipedo == "Γ":
                countdown (60)
                num1, num2 = random.randint(1, 20), random.randint(1, 20)
                print(f"Γύρος: {i}/10 — Έχεις 60 δευτερόλεπτα!")
                ask_question(num1, num2, "*")
            else:
                print("Άκυρη επιλογή!")
                break
    if epilogi in ["1", "2", "3"]:
        print(f"\n⭐ Η τελική σου βαθμολογία είναι: {score}/10")
      
    elif epilogi == "4":
        print("Ευχαριστώ που παίξαμε! Τα ξαναλέμε!")    # Σταματάει το loop και κλείνει το πρόγραμμα  check                                            
    elif epilogi not in ["1","2","3","4"]:
        print("Χμμ, δεν κατάλαβα... Διάλεξε 1, 2, 3 ή 4")


               
print("\n-------------------------------------")
<<<<<<< HEAD:Math game maria ver.py
           

   if epilogi in ["1", "2", "3"]:
    print(f"\n⭐ Η τελική σου βαθμολογία είναι: {score}/10")

    
        
arxiko_menu()
    
#Επιλογή 2: Οδηγίες
#Ορισμός συνάρτησης
def show_instructions():                                                          # need to call it and place it 
    print("\n")
    print("--------- Οδηγίες ---------\n")
    print("1. Ο παίκτης/η παίκτρια επιλέγει μαθηματική πράξη.\n"
          "2. Το παιχνίδι έχει 3 επίπεδα: Στο εύκολο δίνονται αριθμοί από το 0-10, στο μέτριο επίπεδο από το 0-20, ενώ στο δύσκολο υπάρχει και αντίστροφη μέτρηση.\n"
          "3. Το παιχνίδι έχει 10 γύρους.\n" 
          "4. Σε κάθε γύρο οι αριθμοί εμφανίζονται τυχαία.\n" 
          "5. Αν απαντήσεις σωστά, παίρνεις 1 βαθμό.\n" 
          "6. Στο τέλος εμφανίζεται η συνολική σου βαθμολογία.")

=======
>>>>>>> c1f34d1a785d4fd47b88e2a983437053baf264c4:Math_code/Math game maria ver.py
arxiko_menu()

