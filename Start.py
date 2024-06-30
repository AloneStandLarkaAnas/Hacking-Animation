import os
import time
import pyfiglet

# Set the text color to green
os.system("tput setaf 2")

# Create a figlet object
f = pyfiglet.Figlet(font='slant')

# Print the title in figlet style
print(f.renderText("Alone Stand Larka"))

# Print the options
print("\nSelect an option:")
print("1. Tool1")
print("2. Tool2")
print("3. Tool3")
print("4. Tool4")
print("5. Tool5")
print("6. Tool6")
print("7. Tool7")
print("8. Tool8")
print("9. Tool9")
print("10. Exit")

while True:
    # Get the user's input
    option = input("\nEnter an option: ")

    # Handle the options
    if option == "1":
        os.system("pkg install libcaca")
        os.system("cacafire")
    elif option == "2":
        os.system("apt install sl")
        os.system("sl")
    elif option == "3":
        os.system("apt install cmatrix")
        os.system("cmatrix")
    elif option == "4":
        os.system("apt install 0verkill")
        os.system("0verkill")
    elif option == "5":
        os.system("apt install 1oom")
        os.system("1oom")
    elif option == "6":
        os.system("apt install 2048-c")
        os.system("2048-c")
    elif option == "7":
        os.system("apt install a52dec")
        os.system("a52dec")
    elif option == "8":
        os.system("apt install aalib")
        os.system("aalib")
    elif option == "9":
        os.system("pkg install hollywood")
        os.system("hollywood")
    elif option == "10":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again!")

    # Wait for 2 seconds before printing the options again
    time.sleep(2)
    os.system("clear")
    print(f.renderText("Alone Stand Larka"))
    print("\nSelect an option:")
    print("1. Cacafire")
    print("2. SL")
    print("3. CMatrix")
    print("4. 0verkill")
    print("5. 1oom")
    print("6. 2048-c")
    print("7. a52dec")
    print("8. aalib")
    print("9. Hollywood")
    print("10. Exit")