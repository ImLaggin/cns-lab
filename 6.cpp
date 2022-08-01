#include <bits/stdc++.h>
using namespace std;

int main(){
    int p, q;
    cout << "Enter p : ";
    cin >> p;
    cout << "Enter q : ";
    cin >> q;
    int n = p*q;
    int phin = (p-1)*(q-1);
    int e = 2;
    for(;e < phin; e++)
        if(__gcd(e,phin) == 1)
            break;
    int d = 1;
    while(d*e % phin != 1)
        d++;
    cout << "e : " << e << endl << "d : " << d << endl;
    int m;
    cout << "Enter m : ";
    cin >> m;
    int c = 1;
    for(int i = 1; i <= e; i++){
        c = (c*m) % n;
        //cout << c << endl;
    }
    cout << "Encrypted key : " << c << endl;
    int D = 1;
    for(int i = 1; i <= d; i++){
        D = (D*c) % n;
    }
    cout << "Decrypted key : " << D << endl;
    return 0;
}
