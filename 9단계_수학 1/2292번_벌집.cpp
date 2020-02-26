#include <iostream>
using namespace std;

int main()
{
	int count = 1, start = 1, x;
	cin >> x;
	while (1)
	{
		if (x <= start + 6 * (count - 1))
			break;

		start += 6 * (count - 1);
		count++;
	}

	cout << count << endl;
}