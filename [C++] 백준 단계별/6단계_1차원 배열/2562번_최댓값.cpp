/* 9���� ���� �ٸ� �ڿ����� �־��� ��, �̵� �� �ִ��� ã�� �� �ִ��� �� ��° �������� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

���� ���, ���� �ٸ� 9���� �ڿ���
3, 29, 38, 12, 57, 74, 40, 85, 61
�� �־�����, �̵� �� �ִ��� 85�̰�, �� ���� 8��° ���̴�.*/

#include <iostream>
using namespace std;

int main()
{
	int max_index = 0, * arr = new int[9];

	for (int i = 0; i < 9; i++)
	{
		cin >> arr[i];
		if (arr[i] > arr[max_index])
			max_index = i;
	}

	cout << arr[max_index] << endl;
	cout << max_index+1 << endl;
}