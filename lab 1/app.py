from flask import Flask, request, render_template

app = Flask(__name__)

# Используемый алфавит
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def caesar_cipher(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            # индекс буквы и сдвиг
            index = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += letter  # Символ не входящий в алфавит не шифруется 
    return encrypted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    shift = 0
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        action = request.form['action']

        if action == 'Зашифровать':
            encrypted_text = caesar_cipher(text, shift)
        elif action == 'Дешифровать':
            encrypted_text = caesar_cipher(text, -shift)

    return render_template('index.html', encrypted_text=encrypted_text, shift=shift)
if __name__ == '__main__':
    app.run(debug=True)