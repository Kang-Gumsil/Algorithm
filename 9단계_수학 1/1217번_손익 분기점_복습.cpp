#include <iostream>
using namespace std;

int main()
{
    int A, B, C, x;
    cin >> A >> B >> C;

    if (B >= C)
    {
        cout << -1 << endl;
        return 0;
    }

    x = A / (C - B) + 1;
    cout << x << endl;
}