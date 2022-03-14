import sys

sp="#####"

def distinct_2(path):
    inFile = open(path, mode="r", encoding="utf8")
    bichar_set = set()
    all_bigram_count = 0
    for line in inFile.readlines():
        line = line.strip().split(" ")
        sent = ""
        for word in line:
            sent += word
        char_len = len(sent)
        for idx in range(char_len - 1):
            bichar_set.add(sent[idx] + sp + sent[idx + 1])
        bichar_set.add("<BOS>" + sp + sent[0])
        bichar_set.add(sent[char_len - 1] + sp + "<EOS>")
        all_bigram_count += (char_len + 1)

    distinct_bigram_count = len(bichar_set)
    print("distinct_bigram: ", distinct_bigram_count)
    print("all_bigram: ", all_bigram_count)
    print("distinct 1: " + str(distinct_bigram_count / all_bigram_count))
    inFile.close()

distinct_2(sys.argv[1])
