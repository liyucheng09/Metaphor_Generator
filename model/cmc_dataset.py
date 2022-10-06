import datasets
# import pandas as pd
import json

class CMC(datasets.GeneratorBasedBuilder):

    BUILDER_CONFIG_CLASS=datasets.BuilderConfig

    def _info(self):

        feature = {
            'sent': datasets.Value('string'),
            'tenor': datasets.Value('string'),
            'comparator': datasets.Value('string'),
            'vehicle':datasets.Value('string'),
        }

        return datasets.DatasetInfo(
            description='The Chinese Metaphor Corpus',
            features=datasets.Features(feature),
        )
    
    def _split_generators(self, dl_manager):

        return datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'data_dir': self.config.data_dir}),
        # return [
        #     datasets.SplitGenerator(name='hard', gen_kwargs={'filepath': self.config.data_path}),
        # ]
    
    def _generate_examples(self, data_dir):
        with open(data_dir, encoding='utf-8') as f:
            count = 0
            for line in f:
                if not line:
                    continue
                data = json.loads(line)
                yield count, {
                    'sent': data['sent'],
                    'tenor': data['tenor'],
                    'comparator': data['comparator'],
                    'vehicle': data['vehicle']
                }
                count+=1