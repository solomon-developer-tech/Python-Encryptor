import random
import argparse

runs = 0

def main():
    parser = argparse.ArgumentParser(description="Encryption Options")
    parser.add_argument(
        '-e', '--encrypt',
        type=str,
        help="Specify the .txt file to encrypt."
    )
    parser.add_argument(
        '-d', '--decrypt',
        type=str,
        help="Specify the .txt file to decrypt."
    )
    args = parser.parse_args()

    sequence1 = {'l': 91, 'c': 103, 'b': 112, 's': 124, 'k': 125, 'h': 122, 'g': 98, 'n': 119, 'v': 105, 'f': 114, 'm': 94, 'x': 100, 'd': 121, 't': 126, 'u': 102, 'i': 107, 'y': 111, 'w': 101, 'e': 117, 'z': 95, 'r': 92, 'a': 116, 'p': 108, 'o': 123, 'j': 99, 'q': 97}
    sequence2 = {'j': 108, 'q': 120, 'x': 117, 'l': 91, 'p': 126, 'i': 94, 'o': 107, 'n': 125, 'b': 100, 'c': 119, 'w': 121, 'e': 106, 'v': 101, 's': 95, 'u': 116, 'r': 113, 'd': 105, 'm': 122, 'a': 110, 'f': 97, 'h': 99, 'y': 111, 'k': 96, 'z': 118, 'g': 102, 't': 124}
    sequence3 = {'n': 99, 'u': 114, 'm': 91, 'f': 94, 'v': 102, 'x': 119, 'a': 111, 'e': 95, 'k': 117, 'w': 122, 'j': 124, 'o': 92, 'c': 106, 'z': 109, 'h': 112, 't': 96, 'i': 105, 'r': 113, 'd': 108, 's': 120, 'g': 93, 'p': 107, 'l': 121, 'q': 126, 'b': 104, 'y': 110}
    sequence4 = {'r': 102, 'c': 119, 't': 94, 'i': 120, 'j': 112, 'f': 111, 'q': 95, 'n': 117, 'a': 121, 'v': 115, 'o': 110, 'x': 104, 'm': 98, 'e': 118, 'y': 109, 'p': 125, 'b': 114, 's': 123, 'g': 91, 'h': 101, 'l': 106, 'u': 116, 'z': 108, 'd': 105, 'w': 122, 'k': 92}
    sequence5 = {'a': 93, 'm': 110, 'h': 117, 'l': 123, 'd': 95, 'z': 97, 'k': 92, 'p': 112, 'u': 94, 'j': 108, 's': 118, 'q': 111, 'e': 119, 'v': 98, 'f': 105, 't': 91, 'x': 122, 'r': 116, 'n': 99, 'g': 101, 'w': 126, 'y': 106, 'b': 104, 'i': 103, 'o': 124, 'c': 121}

    keys ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    # values = random.sample(range(91,127), len(keys))  // Can be used to generate a new key value sequence that you can use to encrypt your file.
    # sample_dict = dict(zip(keys, values))
    file_name = args.encrypt
    encrypted_file_name = "encrypted.txt"
    decrypted_file_name = "decrypted.txt"




    def determine_largest_word(filename):
        largest_word = ''
        with open(filename, 'r') as file:
            for word in file:
                for line in word.split():
                    if len(largest_word) < len(line):
                        largest_word = line
        return largest_word





    def generateparaphrase(length, character):
        count = len(determine_largest_word(file_name))
        password = ''.join(random.choice(list(keys)) for _ in range(length))+character+chr(128)+chr(112)
        if count <= 5:
            password = password[:2] + character + password[3:]
        elif count > 5 & count <= 7:
            password = password[:3] + character + password[4:]
        else:
            password = password[:5] + character + password[6:]
        return password


    def openfile(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content

    def writeToFile(content):
        with open(encrypted_file_name, 'w') as file:
            file.write(content)

    def writeDecryptedToFile(content):
        with open(decrypted_file_name, 'w') as file:

            file.write(content)

    def cleardata():
        with open(file_name, 'w') as file:
            file.write(' ')


    def encrypt(content):
        count = len(determine_largest_word(file_name))
        encrypted_content = ''
        if count <= 5:
            for word in content:
                if word.lower() in sequence2:
                    encrypted_text = chr(sequence2[word.lower()])
                    if word.isupper():
                        encrypted_content += encrypted_text.upper()
                    else:
                        encrypted_content += encrypted_text
                else:
                    encrypted_content += word
            print("If you lose your passkey, your data may be lost")
            print("PASSKEY:", generateparaphrase(len(determine_largest_word(file_name)), chr(36)))

            writeToFile(encrypted_content)
            cleardata()

        elif count > 5 & count <= 7:
            for word in content:
                if word.lower() in sequence3:
                    encrypted_text = chr(sequence3[word.lower()])
                    if word.isupper():
                        encrypted_content += encrypted_text.upper()
                    else:
                        encrypted_content += encrypted_text
                else:
                    encrypted_content += word
            print("If you lose your passkey, your data may be lost")
            print("PASSKEY:", generateparaphrase(len(determine_largest_word(file_name)), chr(38)))

            writeToFile(encrypted_content)
            cleardata()
        else:
            for word in content:
                if word.lower() in sequence5:
                    encrypted_text = chr(sequence5[word.lower()])
                    if word.isupper():
                        encrypted_content += encrypted_text.upper()
                    else:
                        encrypted_content += encrypted_text
                else:
                    encrypted_content += word
            print("If you lose your passkey, your data may be lost")
            print("PASSKEY:", generateparaphrase(len(determine_largest_word(file_name)), chr(64)))

            writeToFile(encrypted_content)
            cleardata()

    def decrypt(content):
        print("You have two chances before the encrypted file is erased.")

        global runs

        runs +=1
        passwordkey = input("Enter your passkey to decrypt: ")



        if runs >=2:
            "Incorrect passkey encrypted file will be cleared now"
            with open(encrypted_file_name, 'w') as file:
                file.write(' ')
        if len(passwordkey)<=5:
            special_char = passwordkey[2]
        elif len(passwordkey) > 5 & len(passwordkey) <= 7:
            special_char = passwordkey[3]
        else:
            special_char = passwordkey[5]

        decrypted_content = ''
        if special_char == chr(36):
            reverse_dict = {chr(value): key for key, value in sequence2.items()}

            for word in content:
                if word.lower() in reverse_dict:
                    decrypted_text = reverse_dict[word.lower()]
                    if word.isupper():
                        decrypted_content += decrypted_text.upper()
                    else:
                        decrypted_content += decrypted_text
                else:
                    decrypted_content += word
            print("File decrypted")
            return decrypted_content
        elif special_char == chr(38):
            reverse_dict = {chr(value): key for key, value in sequence3.items()}

            for word in content:
                if word.lower() in reverse_dict:
                    decrypted_text = reverse_dict[word.lower()]
                    if word.isupper():
                        decrypted_content += decrypted_text.upper()
                    else:
                        decrypted_content += decrypted_text
                else:
                    decrypted_content += word
            print("File decrypted")
            return decrypted_content
        elif special_char == chr(64):
            print("File decrypted")
            reverse_dict = {chr(value): key for key, value in sequence5.items()}

            for word in content:
                if word.lower() in reverse_dict:
                    decrypted_text = reverse_dict[word.lower()]
                    if word.isupper():
                        decrypted_content += decrypted_text.upper()
                    else:
                        decrypted_content += decrypted_text
                else:
                    decrypted_content += word
            print("File decrypted")
            return decrypted_content
        else:
            print("Wrong Password")
            writeDecryptedToFile(decrypt(openfile(encrypted_file_name)))
            return ''

    if args.encrypt:
        encrypt(openfile(args.encrypt))
    if args.decrypt:
        writeDecryptedToFile(decrypt(openfile(args.decrypt)))
    # # encrypt(openfile("trial.txt"))
    # writeDecryptedToFile(decrypt(openfile(encrypted_file_name)))

if __name__ == "__main__":
    main()