import numpy as np

#funcao que transforma uma letra em one-hot encoding (inclui espaço)
def one_hot_encoding(letter, alphabet='abcdefghijklmnopqrstuvwxyz '): 
    one_hot = np.zeros((len(alphabet), 1))  
    index = alphabet.index(letter.lower())  
    one_hot[index][0] = 1 
    return one_hot

def get_alphabet():
    return list('abcdefghijklmnopqrstuvwxyz ') 

def string_to_one_hot(msg, alphabet='abcdefghijklmnopqrstuvwxyz '):
    return np.concatenate([one_hot_encoding(letter, alphabet) for letter in msg], axis=1)

def one_hot_to_string(matrix, alphabet='abcdefghijklmnopqrstuvwxyz '):
    string = ''
    for column in matrix.T:
        index = np.argmax(column)  
        string += alphabet[index]
    return string

#funcao que cifra uma mensagem usando uma matriz de permutacao P
def encrypt(msg, P):
    one_hot_matrix = string_to_one_hot(msg)
    permuted_matrix = np.dot(P, one_hot_matrix)
    return one_hot_to_string(permuted_matrix)

#funcao que decifra uma mensagem usando a matriz inversa de P
def decrypt(msg, P):
    one_hot_matrix = string_to_one_hot(msg)
    inverse_permuted_matrix = np.dot(np.linalg.inv(P), one_hot_matrix) 
    return one_hot_to_string(inverse_permuted_matrix)

#funcao que cifra usando Enigma 
def enigma_cipher(msg, initial_P, E):
    final_message = ""
    P = np.copy(initial_P)  
    for letter in msg:
        final_message += encrypt(letter, P)
        P = np.dot(E, P) 
    return final_message

#funcao que decifra a mensagem Enigma
def enigma_decrypt(msg, initial_P, E):
    final_message = ""
    P = np.copy(initial_P)  
    for letter in msg:
        final_message += decrypt(letter, P)
        P = np.dot(E, P)  
    return final_message

#bloco principal para testar a funcionalidade
if __name__ == "__main__":
    message = "hello "
    alphabet_size = 27  

    #criacao de uma matriz de permutação P e E 
    P = np.eye(alphabet_size)  
    E = np.roll(np.eye(alphabet_size), 1, axis=1)  

    encrypted_message = enigma_cipher(message, P, E)
    print("Mensagem cifrada:", encrypted_message)

    decrypted_message = enigma_decrypt(encrypted_message, P, E)
    print("Mensagem decifrada:", decrypted_message)