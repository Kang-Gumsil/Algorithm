#include <iostream>
#include <string>
using namespace std;

int main()
{
	int num, count = 0;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		string s;
		cin >> s;
		int len = s.length();
		bool is = true;
		for (int j = 0; j < len; j++)
		{
			for (int k = j + 1; k < len; k++)
			{
				if (s[k] == s[j] && s[k - 1] != s[j])
					is = false;
			}
			if (is == false)
				break;
		}
		if (is == true)
			count++;
	}

	cout << count << endl;
}



int main()
{
	int num, count = 0;
	cin >> num;

	for (int i = 0; i < num; i++)
	{
		string s;
		cin >> s;
		bool is = true;
		int len = s.length();
		bool arr[26] = { false, };


		for (int j = 0; j < len; j++)
		{
			int ascii = s[j] - 'a';
			if (arr[ascii] == true && s[j - 1] != s[j]) 
			{
				is = false;
				break;
			}

			arr[ascii] = true;
		}

		if (is == true)
			count++;
	}

	cout << count << endl;
}