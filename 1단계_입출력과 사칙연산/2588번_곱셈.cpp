#include <iostream>
using namespace std;

int main()
{
	int in1, in2;
	int out1, out2, out3, out4;

	cin >> in1 >> in2;

	out1 = in2 % 10 * in1;
	out2 = in2 % 100 / 10 * in1;
	out3 = in2 / 100 * in1;
	
	out4 = out1 + out2 * 10 + out3 * 100;

	cout << out1 << endl;
	cout << out2 << endl;
	cout << out3 << endl;
	cout << out4 << endl;
}