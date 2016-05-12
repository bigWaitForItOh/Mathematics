#for capital letters only

def encrypt_alphabet (alphabet, key):
    alpha_code = ord (alphabet) - ord ('A');
    alpha_code += (ord (key) - ord ('A'));
    alpha_code %= (ord ('Z') - ord ('A'))+1;
    alpha_code += ord ('A');
    return (chr (alpha_code));

def vigenere_encrypt (message, digest):
    i, cipher = 0, '';
    for alpha in message:
        cipher += encrypt_alphabet (alpha, digest [i]);
        i += 1;
        if (i == len (digest)): i = 0;

    return (cipher);

if (__name__ == '__main__'):
    message = input ('Enter message: ');
    key = input ('Enter key: ');
    print ('Cipher Text: \n', vigenere_encrypt (message, key));
