import json
import sys
sys.path.append('/Users/liyucheng/projects/Metaphor_Generator/eval')
from novelty import comparisons
from dataclasses import dataclass

def identify_tenor(key_list, sent):
    if not key_list[0].startswith('<'):
        for key in key_list:
            if key in sent:
                start = sent.index(key)
                return key
                # return (start, start+len(key))
    return None

@dataclass
class Example:
    sent: str
    tenor: str = None
    vehicle: str = None
    comparator: str = None

    def to_dict(self,):
        return {
            'sent': self.sent,
            'tenor': self.tenor if self.tenor is not None else '_',
            'vehicle': self.vehicle if self.vehicle is not None else '_',
            'comparator': self.comparator if self.comparator is not None else '_'
        }

def parse_liu_data_and_write():
    all_sents = []
    for file in glob('Chinese-Simile-Recognition-Dataset/*.tsv'):
        with open(file, encoding='utf-8') as f:
            sents = f.read().split('\n\n')
        for sent in sents:
            tokens = sent.split('\n')
            label = tokens[0]
            if label == 'literal': continue
            ts = []
            for t in tokens:
                if '\t' not in t: continue
                t_text, t_label = t.split('\t')
                ts.append(t_text)
                if t_label == 'ts': tenor = t_text
                if t_label == 'vs': vehicle = t_text
            text = ''.join(ts)
            all_sents.append([text, tenor, vehicle])
    
    all_examples = [Example(sent=sent[0], tenor=sent[1], vehicle=sent[2], comparator='像') for sent in all_sents]
    with open('CMC/zh_CMC2.txt', 'a', encoding='utf-8') as f:
        for i in all_examples:
            line = json.dumps(i.to_dict(), ensure_ascii=False)
            f.write(line + '\n')

if __name__ == '__main__':
    path = 'CMC/Metaphor_corpus_final_version.json'
    output_path = 'CMC/zh_CMC2.txt'

    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    
    identifier = comparisons()

    all_examples = []
    for key, sents in data.items():
        key_list = key.split(',')
        for sent in sents:
            reference_tenor = identify_tenor(key_list, sent)
            tenor = reference_tenor
            vehicle = None
            comparator = None
            if tenor is None:
                pair = identifier.parse(sent)
                if pair is not None:
                    tenor, vehicle, comparator = pair
            example = Example(sent=sent, tenor=tenor, vehicle=vehicle, comparator = comparator)
            all_examples.append(example)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for i in all_examples:
            line = json.dumps(i.to_dict(), ensure_ascii=False)
            f.write(line + '\n')
    
    print('Finished!')