import random
from kelimeler import words_list

def get_words():
    word = random.choice(words_list)
    return word.upper()

def play(word):
    word_show = "_" * len(word)
    guess = False
    guess_letters = []
    guess_word = []
    chance = 8

    print("----* HADİ OYNAYALIM *----")
    print(f"{chance} hakkın var.")
    print("\n")
    print(word_show)
    print("\n")
    resim = ["""
     +---+
       |   |
           |
           |
           |
           |
    --------""", """
     +---+
       |   |
       O   |
           |
           |
           |
    --------""", """
     +---+
       |   |
       O   |
       |   |
           |
           |
    --------""", """
     +---+
       |   |
       O   |
      /|   |
           |
           |
    --------""", """
     +---+
       |   |
       O   |
      /|   |
           |
           |
    --------""", """
     +---+
       |   |
       O   |
      /|   |
      /    |
           |
    --------""", """
     +---+
       |   |
       O   |
      /|   |
      /    |
           |
    --------""", """
     +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    --------""","""
     +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    --------"""]
    adim = 0
    while not guess and chance > 0:
        tahmin = input("Tahminde bulunun: ").upper()

        if len(tahmin)==1 and tahmin.isalpha():
            if tahmin in guess_letters:
                print(f"{tahmin} harfini daha önce denediniz.")
            elif tahmin not in word:
                adim += 1
                print("YANLIŞ ")
                print(resim[adim])
                print(chance-adim,"HAKKIN KALDI")

                if chance-adim == 0:
                    print(f"KAYBETTİN KELİME : {word}")
                    break
            else:
                print(f"{tahmin} harfi kelimede var")
                guess_letters.append(tahmin)
                dogrukelime = list(word_show)

            butunkelime = (i for i, letter in enumerate(word) if letter == tahmin)
            for indeks in butunkelime:
                dogrukelime[indeks] = tahmin
                word_show = "".join(dogrukelime)

            if "_" not in word_show:
                guess = True

            print(word_show)
            print("\n")

            if guess == True:
                print("Tebrikler,bildin!")
            else:
                pass
        if tahmin == word:
            print(f"TEBRİKLER BİLDİN KELİME : {word}")
            break

play(get_words())