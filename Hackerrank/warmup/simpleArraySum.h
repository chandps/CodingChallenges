#pragma once

int simpleArraySum(int n, int ar_size, int* ar) {
	
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum = sum + ar[i];
	}
	return sum;
}