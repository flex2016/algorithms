

def anagram(s1,s2):

    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)

anagram('dog','god')

anagram('clint eastwood','old west action')

anagram('aa','bb')


def anagram2(s1,s2):

    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    # Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}

    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True

anagram2('dog','god')

anagram2('clint eastwood','old west action')

anagram2('aa','bb')
