#include <iostream>
using namespace std;


bool f1(int &x){ x+=1; return false; }
bool f2(int &x){ x+=10; return true; }
bool f3(int &x){ x+=2; return false; }

int main(){
    int x = 1;
    bool result = f1(x) || f2(x) && f3(x);
    cout << x;
}




