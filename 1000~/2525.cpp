#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int hour , min, inp;
	cin >> hour >> min >> inp;
	min += inp;
	hour += min / 60;
	min = min % 60;
	hour = hour % 24;
	cout << hour << ' ' << min << ' ';
	return 0;
}