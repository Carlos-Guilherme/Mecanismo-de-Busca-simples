print('===============================================')
print('=-=-=-=-=-=-= \033[1;30mCENTRAL DOS LINKS\033[m =-=-=-=-=-=-=-=')
print('=================  \033[1;31mPython 3\033[m  ==================')
pesquisa = str.capitalize(input('Pesquise: '))

tags_de_busca = ('Elles Club', 'Hidori Rose', 'Letícia Shirayki')

links = (f'{tags_de_busca[0]}: #link',
         f'{tags_de_busca[1]}: #link', 
         f'{tags_de_busca[2]}: #link', )

def pesquisado(msg):
    if pesquisa in tags_de_busca[msg]:
        print('-='*40)
        print('Item encotrado: ')
        print()
        print(links[msg])
        print('-='*40)
        
pesquisado(0)
pesquisado(1)
pesquisado(2)
