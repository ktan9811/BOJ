#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int in[3];
	cin >> in[0] >> in[1] >> in[2];
	sort(in, in + 3);
	if ((in[2] == in[1]) && (in[1] == in[0])) {
		cout << 10000 + in[2] * 1000 << endl;
	}
	else if ((in[2] == in[1]) || (in[1] == in[0]))
	{
		cout << 1000 + in[1] * 100 << endl;
	}
	else {
		cout << in[2] * 100 << endl;
	}
	return 0;
}