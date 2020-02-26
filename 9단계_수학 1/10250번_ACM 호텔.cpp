#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++)
	{
		int W, H, N;
		cin >> H >> W >> N;

		if ((N - 1) / H + 1 < 10)
			cout << (N - 1) % H + 1 << "0" << (N - 1) / H + 1 << endl;
		else
			cout << (N - 1) % H + 1 << (N - 1) / H + 1 << endl;
	}
}