class Mhs(object):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""

    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uang=us
    def __str__(self):
        s = self.nama + " " + str(self.NIM) + " " + self.kotaTinggal + " " + str(self.uang)
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uang
    
a0 = Mhs("Putri Siwi Utami", 146, "Slawi", 24000)
a1 = Mhs("Sevtika Ichitia", 158, "Serang", 25000)
a2 = Mhs("Nimas Woro P", 160, "Klaten", 26000)
a3 = Mhs("Anissa Ghoyatul", 135, "Boyolali", 27000)
a4= Mhs("Vioala Lovita", 163, "Boyolali", 28000)
a5 = Mhs("Safira",145 , "Madiun", 29000)
a6 = Mhs("Diah Ramadhani", 116, "Sragen", 30000)
a7 = Mhs("Anggit", 115, "Sragen", 31000)
a8 = Mhs("Hesti", 130, "Sumatra", 32000)
a9 = Mhs("Saidah", 162, "Batang", 33000)
a10 = Mhs("Nanang ", 157, "Sragen", 34000)

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

def mergeSort(A):
    #print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    #print("Menggabungkan",A)

def quickSort(A):
    quickSortBantu (A, 0, len(A)-1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah-1)
        quickSortBantu(A, titikBelah+1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal]

    penandakiri = awal + 1
    penandakanan = akhir

    selesai = False
    while not selesai:

        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1

        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1

        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

