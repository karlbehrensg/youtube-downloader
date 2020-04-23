
menuStr = """
[1]Search video with url
[0]Exit
"""

def run():
    while True:
        command = input(menuStr)
        try:
            command = int(command)
            if command == 1:
                print('Search URL')
            elif command == 0:
                print('Exit')
                break
            else:
                print('Invalid command')
        except:
            print('Input need to be a number')


if __name__ == "__main__":
    run()