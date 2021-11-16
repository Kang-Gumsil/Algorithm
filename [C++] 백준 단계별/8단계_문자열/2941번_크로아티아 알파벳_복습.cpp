#include <iostream>
#include <string>
using namespace std;

int main()
{
    string list[] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
    string str;

    cin >> str;

    for (int i = 0; i < 8; i++)
    {
        int index;
        while ((index = str.find(list[i])) != -1)
            str.replace(index, list[i].length(), "a");
    }

    cout << str.length() << endl;

}