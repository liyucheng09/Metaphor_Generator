# Chinese Metaphor Generation

Source code and dataset of **INLG 2022 oral**: [Nominal Metaphor Generation with Multitask Learning](https://arxiv.org/abs/2206.05195).

首个中文比喻数据集，可以用于中文比喻识别与中文比喻生成。

## Chinese Metaphor Corpus

The first Chinese metaphor corpus serving both metaphor identification and generation. The definition of metaphor in Chinese is different with its English counterpart. So we cannot borrow metaphor resource in English and use it in Chinese metaphor processing.

We construct a big metaphor resoruce in Chinese with around 9000 metaphorical sentences with *tenor* and *vehicle* annotated. Some examples are shown below.

```
{"sent": "春风像一只彩笔，把整个世界勾勒得更加绚丽多彩", "tenor": "春风", "vehicle": "彩笔", "comparator": "像"}
{"sent": "秋天，不仅是一个丰收的季节，还让我们饱览了迷人的景色。秋天在秋姑娘的点缀后，像一颗发光的明珠！", "tenor": "秋天", "vehicle": "明珠", "comparator": "像"}
{"sent": "春风像个慈祥的母亲，拂着你的脸颊，使你感到舒畅，心旷神怡。", "tenor": "春风", "vehicle": "母亲", "comparator": "像"}
{"sent": "秋天，田里的稻谷黄澄澄的，像一片片金色的海洋。天空是蓝蓝的，像一片无边无际的大海。", "tenor": "天空", "vehicle": "大海", "comparator": "像"}
```

As shown here metaphor sentences and their components are identified. To enlarge the dataset, we merge the dataset published in [Liu et al. 2018](https://aclanthology.org/D18-1183.pdf) with ours. If you use the dataset, please cite both our and their paper.

The dataset can be found in `CMC/zh_CMC2.txt`.


--- Old Version of CMC ---

Chinese binary metaphor identification dataset. Each sentence within the dataset has a metaphor label indicating whether it is a metaphor or not. Both training and test splits of CMC are shown in `CMC/old_version`.

Some examples shown here.

```
1	月季花的叶子慢慢地伸平了，而且还长出了许多像羊胡子似的须根。
1	一艘银灰色的气垫船，像一匹纯种烈马，在金波粼粼的海面上飞掠而过。
0	还有：啊，克莱德，克莱德，今天，生活里一切跟去年相比，该有多么不一样呀。
0	”青豆说。
1	夏天的山也是绿色的，那绿色浓浓的，一片片树叶，不管是大的还是小的，都像被绿油彩涂过，连雨点落上去，都给染绿的。
0	”秦羽也不谦虚。
0	“已经到了最后一层时空了，没地方可以消失了。
1	几颗星星也连在一起，看上去好像一只巨大的
0	本来是不要去看朋友的；上哪儿去呢？走着瞧吧。
```
Label and sentence was splited by `\t`

![](https://github.com/nine09/Creative-Text-Generator/blob/master/images/samples.png)
![](https://github.com/nine09/Creative-Text-Generator/blob/master/images/CMC.png)


## Chinese Literature Dataset
Chinese Literature corpus (CLC) is a corpus contains only chinese literatures. Literature only corpus is been needed in some NLP tasks, like processing some kinds of texts which are more frequnt viewed in literatures, or analyisis of the difference between literature and other texts (like mews and dialogues). 

![](https://github.com/nine09/Creative-Text-Generator/blob/master/images/CLD.png)

Chinese Literature Dataset consists of 7.31 millon sentences crawled from 1300+ chinese books, which has already been shuffled. Average length of all sentences is 29 tokens.

The download url is: https://pan.baidu.com/s/1XY72p_QHnYuP8-yQkOY0fA.


## citation

If you use our resource, do remember citing our paper:

```
@misc{https://doi.org/10.48550/arxiv.2206.05195,
  doi = {10.48550/ARXIV.2206.05195},
  url = {https://arxiv.org/abs/2206.05195},
  author = {Li, Yucheng and Lin, Chenghua and Geurin, Frank},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Nominal Metaphor Generation with Multitask Learning},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```