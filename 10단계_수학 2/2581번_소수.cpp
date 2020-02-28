#include <iostream>
using namespace std;

int main()
{
	int M, N, sum = 0, min;
	bool exist = false;

	cin >> M >> N;

	for (int i = M; i <= N; i++)
	{
		bool sosu = true;
		for (int j = 2; j * j <= i; j++) 
		{
			if (i % j == 0)
			{
				sosu = false;
				break;
			}
		}
		if (i > 1 && sosu == true)
		{
			if (exist == false) // 첫 소수 -> 최솟값
				min = i;
			exist = true;
			sum += i;
		}
	}

	if (exist == true)
		cout << sum << endl << min << endl;
	else
		cout << -1 << endl;
}