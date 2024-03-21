# CLSEG4CWS


This is the code for the paper [Improving Chinese Word Segmentation with Character-Lexicon Class Attention](ID: NCAA-D-23-07088). 

## Introduction

We  consider character-lexicon attention with word match position and calculate the probability of characters appearing at the beginning (B), end (E), middle (M), and single (S) of words. We therefore propose a neural framework, CLSEG, which incorporates mask and class attention mechanisms to generate informative position features for characters, based on both character and lexicon contexts.

## Environment Requirement
The code has been tested under Python 3.7. The required packages are as follows:
```
torch==1.5.1
numpy==1.18.5
FastNLP==0.5.0
fitlog==0.3.2
```
you can click [here](https://fastnlp.readthedocs.io/zh/latest/) to know more about FastNLP. And you can click [here](https://fitlog.readthedocs.io/zh/latest/) to know more about Fitlog.

## Example to Run the Codes
1. Download the pretrained character embeddings and word embeddings and put them in the data folder.
    * Character embeddings (gigaword_chn.all.a2b.uni.ite50.vec): [Google Drive](https://drive.google.com/file/d/1_Zlf0OAZKVdydk7loUpkzD2KPEotUE8u/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
    * Bi-gram embeddings (gigaword_chn.all.a2b.bi.ite50.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
    * Word(Lattice) embeddings (ctb.50d.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
    * If you want to use a larger word embedding, you can refer to [Chinese Word Vectors 中文词向量](https://github.com/Embedding/Chinese-Word-Vectors) and [Tencent AI Lab Embedding](https://ai.tencent.com/ailab/nlp/en/embedding.html)

2. Modify the `utils/paths.py` to add the pretrained embedding and the dataset.

3. Long sentence clipping for MSRA and Ontonotes, run the command:
```bash
python sentence_clip.py
```

4. Merging char embeddings and word embeddings:
```bash
python char_word_mix.py
```

5. Model training and evaluation
    * PKU dataset
    ```shell
    python main.py --dataset pku
    ```
    * MSR dataset
    ```shell
    python main.py --dataset msr
    ```
    * AS dataset
    ```shell
    python main.py --dataset as
    ```
    * Cityu dataset
    ```shell
    python main.py --dataset cityu
    ```

## Acknowledgements
* Thanks to Dr. Li and his team for contributing the [FLAT source code](https://github.com/LeeSureman/Flat-Lattice-Transformer).
* Thanks to the author team and contributors of [TENER source code](https://github.com/fastnlp/TENER).
* Thanks to the author team and contributors of [FastNLP](https://github.com/fastnlp/fastNLP).
