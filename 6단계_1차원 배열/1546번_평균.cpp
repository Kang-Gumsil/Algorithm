#include  <iostream>
using namespace std;

int main()
{
	int n;
	float max = -1, sum = 0;
	
	cin >> n;
	float *arr = new float[n];

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
		if (arr[i] > max)
			max = arr[i];
	}

	for (int i = 0; i < n; i++)
		sum += arr[i] / max * 100.0f;

	cout << sum / n << endl;


}