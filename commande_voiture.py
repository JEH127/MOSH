command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print(' start - to start the car\n')
        print(' stop - to stop the car\n')
        print(' quit - to exit')

    elif command == 'start':
        if started == False:  # <=> car stopped
            print(' Car started - ready to go ')
            started = True  # <=> car started

        elif started == True:
            print(' The car is already started ! ')

    elif command == 'stop':
        if started == True:
            print(' Car stopped')
            started = False

        elif started == False:
            print(' Car is already stopped ! ')

    elif command == 'quit':
        break

    else:
        print(" I don't understand that...")
