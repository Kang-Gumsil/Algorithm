#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	cin >> s;
	int count[26] = { 0, };
	int len = s.length();

	for (int i = 0; i < len; i++)
	{
		int index = toupper(s[i]) - 'A';
		count[index]++;
	}
	
	int max = 0, max_index;
	bool ismul = false;

	for (int i = 0; i < 26; i++)
	{
		if (count[i] > max)
		{
			max = count[i];
			max_index = i;
			ismul = false;
		}

		else if (count[i] == max)
			ismul = true;
	}

	if (ismul == true)
		cout << "?" << endl;
	else
		cout << (char)(max_index + 'A') << endl;

}