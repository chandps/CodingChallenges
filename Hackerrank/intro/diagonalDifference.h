#pragma once

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int diagonalDifference(int n, int** matrix) {
	int result = 0, diagonal1 = 0, diagonal2 = 0;

	for (int i = 0; i < n; i++) {
		diagonal1 += matrix[i][i];
		diagonal2 += matrix[i][(n - 1) - i];
	}
	result = abs(diagonal1 - diagonal2);

	return result;
}

int main() {
	int n;
	scanf("%d", &n);

	/* allocate matrix */
	int** matrix = (int**) malloc(n * sizeof *matrix);
	for (int i = 0; i < n; i++) {
		matrix[i] = (int*) malloc(n * sizeof *matrix[i]);
	}

	/* initialize matrix */
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &matrix[i][j]);
		}
	}

	/* get the result */
	int result = diagonalDifference(n, matrix);
	/* print output */
	printf("%d", result);

	/* deallocate matrix */
	for (int i = 0; i < n; i++) {
		free(matrix[i]);
	}
	free(matrix);

	return 0;
}
