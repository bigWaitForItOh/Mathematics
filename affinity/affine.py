a, b = 5, 7;	#keys

##################################################################
#Encryption
##################################################################

def crypt_func (a, b, alpha):
	alpha_index = ord (alpha) - ord ('a');
	result = ((a*alpha_index) + b) % 26;
	print (result);
	result += ord ('a');

	return (chr (result));

def affine_encrypt (plain_text):
	cipher = '';

	for alpha in plain_text:
		cipher += crypt_func (a, b, alpha);

	return (cipher);

##################################################################
#Decryption
##################################################################

def a_inverse (a):
	for i in range (1, 26):
		if ( ((a*i) % 26) == 1 ):
			return (i);

def decrypt_func (a, b, alpha):
	alpha_index = ord (alpha) - ord ('a');
	a_inv = a_inverse (a);
	result = (a_inv*(alpha_index-b)) % 26;

	result += ord ('a');
	return (chr (result));

def affine_decrypt (cipher):
	plain = '';

	for alpha in cipher:
		plain += decrypt_func (a, b, alpha);

	return (plain);

if (__name__ == '__main__'):
    message = input ('Enter message: ');
    cipher = affine_encrypt (message);

    print ('Cipher Text: \n' + cipher + '\n');
    print ('Decrypted back: \n' + affine_decrypt (cipher));
