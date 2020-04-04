import hashlib

class myHash:

    def __init__(self):
        return

    def whatYouWant(self):
        try:
            user_hash = int(input('Digite o número do algoritmo que deseja:\n[0] - md5\n[1] - sha1\n[2] - sha224\n[3] - sha256\n[4] - sha384\n[5] - sha512\n\t>> '))
            if user_hash > 5:
                print('Valor desconhecido')
                return
        except Exception :
            print('Valor desconhecido')
            return

        user_input = str(input('Digite o que deseja converter: \n\t>> '))
        value_returned = myHash.chooseHash(user_hash,user_input)
        print('\t>> ',value_returned)

    def chooseHash(user_alg, user_value):
        user_value = user_value.encode('utf8')
        if user_alg == 0:
            value = hashlib.md5(user_value)
        elif user_alg == 1:
            value = hashlib.sha1(user_value)
        elif user_alg == 2:
            value = hashlib.sha224(user_value)
        elif user_alg == 3:
            value = hashlib.sha256(user_value)
        elif user_alg == 4:
            value = hashlib.sha384(user_value)
        elif user_alg == 5:
            value = hashlib.sha512(user_value)

        return value.hexdigest()
