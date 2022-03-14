from lyc.utils import BaiduTranslator

trans_tasks = [
    ('generated_examples/GPT2.tsv', 'zh', 'en'),
    ('generated_examples/MetaGen.tsv', 'zh', 'en')
]

if __name__ == '__main__':
    for task in trans_tasks:
        file_path, from_lang, to_lang = task
        