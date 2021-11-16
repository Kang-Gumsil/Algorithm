/* 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

long long sum(std::vector<int> &a);
a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
리턴값: a에 포함되어 있는 정수 n개의 합
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

