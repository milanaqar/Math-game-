import random
import time

print("=====Ας παίξουμε ... Μαθηματικά!=====")

def arxiko_menu():
    while True:
         choice = input("*****Μαθηματικό παιχνίδι*****\n\n"
                     "1. Έναρξη παιχνιδιού\n"
                     "2. Οδηγίες\n"
                     "3. Έξοδος\n\n"
                     "📌 Επιλέξτε 1-3: ")
         
         if choice == '1':
              play_game()
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

# Επιλογή 1: Παιχνίδι (Ορισμός συνάρτησης)
def play_game():
    score = 0
    print("1. Πρόσθεση (+)")
    print("2. Αφαίρεση (-)")
    print("3. Πολλαπλασιασμός (x)")
    print("4. Έξοδος")
    
    epilogi = input("\nΕπίλεξε πράξη (1-4): ")
    

    def ask_question(num1, num2, praxi):             # Συνάρτηση πράξεων για αποφυγή επαναλήψεων
        if prαxi == "+":
            correct = num1 + num2
        elif praxi == "-":
            if num1 < num2:
            num1, num2 = num2, num1
            correct = num1 - num2
        elif praxi == "*":
            correct= num1*num2    
        answer = int(input(f"Γράψε πόσο κάνει {num1} {praxi} {num2}: "))
        return answer == correct, correct
            if answer==correct:
                 print("✅ Σωστά! Κερδίζεις έναν βαθμό!")
                 score +=1
            else:
                    print(f"❌ Λάθος! Η σωστή απάντηση είναι:{num1} {praxi} {num2} = {correct}")

while True:
    if epilogi == "1":
        print("\n--- Ας προσθέσουμε! ---")

        print("Α) Επίπεδο: Εύκολο")
        print("Β) Επίπεδο: Μέτριο")
        print("Γ) Επίπεδο: Δύσκολο")
        epipedo = input("\nΔιάλεξε επίπεδο (Α, Β, Γ): ").upper()          # .upper() για να δέχεται και μικρά

       
                      
        for i in range(1, 11):
             if epipedo == "Α":
                num1 = random.randint(1, 10)                                               # Why 1-10 and 1-20? 
                                                                                        # 1-20 είναι δυσκολότερο
                num2 = random.randint(1, 10)
             elif epipedo=="Β":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
             elif epipedo== "Γ":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
            else:
                print("Άκυρη επιλογή!")
            break
             for i in range(1, 11):
                if epipedo == "Α":
                    num1, num2 = random.randint(1, 10), random.randint(1, 10)
                elif epipedo == "Β":
                    num1, num2 = random.randint(1, 20), random.randint(1, 20)
                elif epipedo == "Γ":
                    num1, num2 = random.randint(1, 20), random.randint(1, 20)

                           

            if epipedo == "Γ":
                 print(f"Γύρος: {i}/10 — Έχεις 60 δευτερόλεπτα!")
                 countdown(60)
                 answer = int(input(f"Γράψε πόσο κάνει {num1} + {num2}: "))
                 
                if answer==athroisma:
                     print("✅ Σωστά! Κερδίζεις έναν βαθμό!")
                     score +=1
                else:
                    print(f"❌ Λάθος! Η σωστή απάντηση είναι:{num1} + {num2} = {athroisma}")

    elif epilogi == "2":
        print("\n--- Ας αφαιρέσουμε! ---")
        epipedo=input("\nΔιάλεξε επίπεδο: \n")
        print("Α) Επίπεδο: Εύκολο\n")
        print("Β) Επίπεδο: Μέτριο\n")
        print("Γ) Επίπεδο: Δύσκολο\n")
        epipedo = input("\nΔιάλεξε επίπεδο (Α, Β, Γ): \n").upper()

        for i in range(1, 11):
            if epipedo == "Α":
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
            else:
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)

        if epipedo == "Α":
            if num1 < num2:
                num1, num2 = num2, num1                     # Αποφυγή αρνητικών αριθμών
            diafora = num1 - num2
            answer = int(input(f"Γράψε πόσο κάνει {num1} - {num2}: "))
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} - {num2}: \n"))
            if answer==diafora:
                 print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                 score +=1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} - {num2} = {diafora}")

        if epipedo == "Β":
            if num1>num2:
                diafora = num1 - num2
            else:
                diafora = num2 - num1
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} - {num2}: \n"))
            if answer==diafora:
                 print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                 score +=1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} - {num2} = {diafora}")

        if epipedo == "Γ":
            if num1>num2:
                diafora = num1 - num2
            else:
                diafora = num2 - num1
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} + {num2}: \n"))
            countdown(60):
                 
 
        if answer==diafora:
                 print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                 score +=1
        else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} - {num2} = {diafora}")

    elif epilogi == "3":
        print("\n--- Ας πολλαπλασιάσουμε! ---")
        epipedo=input("\nΔιάλεξε επίπεδο: \n")
        print("Α) Επίπεδο: Εύκολο\n")
        print("Β) Επίπεδο: Μέτριο\n")
        print("Γ) Επίπεδο: Δύσκολο\n")
        epipedo = input("\nΔιάλεξε επίπεδο (Α, Β, Γ): \n").upper()
        for i in range(1, 11):
            if epipedo == "Α":
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
            else:
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)

        if epipedo == "Α":
            ginomeno = num1 * num2
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} * {num2}: \n"))
            if answer==ginomeno:
                 print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                 score +=1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} * {num2} = {ginomeno}")

        if epipedo == "Β":
            ginomeno = num1 * num2
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} * {num2}: \n"))
            if answer==ginomeno:
                 print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                 score +=1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} * {num2} = {ginomeno}")       


        if epipedo == "Γ":
            countdown (60)
            ginomeno = num1 * num2
            print(f"Γύρος: {i}/10")
            answer = int(input(f"Γράψε πόσο κάνει {num1} * {num2}: \n"))
            if answer==ginomeno:
                print("✅ Σωστά!Κερδίζεις έναν βαθμό!")
                score +=1
            else:
                print(f"❌ Λάθος! Η σωστή απάντηση είναι: {num1} * {num2}= {ginomeno}")


    if epilogi == "4":
        print("Ευχαριστώ που παίξαμε! Τα ξαναλέμε!")    # Σταματάει το loop και κλείνει το πρόγραμμα  check                                            
    elif epilogi not in ["1","2","3","4"]:
        print("Χμμ, δεν κατάλαβα... Διάλεξε 1, 2, 3 ή 4")
               




print("\n-------------------------------------")
           

   if epilogi in ["1", "2", "3"]:
    print(f"\n⭐ Η τελική σου βαθμολογία είναι: {score}/10")

    
        
#Επιλογή 2: Οδηγίες
#Ορισμός συνάρτησης
def show_instructions():
    print("\n")
    print("--------- Οδηγίες ---------\n")
    print("1. Ο παίκτης/η παίκτρια επιλέγει μαθηματική πράξη.\n"
          "2. Το παιχνίδι έχει 3 επίπεδα: Στο εύκολο δίνονται αριθμοί από το 0-10, στο μέτριο επίπεδο από το 0-20, ενώ στο δύσκολο υπάρχει και αντίστροφη μέτρηση\n."
          "3. Το παιχνίδι έχει 10 γύρους.\n" 
          "4. Σε κάθε γύρο οι αριθμοί εμφανίζονται τυχαία\n" 
          "5. Αν απαντήσεις σωστά, παίρνεις 1 βαθμό.\n" 
          "6. Στο τέλος εμφανίζεται η συνολική σου βαθμολογία.")

arxiko_menu()




            
    
        
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
          "6. Στο τέλος εμφανίζεται η συνολική σου βαθμολογία.")

arxiko_menu()

