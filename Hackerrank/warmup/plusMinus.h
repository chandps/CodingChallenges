#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

float* plusMinus(int n, int pNum, int nNum, int zeroNum) {
	static float* result = (float*)malloc(3 * sizeof *result);

	result[0] = (float)pNum / (float)n;
	result[1] = (float)pNum / (float)n;
	result[2] = (float)pNum / (float)n;

	return result;
}

int main() {
	int n;
	scanf("%d", &n);
	int arr[n];
	for (int arr_i = 0; arr_i < n; arr_i++) {
		scanf("%d", &arr[arr_i]);
	}
	return 0;
}
