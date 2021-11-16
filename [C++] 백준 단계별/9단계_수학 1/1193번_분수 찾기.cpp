#include <iostream>
using namespace std;

int main()
{
	int x, pre = 1, count = 2, m, n;
	cin >> x;

	if (x == 1) {
		cout << "1/1" << endl;
		return 0;
	}

	while (1) {
		if (x <= pre + count) {
			int total = count + 1;
			n = 1, m = total - 1;
			for (int cur = pre + 1;; cur++, n++, m--) {
				if (x == cur) {
					if (total % 2 == 0)
						cout << m << "/" << n << endl;
					else
						cout << n << "/" << m << endl;
					return 0;
				}
			}
		}

		else {
			pre += count;
			count += 1;
		}
	}
}