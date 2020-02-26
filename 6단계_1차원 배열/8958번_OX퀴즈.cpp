/* "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.*/

// 반복할 숫자 받기
// OX 결과 받기
// 이중배열로 OX 점수 세서 더하기

#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string str;
		int score = 0;

		cin >> str;

		for (int i = 0; i < str.length(); i++)
		{
			if (str[i] == 'O')
			{
				int temp_score = 0;
				for (int j = 0; j <= i; j++)
				{
					if (str[j] == 'O')
						temp_score++;

					else if (str[j] == 'X')
						temp_score = 0;
				}
				score += temp_score;
			}
		}
		cout << score << endl;
	}
}
