


yangjie_rich_pretrain_unigram_path = '/home/xzg/TENER-master/data/gigaword_chn.all.a2b.uni.ite50.vec'
yangjie_rich_pretrain_bigram_path = '/home/xzg/TENER-master/data/gigaword_chn.all.a2b.bi.ite50.vec'
yangjie_rich_pretrain_word_path = '/home/xzg/TENER-master/data/ctb.50d.vec'

yangjie_rich_pretrain_char_and_word_path = '../data/yangjie_word_char_mix.txt'
lk_word_path = '/home/xzg/Flat-Lattice-Transformer-master/sgns.merge.word/sgns.merge.word'
tencet_word_path = '/data/ws/Tencent_AILab_ChineseEmbedding.txt'



ontonote4ner_cn_path = '/home/xzg/TENER-master/data/ontonotes5'
msra_ner_cn_path = '/home/xzg/TENER-master/data/MSRANER'
resume_ner_path = '/home/xzg/TENER-master/data/ResumeNER'
weibo_ner_path = '/home/xzg/Flat-Lattice-Transformer-master/weiboall'
pku_cws_path='/home/xzg/TENER-master/data/pku'
cityu_cws_path='/home/xzg/TENER-master/data/cityu'
pku_msr_path='/home/xzg/TENER-master/data/msr'
pku_as_path='/home/xzg/TENER-master/data/as'
data_filename = {
            "weibo": {
                "path": '/home/xzg/Flat-Lattice-Transformer-master/weiboall',
                "train": "train.all.bmes",
                "dev": "dev.all.bmes",
                "test": "test.all.bmes",
            },
            "resume": {
                "path": '/home/xzg/TENER-master/data/ResumeNER',
                "train": "train.char.bmes",
                "dev": "dev.char.bmes",
                "test": "test.char.bmes",
            },
            "ontonotes": {
                "path": '/home/xzg/TENER-master/data/ontonotes5',
                "train": "train.bio_clip",
                "dev": "dev.bio_clip",
                "test": "test.bio_clip",
            },
            "msra": {
                "path": '/home/xzg/TENER-master/data/MSRANER',
                "train": "train.char.bmes_clip",
                "dev": "dev.char.bmes_clip",
                "test": "test.char.bmes_clip",
            },
            "pku": {
                "path": '/home/xzg/TENER-master/data/pku',
                "train": "train.txt",
                "dev": "dev.txt",
                "test": "test.txt",
            },
            "cityu": {
                "path": '/home/xzg/TENER-master/data/cityu',
                "train": "train.txt",
                "dev": "dev.txt",
                "test": "test.txt",
            },
            "msr": {
                "path": '/home/xzg/TENER-master/data/msr',
                "train": "train.txt",
                "dev": "dev.txt",
                "test": "test.txt",
            },
            "as": {
                "path": '/home/xzg/TENER-master/data/as',
                "train": "train.txt",
                "dev": "dev.txt",
                "test": "test.txt",
            }
        }
