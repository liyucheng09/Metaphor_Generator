import datasets

label2id = {
    'O': 0, 'ts': 1, 'vs':2, 'tb':3 , 'te':4, 'vb':5 , 've':6, 'tm':7, 'vm':8
}

class Simile(datasets.GeneratorBasedBuilder):

    BUILDER_CONFIG_CLASS=datasets.BuilderConfig

    def _info(self):

        feature = {
            'tokens': datasets.Sequence(datasets.Value('string')),
            'sent': datasets.Value('string'),
            'tags': datasets.Sequence(datasets.features.ClassLabel(num_classes=len(label2id), names=['O', 'ts', 'vs', 'tb', 'te', 'tm', 'vb', 've', 'vm'])),
            'label': datasets.features.ClassLabel(num_classes=2, names=['literal', 'simile'])
        }

        return datasets.DatasetInfo(
            description='The Chinese Simile Dataset',
            features=datasets.Features(feature),
        )
    
    def _split_generators(self, dl_manager):

        return [datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'data_file': self.config.data_dir + '/Chinese-Simile-Recognition-Dataset-Train.tsv'}),
                datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={'data_file': self.config.data_dir + '/Chinese-Simile-Recognition-Dataset-Dev.tsv'}),
                datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={'data_file': self.config.data_dir + '/Chinese-Simile-Recognition-Dataset-Test.tsv'}),
        ]
    
    def _generate_examples(self, data_file):
        with open(data_file, encoding='utf-8') as f:
            count = 0
            for sent in f.read().split('\n\n'):
                if not sent:
                    continue
                tokens = sent.split('\n')
                label = tokens[0]
                words = []
                tags = []
                for token in tokens[1:]:
                    # print(token)
                    token, tag = token.split('\t')
                    words.append(token)
                    tags.append(tag)
                yield count, {
                    'sent': ''.join(words),
                    'tokens': words,
                    'tags': tags,
                    'label': label
                }
                count+=1
