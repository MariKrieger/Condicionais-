def is_palindrome(word):

    cleaned_word = word.lower().replace(" ", "")


    return cleaned_word == cleaned_word[::-1]



user_input = input("Digite uma palavra: ")


if is_palindrome(user_input):
    print("{} é um palíndromo!".format(user_input))
else:
    print("{} não é um palíndromo.".format(user_input))

