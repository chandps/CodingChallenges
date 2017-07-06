#pragma once

#include <stdio.h>
#include <stdlib.h>

long int aVeryBigSum(int n, int ar_size, long int* ar) {
	long int result = 0;
	for (int i = 0; i < ar_size; i++) {
		result += *(ar + i);
	}
	return result;
}

#ifdef TEST

int main() {
	int n;
	scanf("%d", &n);
	long int * arr = malloc(n * sizeof(long int));
	for (int i = 0; i < n; i++) {
		scanf("%ld", &arr[i]);
	}
	printf("%ld", aVeryBigSum(n, n, arr));

	return 0;
}

#endif // TEST