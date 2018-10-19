def cekKamus(kata, kamus_arr):
    hasilCari = 0
    if (kata in kamus_arr):
        hasilCari = 1
    return hasilCari


# -------------------------------------
# POTONG KATA YANG BERAWALAN ME ATAU PE
# -------------------------------------

def potongAwalanMe(kata):
    _2hurufAwal = kata[:2]
    _3hurufAwal = kata[:3]
    _4hurufAwal = kata[:4]

    awalan = ""
    hurufPengganti = ""

    if (_4hurufAwal == "meng" or _4hurufAwal == "peng"):
        # hasil yang dipotong tambahkan dengan salah satu huruf berikut ini
        # hurufPengganti = ['v', 'k', 'g', 'h', 'q'];

        awalan = _4hurufAwal

    elif (_4hurufAwal == "meny" or _4hurufAwal == "peny"):
        # awalan = _4hurufAwal[:2]
        awalan = _4hurufAwal
        # hurufPengganti = ['s']

    elif (_3hurufAwal == "mem" or _3hurufAwal == "pem"):
        awalan = _3hurufAwal
        # hurufPengganti = ['b','f','p','v']

    elif (_3hurufAwal == "men" or _3hurufAwal == "pen"):
        awalan = _3hurufAwal
        # hurufPengganti = ['c','d','j','s','t','z']

    elif (_3hurufAwal == "per"):
        awalan = _3hurufAwal
        # hurufPengganti = ['c','d','j','s','t','z']

    elif (_2hurufAwal == "me" or _2hurufAwal == "pe"):
        awalan = _2hurufAwal
        # hurufPengganti = ['l','m','n','r','y','w']

    return awalan
    # return awalan+" "+hurufPengganti


# -------------------------------------
# POTONG KATA YANG BERAWALAN ME ATAU BE
# -------------------------------------

def potongAwalanBe(kata):
    _2hurufAwal = kata[:2]
    _3hurufAwal = kata[:3]

    awalan = ""
    hurufPengganti = ""

    if (_3hurufAwal == "ber"):
        awalan = _3hurufAwal

    elif (_2hurufAwal == "be" and kata == "bekerja"):
        awalan = _2hurufAwal

    elif (_3hurufAwal == "bel" and kata == "belajar"):
        awalan = _3hurufAwal

    return awalan
    # return awalan +" "+hurufPengganti


# -------------------------------------
# POTONG KATA YANG BERAWALAN SELAIN ME,PE,BE
# -------------------------------------

def potonganAwalanLainnya(kata):
    awalan = ""
    awalanLain = ["di", "ke", "ku", "se"]
    hurufPengganti = ""

    _2hurufPengganti = kata[:2]
    _3hurufPengganti = kata[:3]

    if (_3hurufPengganti == "ter"):
        # hurufPengganti = ["r"]
        awalan = _3hurufPengganti
    elif (_2hurufPengganti in awalanLain):
        awalan = _2hurufPengganti

    return awalan
    # return awalan +" "+hurufPengganti


# -------------------------------------
# POTONGAN AWALAN
# -------------------------------------

def potonganAwalan(kata):
    # jadikan huruf kecil semua
    kata = kata.lower()
    awalan1 = ["me", "di", "ke", "pe", "se", "be"]
    awalan2 = ["ber", "ter", "per"]

    _2hurufAwal = kata[:2]
    awalan = ["", ""]

    for x in range(2):
        awalanTemp = ""

        if (_2hurufAwal == "me" or _2hurufAwal == "pe"):
            awalanTemp = potongAwalanMe(kata)
        elif (_2hurufAwal == "be"):
            awalanTemp = potongAwalanBe(kata)
        else:
            awalanTemp = potonganAwalanLainnya(kata)

        if (awalanTemp != ""):
            pjgAwalan = len(awalanTemp)
            kata = kata[pjgAwalan:]

            _2hurufAwal = kata[:2]

            if (awalanTemp in awalan2):
                # JIKA AWLAN1 SUDAH ADA ISINYA MASUKAN KE AWALAN1
                # if(awalan1 != ""):
                #     awalan0 = awalanTemp
                # else:
                awalan = awalanTemp

            else:
                if (awalan == ""):
                    awalan[0] = awalanTemp
                else:
                    awalan[1] = awalanTemp

    return awalan


def potonganAkhiran(kata):
    kata = kata.lower()

    akhiran1 = ["lah", "kah", "pun", "tah"]
    akhiran2 = ["ku", "mu", "nya"]
    akhiran3 = ["i", "an", "kan"]

    akhir = ["", "", ""]

    _3hurufAkhir = kata[len(kata) - 3:]
    _2hurufAkhir = kata[len(kata) - 2:]
    _1hurufAkhir = kata[len(kata) - 1:]

    for i in range(3):
        if (i == 0):
            if (_3hurufAkhir in akhiran1):
                akhir[i] = _3hurufAkhir

                kata = kata[len(kata) - 3:]

                _3hurufAkhir = kata[len(kata) - 3:]
                _2hurufAkhir = kata[len(kata) - 2:]
                _1hurufAkhir = kata[len(kata) - 1:]

        elif (i == 1):
            if (_3hurufAkhir in akhiran2):
                akhir[i] = _3hurufAkhir

                kata = kata[len(kata) - 3:]

                _3hurufAkhir = kata[len(kata) - 3:]
                _2hurufAkhir = kata[len(kata) - 2:]
                _1hurufAkhir = kata[len(kata) - 1:]

            elif (_2hurufAkhir in akhiran2):
                akhir[i] = _2hurufAkhir

                kata = kata[len(kata) - 2:]

                _3hurufAkhir = kata[len(kata) - 3:]
                _2hurufAkhir = kata[len(kata) - 2:]
                _1hurufAkhir = kata[len(kata) - 1:]
        else:
            if (_3hurufAkhir in akhiran3):
                akhir[i] = _3hurufAkhir
            elif (_2hurufAkhir in akhiran3):
                akhir[i] = _2hurufAkhir
            elif (_1hurufAkhir in akhiran3):
                akhir[i] = _1hurufAkhir

    return akhir


def cariKataDasar(kata):
    awalan = potonganAwalan(kata)
    akhiran = potonganAkhiran(kata)

    panjang2awalan = len(awalan[0]) + len(awalan[1])
    panjang3akhiran = len(akhiran[0]) + len(akhiran[1]) + len(akhiran[2])

    if (panjang2awalan == 0):
        kataDasar = kata[:-panjang3akhiran]
    elif (panjang3akhiran == 0):
        kataDasar = kata[panjang2awalan:]
    else:
        kataDasar = kata[panjang2awalan:-panjang3akhiran]

    return kataDasar


def stemmingArifin(kata,kamus):
    # -------------------------------------
    # ASUMSIKAN BENTUK KATA ADALAH AW 1 + AW 2 + KD +AKH 3 + AKH 2 + AKH 1
    # -------------------------------------
    # -------------------------------------
    # CEK APAKAH ADA DALAM KAMUS
    # -------------------------------------

    if(kata in kamus):
        return kata

    else:
        # -------------------------------------
        # HASILKAN AWALAN, AKHIRAN DAN KATA DASAR PERIKSA APAKAH TELAH
        # DITEMUKAN , ASUMSINYA KATA SELALU MEMILIKI SUSUNAN SEBAGAI BERIKUT
        # AW I + AW II + KD + AKH III + AKH II + AKH I
        # -------------------------------------
        awalan = potonganAwalan(kata)
        akhiran = potonganAkhiran(kata)

        panjang2awalan = (len(awalan[0]) + len(awalan[1]))
        panjang3akhiran = (len(akhiran[0]) + len(akhiran[1]) + len(akhiran[2]))


        if (panjang2awalan == 0):
            kataDasar = kata[:-panjang3akhiran]
        elif (panjang3akhiran == 0):
            kataDasar = kata[panjang2awalan:]
        else:
            kataDasar = kata[panjang2awalan:-panjang3akhiran]

        _2hurufAwalan = awalan[0][:2]
        _2hurufAkhirAwalan = awalan[0][:-2]
        _1hurufAkhitAwalan = awalan[0][:-1]


        if(_2hurufAkhirAwalan == "ng"):
            # UNTUK KATA SEPERTI KONTAK, KANTUK AKAN DILEBUR MENJADI MENGANTUK
            # TAMBAHKAN HURUF K

            tempKataDasar = "k"+kataDasar

            if(cekKamus(tempKataDasar,kamus)):
                return tempKataDasar

        if(_2hurufAkhirAwalan =="ny"):
            # TAMBAHKAN HURUF S

            tempKataDasar = "s"+kataDasar

            if(cekKamus(tempKataDasar,kamus)):
                return tempKataDasar

        if(_1hurufAkhitAwalan == "n"):
            # TAMBAHKAN DENGAN HURUF T
            tempKataDasar = "t"+kataDasar

            if(cekKamus(tempKataDasar, kamus)):
                return tempKataDasar


        # AW II.KD.AKH III.AKH II.AKHI
        tempKataDasar = awalan[1]+kataDasar+akhiran[2]+akhiran[1]+akhiran[0]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        # KD + AK III + AK II + AK I
        tempKataDasar = kataDasar+akhiran[2]+akhiran[1]+akhiran[0]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #KD + AK III + AK II
        tempKataDasar = kataDasar+akhiran[2]+akhiran[1]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #KD + AK III
        tempKataDasar = kataDasar+akhiran[2]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #KD
        if(cekKamus(kataDasar,kamus)):
            return kataDasar

        #AW I.KD
        tempKataDasar = awalan[0]+kataDasar
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #AW I.AW II.KD
        tempKataDasar = awalan[0]+awalan[1]+kataDasar
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #AW I.AW II.KD.AKH III
        tempKataDasar = awalan[0]+awalan[1]+kataDasar+akhiran[2]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        #AW I.AW II.KD.AKH III.AKH II
        tempKataDasar = awalan[0]+awalan[1]+kataDasar+akhiran[2]+akhiran[1]
        if(cekKamus(tempKataDasar,kamus)):
            return tempKataDasar

        # AW I.AW II.KD.AKH III.AKH II.AKH I
        tempKataDasar = awalan[0] + awalan[1] + kataDasar + akhiran[2] + akhiran[1] +akhiran[0]
        if (cekKamus(tempKataDasar, kamus)):
            return tempKataDasar

        # KATA SEBELUM PEMOTONGAN

        # AW II.KD
        tempKataDasar = awalan[1]+kataDasar
        if (cekKamus(tempKataDasar, kamus)):
            return tempKataDasar

        # AW II.KD.AKH III
        tempKataDasar = awalan[1] + kataDasar +akhiran[2]
        if (cekKamus(tempKataDasar, kamus)):
            return tempKataDasar

        # AW II.KD.AKH III.AKH II
        tempKataDasar = awalan[1] + kataDasar +akhiran[2] + akhiran[1]
        if (cekKamus(tempKataDasar, kamus)):
            return tempKataDasar

    return kata