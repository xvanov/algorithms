
class BinaryTree:
    def __init__( self, n ):
        self.root = None
        self.N = n
        self.key = [ None  for x in range(n)]
        self.left = [ None  for x in range(n)]
        self.right = [ None  for x in range(n)]
        self.parent = [ None  for x in range(n)]

    def addNode( self, nodeLabel, nodeKey ):
        self.key[nodeLabel] = nodeKey

    def addEdge( self, parentLabel, childLabel, isLeft ):
        if isLeft: self.left[parentLabel] = childLabel
        else:      self.right[parentLabel] = childLabel
        self.parent[childLabel] = parentLabel

    def print( self ):
        for i in range(0, self.N):
            print( str(i) + " (" + str(self.key[i]) + ")" + \
              "  L: (" + str(self.left[i]) + ")" + \
              "  R: (" + str(self.right[i]) + ")" + \
              "  P: (" + str(self.parent[i]) +  ")" )

    def listInOrder( self, nodeLabel ):
        leftChild = self.left[nodeLabel]
        if leftChild != None:  self.listInOrder( leftChild )
        print( self.key[nodeLabel], "", end = "" )
        rightChild = self.right[nodeLabel]
        if rightChild != None:  self.listInOrder( rightChild )

# ............................................................................
#                               M A I N
# ............................................................................

binTree = BinaryTree( 10 )


for i in range (0, binTree.N ):
    binTree.addNode( i, i*10 )

binTree.print()

for i in range (0, binTree.N ):
    if i*2+1 < binTree.N:
        binTree.addEdge( i, i*2+1, True )
    if i*2+2 < binTree.N:
        binTree.addEdge( i, i*2+2, False )

print()
binTree.print()
binTree.listInOrder( 0 )

'''

Ahoj,

do nasi aktualni ucebny se vejde asi 48 lidi, takze bychom se asi vesli,
bylo by nutno natahat prodluzovacky, protoze zasuvky na proud jsou jen
po jedne strane mistnosti pod okny, takze ti, co sedi dale od okna
(u dveri),  by tam nedoshli svymi beznymi kabely.
Ted mam asi 30 lidi, ale pocitam, ze jeste par ubyde.

Druha varianta je pocitacova ucebna 404, ktera ma cca 60 mist,
pocitace i obrazovky, ale zas spravcove se tam boji pripojeni
studentskych NB k el. zdrojum, protoze by nevydrzely pojistky,
cela budova by shorela v jednom oslnujicim zablesku
a CVUT beze stopy zaniklo, coz nechteji. Pokud by tam byli
schopni/ochotni instalovat nejaky trivialni system
s par prekladaci a browserem (coz asi dokazou), tak
by se to vyuzit celkem v poho dalo, jiz jsme tam takto delali
programovaci zkousky v povinnych predmetech, a jen tu a tam si
zavislaci museli prinest vlastni klavesnici...

Tento tyden bychom to uz asi nestihli, beztak jsme teprve po
zakladnim rozjezdu. Pokud ale domluvime termin(y) dopredu, tak
odhaduju, ze uz bychom to dokazali organizacne zajistit.
Jeste tam dnes/zitra zkontroluju tu pocitacovnu, a jestli
jeste stoji, tak bych to pokladal celkem za hotovou vec,
v nejhorsim bych musel jen na ty spravce tlacit pres vedouciho
katedry, ale to snad nebude nutne, kdyz se vse dojedna v predstihu.

Navrhuju, abychom se predbezne domluvili na terminu, pak
se pokusim ziskat tu ucebnu. Kdyby s tim byly problemy, tak
se ozvu a budem hledat nahradni variantu, jinak to posleze proste
pouzijem a bude.

Ty terminy, co jsem psal,
22.3., 5.4., 19.4., 3.5., 17.5.
se nam hodi nejlepe, ale zbyle ctvrtky
15.3., 29.3., 12.4., 26.4., 10.5., 24.5.
jsou pouzitelne taky (jen bych trosku zprehazel nas rozvrh, lec to je OK).
Dne 17.5. je na FEL uterni rozvrh, to by mozna nekteri ucastnici
meli kolizi, ze by treba nestihali zacatek apod., takze toto
datum bych predbezne castecne upozadoval, ostatni jsou asi v poho.

M.







----- Message from Tomas Valla <tomas.valla@fit.cvut.cz> ---------
   Date: Sat, 3 Mar 2018 14:21:05 +0100
   From: Tomas Valla <tomas.valla@fit.cvut.cz>
Subject: Re: Synchonizace ACM terninku?
     To: berezovs@fel.cvut.cz


> Ahoj Marko,
>
>> my tedy mame seminar ve ctvrtek od 16:15 v Dejvicich.
>
> a kde presne a jak je velka?
> Nas tentokrat z neznamych duvodu soupli z 3. patra nove budovy do
> pocitacove ucebny, ktera se nachazi v NTK (tusim taky 3. patro).
> Moc radost z toho nemam, sice nam staci, ale trochu se obavam, ze az tam
> budeme chtit delat velky trenink, ze narazime. Konkretne, neni tak
> velka, jako ta obri mistnost co jsme meli k dispozici, ale hlavne nejde
> uplne snadno posedat si venku pred tu ucebnu (je tam nejaky tichy
> rezim). Taky mozna bude problem domluvit, aby nam tam zaridili specialni
> guest ucty.
>
> Nicmene, takovych 40 lidi se tam podle me vleze.
>
>> Dali nam ucebnu bez skolnich stroju, takze je nutno mit vlastni NB
>> a pripadne kdo ma slabou baterku, musi si vzit prodluzovacku.
>> Ale jinak je tam mista snad dost.
>
> Takze myslis, ze ta vase mistnost je na spolecne treninky lepsi?
>
>> Tento tyden jeste budu cekat nez se ustali osazenstvo,
>> nekteri typicky na zacatku odpadnou.
>
> Jasne. Kolik lidi ti tam tak tedy chodi?
>
>> Potom bychom jiz mohli poradat spolecne podniky, vzasade nejsme omezeni,
>> jen by
>> nam vic vyhovovaly ctvrtky tzv. sude, to jest za tyden, za 3 tydny atd.
>> 8.3., 22.3., 5.4., 19.4., 3.5., 17.5.
>>
>> Napis tedy, jak na tom jste, abychom mohli dohodnout predbezne
>> nejake terminy.
>
> Super. Zkusim probrat jeste s ostatnimi kluky, kteri pomahaji s
> treninkem, jak to vidi oni a dam co nejdriv vedet.
>
> Taky asi rovnou napisu klukum z matfyzu, jestli by meli nekdy zajem
> prijit oni.
>
> Diky a mej se fajn,
> Tomas


----- End message from Tomas Valla <tomas.valla@fit.cvut.cz> -----

'''

