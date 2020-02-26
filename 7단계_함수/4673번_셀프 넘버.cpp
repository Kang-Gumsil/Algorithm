#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	bool arr[10001] = { false, };
	for (int i = 1; i <= 10000; i++)
	{
		int temp = i;
		int res = temp + temp % 10; // 일의 자리

		if (temp >= 10) { // 십의 자리
			temp = temp / 10;
			res += temp % 10;

			if (temp >= 10) { // 백의 자리
				temp = temp / 10;
				res += temp % 10;

				if (temp >= 10) { // 천의 자리
					temp = temp / 10;
					res += temp % 10;
				}
			}
		}

		if (res <= 10000)
			arr[res] = true;

	}

	for (int i = 1; i <= 10000; i++)
		if (arr[i] == false)
			printf("%d\n", i);
}