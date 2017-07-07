#pragma once

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int diagonalDifference(int n, int** matrix) {
	int result, diagonal1, diagonal2;
	for (int i = 0; i < n; i++) {
		diagonal1 += matrix[i][i];
		diagonal2 += matrix[(n - 1) - i][(n - 1) - i];
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
		matrix[i] = malloc(n * sizeof *matrix[i]);
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
