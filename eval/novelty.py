import spacy
test=['母亲是避风的港湾，让归航的我不再漂泊。',
    '一艘银灰色的气垫船，像一匹纯种烈马，在金波粼粼的海面上飞掠而过。', 
    '几颗星星也连在一起，看上去好像一只巨大的勺子。']

comparators = ['像','是','好像','仿佛', '似', '好似']

class comparisons:
    def __init__(self):
        self.nlp = spacy.load('zh_core_web_sm')
        self.comparators = ['像','是','好像','仿佛', '似', '好似']

    def find_nsubj(self, token):
        for t in token.children:
            if t.dep_ == 'nsubj':
                return t.text
        if token.dep_ !='ROOT':
            return self.find_nsubj(token.head)
        else:
            return None

    def find_dobj(self, token):
        for t in token.children:
            if t.dep_ == 'dobj':
                return t.text
            else:
                obj = self.find_dobj(t)
                if obj is not None: return obj
        return None
    
    def parse(self, sent):
        doc = self.nlp(sent)
        pair = None
        for token in doc:
            if token.head.text in comparators and token.dep_ == 'dobj':
                vehicle = token.text
                tenor = self.find_nsubj(token)
                pair = [tenor, vehicle, token.head.text]
                break
            for c in token.children:
                if c.text in comparators:
                    tenor = self.find_nsubj(token)
                    vehicle = self.find_dobj(token)
                    if vehicle is None and token.pos_== 'NOUN': vehicle = token.text
                    pair = [tenor, vehicle, c.text]
                    break
        return pair