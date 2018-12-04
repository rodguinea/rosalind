def num_words_dic(s):
    diccionary = {}
    string = s.split(' ')

    for i in range(0, len(string)):
        diccionary.update({string[i]: string.count(string[i])})

    for key, value in diccionary.items():
        print(key, value)

    return diccionary
