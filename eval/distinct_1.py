import sys

def distinct_1(sentence_list):


    char_set = set()
    all_unigram_count = 0
    for line in sentence_list:
        line = line.strip().split(" ")
        sent = ""
        for word in line:
            sent += word
        for char in sent:
            char_set.add(char)
        all_unigram_count += len(sent)
    distinct_unigram_count = len(char_set)


    distinct_1_score=distinct_unigram_count / all_unigram_count
    return distinct_1_score


sp="#####"
def distinct_2(sentence_list):

    bichar_set = set()
    all_bigram_count = 0
    for line in sentence_list:
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

    distinct_2=distinct_bigram_count / all_bigram_count
    return distinct_2


def get_candidate_reference(path):

  null = []
  like = []
  disgust = []
  sad = []
  happy = []
  angry = []

  with open(path, 'r', encoding='utf-8')as infile:
    lines = infile.readlines()
    for line in lines:
      if line.startswith('null:'):
        loc=line.find(":")+1
        null.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('like:'):
        loc=line.find(":")+1
        like.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('disgust:'):
        loc=line.find(":")+1
        disgust.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('angry:'):
        loc=line.find(":")+1
        angry.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('happy:'):
        loc=line.find(":")+1
        happy.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('sad:'):
        loc=line.find(":")+1
        sad.append(' '.join(jieba.cut(line[loc:].strip())))

  return  null, like, angry, happy, disgust, sad


def get_candidate_reference1(path):

  null = []
  like = []
  disgust = []
  sad = []
  happy = []
  angry = []

  with open(path, 'r', encoding='utf-8')as infile:
    lines = infile.readlines()
    for line in lines:
      if line.startswith('null :'):
        loc=line.find(":")+1
        null.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('like :'):
        loc=line.find(":")+1
        like.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('disgust :'):
        loc=line.find(":")+1
        disgust.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('angry :'):
        loc=line.find(":")+1
        angry.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('happy :'):
        loc=line.find(":")+1
        happy.append(' '.join(jieba.cut(line[loc:].strip())))
      if line.startswith('sad :'):
        loc=line.find(":")+1
        sad.append(' '.join(jieba.cut(line[loc:].strip())))

  return  null, like, angry, happy, disgust, sad







if __name__ == "__main__":

    import jieba

    with open(r'C:\Users\hp\Desktop\测试生成结果\seq2seq\test_result.txt','r',encoding='utf-8')as infile:
        seq2seq = []
        for line in infile.readlines():
            line_list = line.strip().split('\t')
            # print(line_list)
            if len(line_list) == 2:
                line = line_list[1]
            else:
                line = ''
            seq2seq.append(' '.join(jieba.cut(line)))


    print(seq2seq)
    print('seq2seq distinct_1:{}'.format(distinct_1(seq2seq)))
    print('seq2seq distinct_2:{}'.format(distinct_2(seq2seq)))

    path=r'C:\Users\hp\Desktop\测试生成结果\ecm\test_result.txt'
    null, like, angry, happy, disgust, sad = get_candidate_reference(path)


    #average_distinct_1=(distinct_1(angry)+distinct_1(null)+distinct_1(like)+distinct_1(happy)+distinct_1(sad)+distinct_1(disgust))/6

    print('ecm distinct_1: {}'.format(distinct_1(null)))
    print('ecm distinct_2: {}'.format(distinct_2(null)))

    path = r'C:\Users\hp\Desktop\测试生成结果\topic_emotion\test_result.txt'
    null, like, angry, happy, disgust, sad = get_candidate_reference1(path)


    print('topic emotion distinct_1:{}'.format(distinct_1(null)))
    print('topic emotion distinct_2:{}'.format(distinct_2(null)))

    # average_distinct_1 = (distinct_1(angry) + distinct_1(null) + distinct_1(like) + distinct_1(happy) + distinct_1(sad) + distinct_1(disgust)) / 6
    # print(average_distinct_1)

    path = r'C:\Users\hp\Desktop\测试生成结果\topic_emotion with attention\test_result.txt'
    null, like, angry, happy, disgust, sad = get_candidate_reference1(path)

    print(null)

    # average_distinct_1 = (distinct_1(angry) + distinct_1(null) + distinct_1(like) + distinct_1(happy) + distinct_1(
    #     sad) + distinct_1(disgust)) / 6
    print('topic emotion with attention distinct_1:{}'.format(distinct_1(null)))
    print('topic emotion with attention distinct_2:{}'.format(distinct_2(null)))
