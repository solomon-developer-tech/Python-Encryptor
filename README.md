# Text File Encryptor

This Python script encrypts text files using a key-value pair sequence. Currently, it supports text file encryption, with plans to support other file extensions in the future. The script utilizes a random sequence of key-value pairs to encrypt files, offering more than 36^26 possible combinations of sequences, though only 3 sequences are currently used in the program. 

## Key Features

- **File Encryption**: Encrypts a specified text file and generates an encrypted file called `encrypted.txt` in the same directory as the Python script.
- **Encryption Sequences**: The encryption uses a random sequence of key-value pairs. Currently, 3 random sequences are implemented, but modifications to the sequences are possible.
- **Passkey Generation**: A passkey is created during the encryption process. If this key is lost, the data will be cleared after two consecutive failed decryption attempts.
- **File Integrity Warning**: Ensure that the sequences used for encryption are backed up. If the encryption sequence is lost, decryption may not work correctly, and the encrypted data could be irrecoverable.

## Usage

### Encrypt a File

To encrypt a text file, run the script with the `-e` option followed by the file name.

```bash
python encryptor.py -e trial.txt
```
### Decrypt a File

To decrypt an encrypted file, run the script with the -d option followed by the encrypted file name.
```bash
python encryptor.py -d encrypted.txt
```
Important: If the decryption fails twice in a row, the encrypted data will be permanently cleared.
## Options and Usage
### Command-Line Arguments

- -e: Specify the name of the text file to encrypt.
- -d: Specify the name of the text file to decrypt.

## How It Works

### Encryption:
- A random key-value pair sequence is generated.
- The original file's content is encrypted using this sequence.
- The original file is cleared.
- The encrypted content is saved to a new file named encrypted.txt.

### Decryption:
- The program verifies the passkey.
- If the passkey is correct, the file is decrypted.
- If the passkey is incorrect twice consecutively, the encrypted data is permanently deleted.

# Notes

- File Extension Support: Currently supports only .txt files. Future updates may extend support to other file formats.
- Key Management:
- Ensure you save the passkey securely.
- Losing the passkey may result in permanent data loss.

# Future Enhancements

- **    Support for encrypting and decrypting additional file types.
- **    Ability to customize the encryption algorithm or select between predefined sequences.
- **    Improved passkey management and recovery options.

# Disclaimer

- Use this program responsibly. The developers are not liable for data loss resulting from improper use or loss of the passkey.

For any queries or contributions, feel free to contact us or submit a pull request!
