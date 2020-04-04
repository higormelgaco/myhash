#!python3
from myHash.myHash import myHash

myhash = myHash()
user_feedback = ''

def main():
    try:
        myhash.whatYouWant()
        user_feedback = str(input('Deseja realizar outra conversão?[Y/N]\n\t>>'))

        if user_feedback.upper() == 'Y':
            main()
        elif user_feedback.upper() == 'N':
            return
        else:
            return 'Comando não reconhecido'

    except Exception as error:
        print(error)

main()