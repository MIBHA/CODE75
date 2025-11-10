try:
    file = open("file.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("An error occurred:", e)
finally:
    if file is not None:
        file.close()
        print("File closed")
