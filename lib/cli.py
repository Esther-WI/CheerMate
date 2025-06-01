from helpers import (
    welcome_user,
    log_mood,
    suggest_activity,
    show_mood_history,
    menu
)

if __name__ == "__main__":
    user = welcome_user()
    
    while True:
        choice = menu()
        
        if choice == '1':
            log_mood(user)
        elif choice == '2':
            suggest_activity(user)
        elif choice == '3':
            show_mood_history(user)
        elif choice == '4':
            print("Thank you for using CheerMate! Goodbye! Stay cheerful!")
            break
        else:
            print("Invalid choice. Please try again.")
    