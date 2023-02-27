print("----------------------Welcome User----------------------\n\n")

# this function is used for apperance in the program
def linebreak():
    print("---------------------------------------------------------")

# Menu for user to choose what they would like to do
# this functuon gives the user a choice from the menu above if they want to log in it will break out of
# the loop and go onto the next block of code below

def menu():
    while True:
        print("-----------------------Main Menu------------------------\n")
        print("To login enter 1:")
        print("To end the program enter 2:")
        print("")
        try:
            sUserSelection = int(input("What would you like to do? \n"))
        # make a conditional statement to see if the user wants to start the login program or exit
            if sUserSelection == 1:
                break
            elif sUserSelection == 2:
                print("Ending program, Goodbye!")
                break
        except:
            print("ERROR! Invalid choice please choose from the menu to continue or exit the program.\n")
            menu()

menu()

# This is a function that will return two print statements one to tell the user that their login was successful
# And it will then print greet with that users inputted name
def welcome_user():
    print("Login successful. ")
    print("Welcome ")

# Create a function for the admin login
sAdmin = "admin"
sAdminPassWord = "aDmin002"

def admin_login():
    print("Please login to the administrator account to create your new personal account: \n")
    while True:
        sUserInput = input("Please enter admin username: \n")
        sUserInput = sUserInput.lower()
        if sUserInput == sAdmin:
            break
        else:
            print("Wrong username please try again! \n")

    while True:
        sPassInput = input("Please enter admin password: \n")
        if sPassInput == sAdminPassWord:
            print("Login Successful")
            break
        else:
            print("Wrong password please try again! \n")

# this function allows the user to create a new account starting with the username and then
# it asks for the creation of a password
def new_account():
    print("\nPlease create a new account.\n")
    while True:
        global sNewUser1
        sNewUser1 = input("\nPlease enter a new username.\n"
                           "It should be at least 5 characters long\n"
                           "and not contain spaces or special characters: \n\n")

        if len(sNewUser1) < 5:
            print("Your username is too short. Please try again: ")
        elif sNewUser1.count(" ") > 0:
            print("Your username contains spaces. Please try again: ")
        elif sNewUser1.isalnum() is False:
            print("Your username contains a special character. "
                  "Please try again: ")
        else:
            # call another function
            break

    while True:
        global sNewPass1
        sNewPass1 = input("\n\nPlease enter a new password.\n"
                           "It should be at least 6 characters long\n"
                           "with at least one uppercase letter,\n"
                           "one lowercase letter, one special character"
                          "and one number: \n\n")

        if len(sNewPass1) < 6:
            print("\nYour password is too short. Please try again: ")
        elif any(lower.islower() for lower in sNewPass1) is False:
            print("\nYour password does not contain lowercase letters. "
                  "Please try again: ")
        elif any(upper.isupper() for upper in sNewPass1) is False:
            print("\nYour password does not contain uppercase letters. "
                  "Please try again: ")
        elif any(digit.isdigit() for digit in sNewPass1) is False:
            print("\nYour password does not contain a number. "
                  "Please try again: ")
        elif any(not char.isalnum() for char in sNewPass1) is False:
            print("\nYour password does not contain a special character. "
                  "Please try again: ")
        elif sNewPass1.replace(" ", "") != sNewPass1:
            print("\nYour password contains whitespaces. "
                  "Please try again: ")
        else:
            # call another function
            break

def name_selection():
    print("Account created sucessfully!")
    global sName1
    sName1 = input("Please enter your name:\n")

def user_login():
    while True:
        sUserLogin = input("Please enter your username:\n")
        if sUserLogin == sNewUser1:
            break
        else:
            print("Wrong username please try again:\n")
    while True:
        sUserPass = input("Please enter your password:\n")
        if sUserPass == sNewPass1:
            print("\nWelcome: ", sName1)
            break


# # calls the menu function
menu()

# # calls the admin login function
admin_login()

# calls the function to create a new account
new_account()

# calls the name creation function after an account has been made
name_selection()

# calls the function to allow the user to login using there credentials
user_login()


print('Updated to GitHub')

print('Test commit')