from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    text, key, encrypted_text, decrypted_text = "", "", "", ""

    if request.method == "POST":
        action = request.form['action']
        text = request.form['text']
        key = int(request.form['key'])

        if action == "encrypt":
            encrypted_text = caesar_cipher.encrypt_text(text, key)
        elif action == "decrypt":
            decrypted_text = caesar_cipher.decrypt_text(text, key)

    return render_template("caesar.html", text=text, key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

@app.route("/vigenere", methods=['GET', 'POST'])
def vigenere():
    text, key, encrypted_text, decrypted_text = "", "", "", ""

    if request.method == "POST":
        action = request.form['action']
        text = request.form['text']
        key = request.form['key']

        if action == "encrypt":
            encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
        elif action == "decrypt":
            decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)

    return render_template("vigenere.html", text=text, key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

@app.route("/railfence", methods=['GET', 'POST'])
def railfence():
    text, key, encrypted_text, decrypted_text = "", "", "", ""

    if request.method == "POST":
        action = request.form['action']
        text = request.form['text']
        key = int(request.form['key'])

        if action == "encrypt":
            encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
        elif action == "decrypt":
            decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)

    return render_template("railfence.html", text=text, key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

@app.route("/playfair", methods=['GET', 'POST'])
def playfair():
    text, key, encrypted_text, decrypted_text = "", "", "", ""

    if request.method == "POST":
        action = request.form['action']
        text = request.form['text']
        key = request.form['key']

        playfair_matrix = playfair_cipher.create_playfair_matrix(key)

        if action == "encrypt":
            encrypted_text = playfair_cipher.playfair_encrypt(text, playfair_matrix)
        elif action == "decrypt":
            decrypted_text = playfair_cipher.playfair_decrypt(text, playfair_matrix)

    return render_template("playfair.html", text=text, key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

@app.route("/transposition", methods=['GET', 'POST'])
def transposition():
    text, key, encrypted_text, decrypted_text = "", "", "", ""

    if request.method == "POST":
        action = request.form['action']
        text = request.form['text']
        key = int(request.form['key'])

        if action == "encrypt":
            encrypted_text = transposition_cipher.encrypt(text, key)
        elif action == "decrypt":
            decrypted_text = transposition_cipher.decrypt(text, key)

    return render_template("transposition.html", text=text, key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
