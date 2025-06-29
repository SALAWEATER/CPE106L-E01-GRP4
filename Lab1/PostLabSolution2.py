filename = input("Enter the path to the file: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
        while True:
            choice = int(input("Enter the line number to print (0 to exit): "))
            if choice == 0:
                print("Exiting program.")
                break
            elif 1 <= choice <= len(lines):
                print(f"Line {choice}: {lines[choice - 1].rstrip()}")
            else:
                print("Invalid line number.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
