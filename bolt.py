

def ertek(darab):
    if darab == 0:
        return 0
    elif darab == 1:
        return 1000
    elif darab == 2:
        return 1000 + 900
    else:
        return (darab - 2) * 800 + 1500


vásárlások = []
vásárlás = {}

class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> None:
        print("elso feladat:")
        forrásfájl = open('penztar.txt')
        for sor in forrásfájl:
            sor = sor.strip()
            if sor == 'F':
                vásárlások.append(vásárlás)
                vásárlás = {}
            else:
                vásárlás[sor] = vásárlás.get(sor, 0) + 1
        forrásfájl.close()
        pass

    def feladat_2(self) -> None:
        print("masodik feladat\nA fizetesek szama:", len(vásárlások))
        pass

    def feladat_3(self) -> None:
        vásárlás_sorszáma = int(input("harmadik feladat: vasarlas sorszama "))
        árucikk_neve = input('Adja meg egy árucikk nevét! ')
        vásárolt_darabszám = int(input('Adja meg a vásárolt darabszámot! '))
        print(vásárolt_darabszám, ' darab vételekor fizetendő: ', ertek(vásárolt_darabszám), sep='')
        pass

    def feladat_4(self, árucikk_neve=None) -> None:
        vettek_ilyet = [index + 1 for index, vásárlás in enumerate(vásárlások) if árucikk_neve in vásárlás.keys()]

        print("negyedik feladat:", vettek_ilyet[0], '\nAz utolsó vásárlás sorszáma: ',
              vettek_ilyet[-1],
              '\n', len(vettek_ilyet), ' vásárlás során vettek belőle.', sep='')
        pass

    def feladat_5(self, filepath: str) -> None:
        print("otodik feladat")
        célfájl = open('osszeg.txt', 'w')
        for index, vásárlás in enumerate(vásárlások):
            print(index + 1, ': ', sum(map(ertek, vásárlás.values())), sep='', file=célfájl)
        pass
