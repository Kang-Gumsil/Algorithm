#include <iostream>
using namespace std;

int main()
{
	int N, count = 0;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		int num;
		bool sosu = true;

		cin >> num;

		for (int j = 2; j < num; j++)
		{
			if (num % j == 0)
			{
				sosu = false;
				break;
			}
		}
		
		if (num > 1 && sosu == true)
			count++;
	}

	cout << count << endl;
}