#include <iostream>
using namespace std;

int main()
{
	int a, b, c; 
	int arr[10] = { 0, };
	cin >> a >> b >> c;

	a = a * b * c; // 17037300

	while (1)
	{
		int temp = a % 10;  
		arr[temp]++;

		
		a = a / 10; 
		if (a < 1)
			break;
	}

	for (int i = 0; i < 10; i++)
		cout << arr[i] << endl;
}
