/* 입력

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. */

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