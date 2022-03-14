import spacy
test=['母亲是避风的港湾，让归航的我不再漂泊。',
    '一艘银灰色的气垫船，像一匹纯种烈马，在金波粼粼的海面上飞掠而过。', 
    '几颗星星也连在一起，看上去好像一只巨大的勺子。']

comparators = ['像','是','好像']

def find_nsubj(token):
    for t in token.children:
        if t.dep_ == 'nsubj':
            return t
    if token.dep_ !='ROOT':
        return find_nsubj(token.head)
    else:
        return None

def find_dobj(token):
    for t in token.children:
        if t.dep_ == 'dobj':
            return t
        else:
            obj = find_dobj(t)
            if obj is not None: return obj
    return None

if __name__ == '__main__':
    nlp = spacy.load('zh_core_web_trf')
    comparisons = []
    for sent in test:
        doc = nlp(sent)
        pair = None
        for token in doc:
            if token.head.text in comparators and token.dep_ == 'dobj':
                vehicle = token
                tenor = find_nsubj(token)
                pair = [tenor, vehicle]
                break
            if any([c.text in comparators for c in token.children]):
                tenor = find_nsubj(token)
                vehicle = find_dobj(token)
                if vehicle is None and token.pos_== 'NOUN': vehicle = token
                pair = [tenor, vehicle]
                break
        comparisons.append(pair)

    print(comparisons)


