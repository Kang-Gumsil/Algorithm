#include <iostream>
using namespace std;

int main()
{
	int N, count = 0; 
	cin >> N; // 1000���� ���ų� ���� �ڿ���
	
	for (int i = 1; i <= N; i++)
	{
		if (i < 100) // 100 ���ϴ� ��� �� ��
			count++;

		else if (i < 1000) { // 100~999, 1000�� �Ѽ�X
			int num_1 = i % 10;
			int num_10 = i / 10 % 10;
			int num_100 = i / 100 % 10;

			if ((num_10 - num_1 == num_100 - num_10) || (num_1 - num_10 == num_10 - num_100))
				count++;
		}
	}

	cout << count << endl;
}