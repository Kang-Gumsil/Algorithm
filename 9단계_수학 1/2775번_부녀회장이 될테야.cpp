#include <iostream>
using namespace std;

int f(int k, int n)
{
	int count = 0;

	if (k == 0)
		return n;

	for (int i = 1; i <= n; i++)
		count += f(k - 1, i);

	return count;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int k, n;
		cin >> k >> n;
		cout << f(k, n) << endl;
	}
}

