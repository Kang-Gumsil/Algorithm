#include <iostream>
using namespace std;

int main()
{
	bool arr[42] = { false, };
	int count = 0;

	for (int i = 0; i < 10; i++)
	{
		int temp;
		cin >> temp;
		arr[temp % 42] = true;	
	}

	for (int i = 0; i < 42; i++)
	{
		if (arr[i] == true)
			count++;
	}

	cout << count << endl;
}


int main()
{
	int arr[10];
	int count = 0;

	for (int i = 0; i < 10; i++)
	{
		cin >> arr[i];
		arr[i] = arr[i] % 42;
	}

	for (int i = 0; i < 10; i++)
	{
		bool isin = false;

		for (int j = 0; j < i; j++)
		{
			if (arr[i] == arr[j])
			{
				isin = true;
				break;
			}
		}

		if (isin == false)
			count++;
	}

	cout << count << endl;
}