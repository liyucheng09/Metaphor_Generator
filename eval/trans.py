from lyc.utils import BaiduTranslator
import pandas as pd
import os
from tqdm import tqdm
import time

trans_tasks = [
    # ('generated_examples/GPT2.tsv', 'zh', 'en'),
    ('generated_examples/MetaGen.tsv', 'zh', 'en'),
    ('generated_examples/SCOPE.tsv', 'en', 'zh')
]
num_sent_per_request = 5

if __name__ == '__main__':
    translator = BaiduTranslator()
    for task in trans_tasks:
        file_path, from_lang, to_lang = task
        with open(file_path, encoding='utf-8') as f:
            final_results = []
            lines = f.readlines()
            for i in tqdm(range(0, len(lines), 5)):
                query = '\n'.join(lines[i:i+5])
                for _ in range(10):
                    try:
                        responds = translator.make_request(query, from_lang, to_lang)
                        results = responds['trans_result']
                    except:
                        print('Failed! retrying...')
                        time.sleep(3)
                        continue
                    else:
                        break
                final_results.extend(results)
            df = pd.DataFrame(final_results)
            df.to_csv(file_path+'.out', sep='\t', index=False)
            print(f'Saved to {file_path}.out !')
