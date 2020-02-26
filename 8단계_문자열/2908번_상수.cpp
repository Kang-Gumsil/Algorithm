#include <iostream>
using namespace std;

int main()
{
	int num[2], max;
	for (int i = 0; i < 2; i++)
	{
		cin >> num[i];
		num[i] = num[i] % 10 * 100 + num[i] % 100 / 10 * 10 + num[i] / 100;
	}

	cout << (num[0] > num[1] ? num[0] : num[1]) << endl;	
}