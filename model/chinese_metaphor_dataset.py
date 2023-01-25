import datasets
# import pandas as pd
import json

_CITATION = """\
@inproceedings{li-etal-2022-cm,
    title = "{CM}-Gen: A Neural Framework for {C}hinese Metaphor Generation with Explicit Context Modelling",
    author = "Li, Yucheng  and
      Lin, Chenghua  and
      Guerin, Frank",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.563",
    pages = "6468--6479",
}

@misc{li-inlg-2022-nominal,
  doi = {10.48550/ARXIV.2206.05195},
  url = {https://arxiv.org/abs/2206.05195},
  author = {Li, Yucheng and Lin, Chenghua and Geurin, Frank},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Nominal Metaphor Generation with Multitask Learning},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
"""

_DESCRIPTION = """\
Chinese Metaphor Corpus

The first Chinese metaphor corpus serving both metaphor identification and generation. 
首个中文比喻数据集，可以用于中文比喻识别与中文比喻生成。
"""

_HOMEPAGE = "https://github.com/liyucheng09/Metaphor_Generator"

_URL = 'https://github.com/liyucheng09/Metaphor_Generator/raw/master/CMC/zh_CMC2.txt'

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
            description=_DESCRIPTION,
            features=datasets.Features(feature),
            homepage=_HOMEPAGE,
            citation=_CITATION
        )
    
    def _split_generators(self, dl_manager):
        
        cmc_file = dl_manager.download(_URL)

        return datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'cmc_file': cmc_file}),
        # return [
        #     datasets.SplitGenerator(name='hard', gen_kwargs={'filepath': self.config.data_path}),
        # ]
    
    def _generate_examples(self, cmc_file):
        with open(cmc_file, encoding='utf-8') as f:
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