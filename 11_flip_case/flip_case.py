def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swappedPhrase = ''
    for l in phrase:
        if l.lower() == to_swap.lower():
            swappedPhrase = swappedPhrase + l.swapcase()
        else:
            swappedPhrase = swappedPhrase + l
    return swappedPhrase