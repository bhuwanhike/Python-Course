
# Split only two words by @
def split(string):
    firs = ''
    sec = ''
    addFirst = True
    for c in string:
        if addFirst and c != '@':
            firs += c
        if c == '@':
            addFirst = False
            continue
        if not addFirst:
            sec += c
    return firs, sec


# Mimics the python Split function with any delimiter.
def split(string, delimiter):

    result = []
    word = ''
    for c in string:
        if c != delimiter:
            word += c
        else:
            result.append(word)
            word = ''

    result.append(word)
    return result
