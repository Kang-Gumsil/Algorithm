/* "OOXXOXXOOO"�� ���� OX������ ����� �ִ�. O�� ������ ���� ���̰�, X�� ������ Ʋ�� ���̴�. 
������ ���� ��� �� ������ ������ �� �������� ���ӵ� O�� ������ �ȴ�. 
���� ���, 10�� ������ ������ 3�� �ȴ�.

"OOXXOXXOOO"�� ������ 1+2+0+0+1+0+0+1+2+3 = 10���̴�.

OX������ ����� �־����� ��, ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.*/

// �ݺ��� ���� �ޱ�
// OX ��� �ޱ�
// ���߹迭�� OX ���� ���� ���ϱ�

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
