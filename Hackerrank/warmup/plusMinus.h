#pragma once

#include <stdio.h>
#include <stdlib.h>

void plusMinus(int n, int pNum, int nNum, int zeroNum) {
	float *result = (float *) malloc(3 * sizeof *result);

	result[0] = (float) pNum / n;
	result[1] = (float) nNum / n;
	result[2] = (float) zeroNum / n;

	printf("%.6f\n", result[0]);
	printf("%.6f\n", result[1]);
	printf("%.6f\n", result[2]);

	free(result);
}

int main() {
	int n, pNum = 0, nNum = 0, zeroNum = 0;
	scanf("%d", &n);
	int arr[n];

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] > 0) {
			pNum++;
		}
		else if (arr[i] < 0) {
			nNum++;
		}
		else {
			zeroNum++;
		}
	}

	plusMinus(n, pNum, nNum, zeroNum);

	return 0;
}
