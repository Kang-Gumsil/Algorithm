/* ���� n���� �־����� ��, n���� ���� ���ϴ� �Լ��� �ۼ��Ͻÿ�.

long long sum(std::vector<int> &a);
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� �迭 (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� ��
*/

#include <iostream>
#include <vector>
using namespace std;

long long sum(std::vector<int>& a) {
	
	long long ans = 0;
	vector<int>::iterator it;

	for (it = a.begin(); it != a.end(); it++)
		ans += *it;

	return ans;
}

int main()
{
	std::vector<int> v;
	v.push_back(10);
	v.push_back(15);
	v.push_back(15);
	v.push_back(10);

	std::cout << sum(v) << std::endl;
}

