/* �Է�

ù° �ٿ��� �׽�Ʈ ���̽��� ���� C�� �־�����.
��° �ٺ��� �� �׽�Ʈ ���̽����� �л��� �� N(1 �� N �� 1000, N�� ����)�� ù ���� �־�����, �̾ N���� ������ �־�����. 
������ 0���� ũ�ų� ����, 100���� �۰ų� ���� �����̴�.

���

�� ���̽����� �� �پ� ����� �Ѵ� �л����� ������ �ݿø��Ͽ� �Ҽ��� ��° �ڸ����� ����Ѵ�. */

#include <iostream>
using namespace std;

int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++)
	{
		int num_student, sum = 0;
		cin >> num_student;

		int* scores = new int[num_student];
		for (int j = 0; j < num_student; j++)
		{
			cin >> scores[j];
			sum += scores[j];
		}

		float ave = (float)sum / num_student;
		int count = 0;
		for (int j = 0; j < num_student; j++)
			if (scores[j] > ave)
				count++;

		cout << fixed;
		cout.precision(3);
		cout << float(count) / num_student * 100 << "%" << endl;
	}
}