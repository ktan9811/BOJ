#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int N, arr[100] = { 0, };
	int search, cnt = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	cin >> search;
	for (int i = 0; i < N; i++) {
		if (search == arr[i]) cnt++;
	}
	cout << cnt;
	return 0;
}