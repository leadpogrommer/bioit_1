from ete3 import NCBITaxa, TreeStyle, TreeNode, AttrFace, TextFace

ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()

# First question
names = [
    'Homo sapiens', # Человек
    'Mus musculus', # Мышь
    'Lepidoptera',  # Бабочки и мотыльки
    'Saccharomyces cerevisiae',      # Пекарские дрожжи
    'Brassica oleracea',             # Капуста
    ]

human_names = [
    'Человек',
    'Мышь',
    'Бабочки',
    'Пекарские дрожжи',
    'Капуста', 
    ]

# Last question
names = [
    'Homo sapiens',
    'Caretta caretta',
    'Tyto alba',
    'Python bivittatus',
    'Pygoscelis adeliae',
    'Protopterus annectens',
    'Chrysemys picta bellii',
    'Bufo bufo',
    'Alligator sinensis',
    'Crocodylus porosus',
    'Latimeria chalumnae',
]
human_names = [
    'Человек разумный',
    'головастая черепаха',
    'Обыкновенная сипуха',
    'Тёмный тигровый питон',
    'Пингвин Адели',
    'Бурый протоптер',
    'Расписная черепаха',
    'Обыкновенная жаба',
    'Китайский аллигатор',
    'Гребнистый крокодил',
    'Latimeria chalumnae',
]

tax_ids = ncbi.get_name_translator(names)
id_russian = dict()
for key in tax_ids.keys():
    if len(tax_ids[key]) != 1:
        raise Exception(f'Not exactly one ID per search for {key}: {tax_ids[key]}')
    tax_ids[key] = tax_ids[key][0]
    id_russian[tax_ids[key]] = human_names[names.index(key)]

print(id_russian)

print(tax_ids)

def layout(node: TreeNode):
    if getattr(node, "rank", None):
        rank_face = AttrFace("rank", fsize=7, fgcolor="indianred")
        node.add_face(rank_face, column=0, position="branch-top")
    # if node.is_leaf():
    # tax_ids.items().
    if int(node.name) in id_russian.keys():
        node.add_face(
            TextFace(id_russian[int(node.name)]),
            column=0,
            position='branch-top',
        )
    sciname_face = AttrFace("sci_name", fsize=9, fgcolor="steelblue")
    node.add_face(sciname_face, column=0, position="branch-top")

tree = ncbi.get_topology(list(tax_ids.values()), intermediate_nodes=False)
ts = TreeStyle()
ts.show_leaf_name = True
ts.layout_fn=layout
ts.show_scale = False
print(tree.get_ascii())
tree.render('q2.png', tree_style=ts, w=800)