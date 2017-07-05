#pragma once

#include <cstdio>
#include <stdexcept>

/* n > 1 */
char* conditionalStatements(int n) {
	if (n < 1) throw std::invalid_argument("n can't be negative or 0");
	char* word = (char*) "Greater than 9";
	switch (n) {
	case 1: word = (char*) "one"; break;
	case 2: word = (char*) "two"; break;
	case 3: word = (char*) "three"; break;
	case 4: word = (char*) "four"; break;
	case 5: word = (char*) "five"; break;
	case 6: word = (char*) "six"; break;
	case 7: word = (char*) "seven"; break;
	case 8: word = (char*) "eight"; break;
	case 9: word = (char*) "nine";
	}

	return word;
}