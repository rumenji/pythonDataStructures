def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a','o','u','i','e', 'A', 'O','U','I','E']
    found_vowels = []
    new_word = []
    for char in s:
        if char in vowels:
            found_vowels.append(char)
    for char in s:
        if char in vowels:
            new_word.append(found_vowels[-1])
            found_vowels.pop()
        else:
            new_word.append(char)
    return ''.join(new_word)
