#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	bool arr[10001] = { false, };
	for (int i = 1; i <= 10000; i++)
	{
		int temp = i;
		int res = temp + temp % 10; // ���� �ڸ�

		if (temp >= 10) { // ���� �ڸ�
			temp = temp / 10;
			res += temp % 10;

			if (temp >= 10) { // ���� �ڸ�
				temp = temp / 10;
				res += temp % 10;

				if (temp >= 10) { // õ�� �ڸ�
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