# coding: utf-8

# not only for all six person=
# instead, for most common person
stop_places = ['贾政', '王夫人', '贾赦', '邢夫人', 
               '史湘云', '探春', '春感司', '秋悲司']

goback_place = ['贾氏家塾', '大堂', '松鹤童子', '冯渊', '鬼卒']

qingan_places = ['贾政', '王夫人', '贾母', '贾赦', '邢夫人', '贾珍', 
                '尤老娘', '薛姨妈', '元春', '林如海', '贾夫人', '贾珠']

wenhao_places = ['金钏', '玉钏', '周姨娘', '赵姨娘', '贾环', '琥珀', 
                '贾琏', '平姑娘', '尤二姐', '巧姐', '小红', '彩云', '彩霞', 
                '赖大家', '周瑞家', '柳二家', '尤氏', '尤三姐', '贾蓉', 
                '秦可卿', '薛蟠', '夏金桂', '宝蟾', '薛蝌', '邢岫烟', '女仙', 
                '昭容', '李纨', '贾兰', '李纹', '李琦', '惜春', '侍书', '紫鹃', 
                '雪雁', '宝琴', '史湘云', '莺儿', '翠缕', '袭人', '麝月', 
                '晴雯', ' 秋雯', '碧痕', '迎春', '司棋', '探春', '入画']

juhe_places = ['大观园', '天台', '曲径通幽', '采莲舟', '蓬莱仙境', '绛珠宫', '赤霞宫']

nianxiang_places = ['小终南', '大荒山', '青埂峰', '空洞', 
                    '栊翠庵', '大主山', '城隍庙', '散花寺']

losemoney_places = ['板儿', '文官', '龄官', '芳官', '藕官', '蕊官', '药官', 
                    '葵官', '艾官', '豆官', '沁芳桥', '女尼', '茶棚']

calldice_places = ['贾母', '元春', ('栊翠庵', 5), ('薄司命', 2), 
                    ('痴情司', 2), ('结怨司', 5), ('朝啼司', 3), ('暮哭司', 3)]

# 停一轮
# 贾政 王夫人 贾赦 邢夫人 史湘云 探春 春感司 秋悲司

# 退回本位 罚回本位
# 贾氏家塾 大堂 松鹤童子 冯渊 鬼卒

# 请安
# 贾政 王夫人 贾母 贾赦 邢夫人 贾珍 尤老娘 薛姨妈 元春 林如海 贾夫人 贾珠

# 问好
# 金钏 玉钏 周姨娘 赵姨娘 贾环 琥珀 贾琏 平姑娘 尤二姐 巧姐 小红 彩云 彩霞 赖大家 周瑞家 柳二家 尤氏 尤三姐 贾蓉 秦可卿 薛蟠 夏金桂 宝蟾 薛蝌 邢岫烟 女仙 昭容 李纨 贾兰 李纹 李琦 惜春 侍书 紫鹃 雪雁 宝琴 史湘云 莺儿 翠缕 袭人 麝月 晴雯 秋雯 碧痕 迎春 司棋 探春 入画

# 举贺
# 大观园 天台 曲径通幽 采莲舟 蓬莱仙境 绛珠宫 赤霞宫

# 拈香
# 小终南 大荒山 青埂峰 空洞 栊翠庵 大主山 城隍庙 散花寺

# 糖钱 赏赐 捐资 布施
# 板儿 文官 龄官 芳官 藕官 蕊官 药官 葵官 艾官 豆官 沁芳桥 女尼 茶棚

# 谒师
# 贾氏家塾 茫茫大士 渺渺真人