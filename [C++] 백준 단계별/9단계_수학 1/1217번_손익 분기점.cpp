#include <iostream>
using namespace std;

int main()
{
	double a, b, c;
	cin >> a >> b >> c;
	double rev = c - b;
	int count;

	if (b >= c) // ���ͺб����� �������� ����
		count = -1;
	else
		count = int(a / rev) + 1;

	cout << count << endl;
}