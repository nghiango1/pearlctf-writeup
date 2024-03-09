from string import ascii_uppercase


def caesar_table():
    table = []

    for i in range(len(ascii_uppercase)):
        table.append([])  # Create row

        for j in range(i, len(ascii_uppercase)):
            table[i].append(ascii_uppercase[j])

        for j in range(0, i):
            table[i].append(ascii_uppercase[j])
    return table


def decrypt(key, encrypted, table):

    # SEARCH ELEMENTS
    _ki = -1  # Key Iterrator
    key_text = ''

    for i in range(len(encrypted)):
        # loop over key
        _ki = 0 if (_ki == len(key)-1) else (_ki + 1)

        if not encrypted[i].isalpha():
            key_text += encrypted[i]
            _ki -= 1
            pass

        column = ascii_uppercase.index(key[_ki].upper())

        # Find encrypted char in caesar table
        for j in range(len(ascii_uppercase)):
            if table[j][column] == encrypted[i].upper():
                key_text += table[j][0] if encrypted[i].isupper() else table[j][0].lower()

    print(key_text)


def encrypt(key, text, table):

    # CHANGE TEXT TO KEY TEXT
    key_text = ''
    x = -1

    for i in range(len(text)):
        # key length control
        x = 0 if (x == len(key)-1) else (x + 1)

        # Check is char must be in upper or lowercase
        _key_char = key[x].upper() if text[i].isupper() else key[x].lower()

        # Check special characters
        if text[i].isalpha():
            key_text += _key_char
        else:
            key_text += text[i]
            x -= 1

    # ENCRYPTION THE KEY_TEXT
    encrypted = ''

    for i in range(len(text)):
        # Locate letter in caesar table
        column = ascii_uppercase.index(
            text[i].upper()) if text[i].isalpha() else False
        row = ascii_uppercase.index(
            key_text[i].upper()) if key_text[i].isalpha() else False

        if column or row:
            encrypted += table[row][column] if key_text[i].isupper(
            ) else table[row][column].lower()
        else:
            encrypted += text[i]

    print(encrypted)


text = """Civvc Ihsce Gzgg Rtj Yp
Np'tx sd wtilpzjgw tf wqoj
Nsu byqp ywi rlwgl fch sf oq B
F uylc nqfrxxmvyv'l bwet Z'x vancoier qy Ddy wffnws'i kek ejbx uvod lpr tilei rwr N yysk hcgsp xecw ahz wsw Z'x
hxjamnx Rqmyp qabp ahz jrdvcumfch
Nvggk ldrnr rkoj nsu la Pxatv gfypt qtx yff fhbc
Rempt ztcra ifp twdynu lpw itweie ahz Civvc ihsce mrvg rtj grp
Ygojg koeyc lfn kofodrj
Civvc ihsce tvwn t qxi aeo jnwi col Hg'oj zrony gthw stypt ytg wo czpz
Ddyr ypcky'h fevy cvmxrg sfv rtj've kzq lmn xo jla by Xrszog pj qsty vphb llak'd dxjc kozyi hs
tzqo pdsdkft mr soyhzqyki zg xfqiqhzsqu
Wv vphb ile xlox fch wv'cg ztcra gwcr ni Enu th rtj esb xg atl M'm wpgenck
Dfy'v mjap mv jqn'wt xof mnbss xo jpg Gjkir xzpgf vmvv jqn ze
Rempt ztcra cpv rtj hony
Pxatv gfypt wjr aizwgi prd upuxwi col Ygojg koeyc ffzi yff ekd
Civvc ihsce srj ihtsfyv
Ygojg koeyc mjap a ctg tss luie ahz Civvc ihsce gzgg rtj yp
Epxxw vsnel nxy nsu uzyg
Stzei rqgsp vue lthzch aeo fxxtvt pzw Gjkir xzpgf bekv jqn hgc
Nvggk ldrnr dcr ldsdsjg
Gjkir xzpgf iilc l nbj prd yftm ddy Nvggk ldrnr rkoj, civvc ihsce gzgg (Znki yff wi)
(Tdl) Nvggk ldrnr rkoj, civvc ihsce gzgg (Znki yff wi)
"""

key = "PEARLCTF"
# encrypt(key, text, caesar_table())
decrypt(key, text, caesar_table())

next_stage = "evqx ebzyvbt vg qvtsvqhzg gb ibqrffgnbq"
_assumtion = "rick_rolling_is_difficult_to_understand"

key2 = "rickrollingisdifficulttounderstand"
key2 = "o"  # ..c. ..l..n. .s ..f..c.l. sn un..r...n.
key2 = "n"  # ri.k ro.li.g i. di.fi.u.t to ..de.sta.d
key2 = "nnonnnonnonnonnonnononnnoonnonnnon"  # ???

decrypt(key2, next_stage, caesar_table())
