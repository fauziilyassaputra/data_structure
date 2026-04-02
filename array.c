Bagian A :

#include

int main() {

int nilai[] = {10,20,30,40,50};

printf("%d\n", nilai[1]);

nilai[2] = 999;

int panjang_nilai = sizeof(nilai) / sizeof(nilai[0]);

for (int x = 0; x < panjang_nilai; x++){

printf("%d\n", nilai[x]);

}

return 0;

}

Bagian B :

// Online C compiler to run C program online

#include

int main() {

int nilai_matriks[3][3] = {

{1,2,3},

{4,5,6},

{7,8,9}

};

int panjangbaris = sizeof(nilaimatriks) / sizeof(nilai_matriks[0]);

int panjangkolom = sizeof(nilaimatriks[0]) / sizeof(nilai_matriks[0][0]);

for (int x = 0; x < panjang_baris; x++){

for (int y = 0; y < panjang_kolom; y++){

printf("%d", nilai_matriks[x][y]);

}

printf("\n");

}

return 0;

}
