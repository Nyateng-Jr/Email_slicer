# collect email from user, if the user enters "quit" the program exits
# split email using the @, save the first part as the username, the second part will be saved as domain
# split domain using "."

def main():
    print("Welcome to the email slicer")
    print("")
    while True:
        email_input = input("Enter your email address: ")
        if email_input == "quit":
            print("Exiting the program...")
            break
        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")
        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension)


main()


