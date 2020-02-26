#include <iostream>
using namespace std;

int main()
{
	while (1)
	{
		int a, b;
		cin >> a >> b;

		if (cin.eof())
			break;

		else
			cout << a + b << endl;
	}
}