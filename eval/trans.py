from lyc.utils import BaiduTranslator
import pandas as pd
import os

trans_tasks = [
    ('generated_examples/GPT2.tsv', 'zh', 'en'),
    ('generated_examples/MetaGen.tsv', 'zh', 'en')
]

if __name__ == '__main__':
    translator = BaiduTranslator()
    for task in trans_tasks:
        file_path, from_lang, to_lang = task
        with open(file_path, encoding='utf-8') as f:
            query = f.read()
            responds = translator.make_request(query, from_lang, to_lang)
            results = responds['trans_result']
            df = pd.DataFrame(results)
            df.to_csv(file_path+'.out', sep='\t', index=False)