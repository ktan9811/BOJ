#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int32_t a = 0x00;
	int in;

	for (int i = 0; i < 28; i++) {
		cin >> in;
		a = a | (1 << in);
	}

	for (int i = 1; i <= 30; i++) {
		if (!(a & (1 << i))) cout << i << endl;
	}
}