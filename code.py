import cv2
import os

def encrypt_image(img, message):
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    n, m, z = 0, 0, 0

    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def decrypt_message(img, password):
    decrypted_message = ""
    n, m, z = 0, 0, 0

    passcode = input("Enter passcode for Decryption: ")

    if password == passcode:
        for i in range(len(msg)):
            decrypted_message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decryption message:", decrypted_message)
    else:
        print("Not a valid key")

if __name__ == "__main__":
    img = cv2.imread("wallp.jpg")
    msg = input("Enter secret message: ")
    password = input("Enter password: ")

    encrypted_img = encrypt_image(img.copy(), msg)
    cv2.imwrite("Encryptedmsg.jpg", encrypted_img)
    os.system("start Encryptedmsg.jpg")

    decrypt_message(encrypted_img.copy(), password)
