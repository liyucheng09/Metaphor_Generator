# Chinese Literature Dataset
Chinese Literature Dataset (CLD) is a corpus contains only chinese literatures. Literature only corpus is been needed in some NLP tasks, like processing some kinds of texts which are more frequnt viewed in literatures, or analyisis of the difference between literature and other texts (like mews and dialogues). 

![](https://github.com/nine09/Creative-Text-Generator/blob/master/images/CLD.png)

Chinese Literature Dataset consists of 7.31 millon sentences crawled from 1300+ chinese books, which has already been shuffled. Average length of all sentences is 29 tokens.

The download url is: https://pan.baidu.com/s/1XY72p_QHnYuP8-yQkOY0fA.

# Chinese Metaphor Corpus
There is no public Chinese metaphor corpus avaiable so far. This made some researches of Chinese metaphor is hard to begin, expecially whose neural approaches which need sufficient training dataset. We decide to break this restriction. We annotate 6000+ sentences manually, each sentence has one label: "is metaphor" or "not metaphor".

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

Here we give both train/eval split of CMC in the folder of `/CMC`.

**Future Update Coming Soon!!** 
We will produce a detailed and extented version of CMC later, with metaphor components manually annotated, e.g., `TENOR` (the subject of metaphor) and `COMPARATOR` (the verb used to compare, such as like).

Besides, CMC will be merged with other available chinese metaphor resources to enlarge the size of the dataset.