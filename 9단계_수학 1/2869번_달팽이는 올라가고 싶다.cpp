#include <iostream>
using namespace std;


int main()
{
	int V, A, B;
	cin >> A >> B >> V;

	if (A == V) {
		cout << "1" << endl;
		return 0;
	}
		

	int per_day = A - B;
	V -= A;

	// ������ 0 �̸��� �ƴ϶� 0 �����̱� ������ ���� �����ߵ�!!
	if (V % per_day == 0)
		cout << V / per_day + 1 << endl;
	else
		cout << V / per_day + 2 << endl;
	
}