#include <iostream>

using namespace std;

int main() {
	cout << "----------------------------------------"<< endl;
	cout << "-----------LUAS LAYANG-LAYANG-----------"<< endl;
	cout << "---------KELILING LAYANG-LAYANG---------"<< endl;
	cout << "----------------------------------------"<< endl;
	
	int d1,d2,luas;
	int s1,s2,keliling;
	cout <<"Silahkan Masukan Nilai Diagonal Pertama: ";
	cin >>d1;
	cout <<"Silahkan Masukan Nilai Diagonal Kedua: ";
	cin >>d2;
	cout <<"Silahkan Masukan Sisi Pertama: ";
	cin >>s1;
	cout <<"Silahkan Masukan Sisi Kedua: ";
	cin >>s2;

	luas= 0.5*d1*d2;
	keliling= 2*(s1+s2);
	
	cout<<"Hasil dari luas layang-layang : "<<luas<<endl;
	cout<<"Hasil dari kelilinglayang-layang : "<<keliling<<endl;
	
	return 0;
}
