#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int res, N; 
	int in_arr[200] = { 0, };
	cin >> res >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> in_arr[2 * i] >> in_arr[2 * i + 1];
	}
	
	for (int i = 0; i < N; i ++) {
		if (in_arr[2 * i] == 0) {
			break;
		}
		res -= in_arr[2 * i] * in_arr[2 * i + 1];
	}

	if (res == 0) cout << "Yes";
	else cout << "No";
	return 0;
}