#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	cin >> s;

	int arr[26];
	for (int i = 0; i < 26; i++)
		arr[i] = -1;
	
	for (int i = 0; i < s.length(); i++)
	{
		int to_asc = int(s[i]) - int('a');
		if (arr[to_asc] == -1)
			arr[to_asc] = i;
		
	}

	for (int i = 0; i < 26; i++)
		cout << arr[i] << " ";
}