#include <iostream>
using namespace std;

int main()
{
	string s;
	cin >> s;
	
	int len = s.length();
	int count = 0;
	for (int i = 0; i < len; i++)
	{
		if (s[i] >= 'a' && s[i] <= 'z')
			count++;

		if (i >= 2 && s[i] == '=' && s[i - 1] == 'z' && s[i - 2] == 'd')
			count--;

		if (i >= 1 && s[i] == 'j' && (s[i - 1] == 'l' || s[i - 1] == 'n'))
			count--;
	}

	cout << count << endl;
}