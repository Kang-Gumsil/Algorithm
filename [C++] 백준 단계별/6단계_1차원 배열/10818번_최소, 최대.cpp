// N���� ������ �־�����. �̶�, �ּڰ��� �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
#include <iostream>
using namespace std;

int main()
{
	int num;
	cin >> num;

	int* arr = new int[num];
	
	for (int i = 0; i < num; i++)
		cin >> arr[i];

	int max = arr[0], min = arr[0];

	for (int i = 1; i < num; i++)
	{
		if (arr[i] > max)
			max = arr[i];
		if (arr[i] < min)
			min = arr[i];
	}

	cout << min << " " << max << endl;
	
}