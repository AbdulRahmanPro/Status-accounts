from Functions.Bot import AmzoneBot
from Functions.protection import Protection
def main():
    while True:
        print("Main Menu:")
        print("1. Start")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            pathprofile = input("Enter the path to your profile: ")
            handles = input("Do you want it hidden or visible: yes or no : ")
            if handles == "yes":
                bot = AmzoneBot(pathprofile,"--headless")
                bot.start()
            elif handles == "no":
                bot = AmzoneBot(pathprofile,"none")
                bot.start()
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Protection().check_board_number()
    main()
