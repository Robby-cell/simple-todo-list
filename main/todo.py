import sys
import datetime

def help():
    msg = """Usage :-
$ ./todo add "todo item"
$ ./todo ls               # Show remaining todos
$ ./todo delete NUMBER    # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo stats            # Statistics
$ ./todo log              # Shows the log of previous commands"""
    sys.stdout.buffer(msg.encode('utf8'))


def add(c):

    with open('todo.txt', 'a') as f:
        f.write(c)
        f.write('\n')

    c = '"'+c+'"'
    print(f"Added todo: {c}")


def ls():

    try:
        dict_util('todo.txt', 'd')
        l = len(d)

        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1

    except Exception as e:
        raise e


def done(nn):
    # adds the complete task to done.txt
    try:
        dict_util('todo.txt', 'd')
        nn = int(nn)
        f = open('done.txt', 'a')
        dn = '/ '+str(datetime.datetime.today()).split()[0]+' '+d[nn] # adds date, and task completed to the string

        f.write(dn) # writes the content to the file
        f.write("\n")
        f.close()

        print(f'todo #{nn} marked as done.')

        with open('todo.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[nn]:
                    f.write(i)

            f.truncate()

    except:
        print(f'todo #{nn} does not exist')


def stats():
    dict_util('todo.txt', 'd')
    try:

        nf = open('done.txt', 'r')
        c = 1

        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c += 1

        print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')

    except:
        print(f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')


def delete(nn):

    try:
        nn = int(nn)
        dict_util('todo.txt', 'd')

        with open('todo.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[nn]:
                    f.write(i)

            f.truncate()
        print(f"deleted todo #{nn}")

    except Exception as e:
        print(f'error: todo #{nn} does not exist. nothing deleted')


def dict_util(filename, dict): # takes name of file to work with, and the dictionary to put it into

    # utility function
    try:
        f = open(filename, 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            globals()[dict].update({c: line})
            c += 1

    except:
        sys.stdout.buffer.write('there are no pending todos'.encode('utf8'))


def logthis(content=''):

    f = open('log.txt', 'a')
    lg = 'log: ' + str(datetime.datetime.today()).split()[0] + ' ' + args[1] + ' ' + content

    f.write(lg)
    f.write("\n")
    f.close()


def log():

    try:
        dict_util('log.txt', '_log')
        l = len(_log)

        for i in _log:
            sys.stdout.buffer.write(f"[{i}] {_log[i]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1

    except Exception as e:
        raise e




if __name__ == '__main__':

    try:
        d = {}
        _log = {}
        don = {}
        args = sys.argv

        if (args[1] == 'delete'):
            args[1] = 'delete'

        if (args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write('Error: missing todo string. nothing added'.encode('utf8'))

        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write('Error: missing number for marking todo as done.'.encode('utf8'))

        elif (args[1] == 'delete' and len(args[2:]) == 0):
            sys.stdout.buffer.write('Error: missing number for deleting todo.'.encode('utf8'))

        else:
            globals()[args[1]](*args[2:])

        
    except Exception as e:
        msg = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo delete NUMBER    # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo stats            # Statistics
$ ./todo log              # Shows the log of previous commands"""
        sys.stdout.buffer.write(msg.encode('utf8'))

    logthis(*args[2:])

        