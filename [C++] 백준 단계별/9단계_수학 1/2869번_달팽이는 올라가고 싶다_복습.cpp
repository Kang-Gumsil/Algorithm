#include <iostream>
using namespace std;

int main()
{
    int A, B, V, x;
    cin >> A >> B >> V;

    x = (V - B) / (A - B);

    if (((V - B) % (A - B)) == 0)
        cout << x << endl;
    else
        cout << x + 1 << endl;
}