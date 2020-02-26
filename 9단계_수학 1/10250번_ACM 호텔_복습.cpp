#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int H, W, N, y, x;
        cin >> H >> W >> N;

        y = (N - 1) % H + 1;
        x = (N - 1) / H + 1;

        if (x < 10)
            cout << y << "0" << x << endl;
        else
            cout << y << x << endl;
    }
}