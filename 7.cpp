#include <bits/stdc++.h>
using namespace std;

int main(){
    int q, a, xa, xb;
    cout << "Enter q : ";
    cin >> q;
    cout << "Enter a : ";
    cin >> a;
    cout << "Enter Xa and Xb : ";
    cin >> xa >> xb;
    int ya = 1, yb = 1;
    for(int i = 1; i <= xa; i++)
        ya = (ya*a) % q;
    for(int i = 1; i <= xb; i++)
        yb = (yb*a) % q;
    cout << "Ya : " << ya << endl << "Yb : " << yb << endl;
    int ka = 1, kb = 1;
    for(int i = 1; i <= xa; i++)
        ka = (ka*yb) % q;
    for(int i = 1; i <= xb; i++)
        kb = (kb*ya) % q;
    cout << "Ka : " << ka << endl << "Kb : " << kb << endl;
    return 0;
}
