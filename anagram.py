def anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    countword1, countword2 = {}, {}

    for i in range(len(word1)):
        countword1[word1[i]] = 1 + countword1.get(word1[i], 0)
        countword2[word2[i]] = 1 + countword2.get(word2[i], 0)
    print(countword1)
    print(countword2)
    return countword1 == countword2


print(anagram("anagram", "magrana"))
