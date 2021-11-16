#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	if (a > b)
	{
		if (a > c)
		{
			if (b > c) cout << b;
			else cout << c;
		}
		else cout << a;
	}

	else // b > a
	{
		if (a > c) cout << a;
		else // b>a && c>a 
		{
			if (b > c) cout << c;
			else cout << b;
		}
	}
}