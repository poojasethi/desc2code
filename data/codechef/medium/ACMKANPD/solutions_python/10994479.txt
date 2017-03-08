#include<stdio.h>
#include<string.h>

int count_zeros(const char* str) {
	int num_zeros = 0;
	for (int i = 0; str[i] != 0; i += 1) {
		if (str[i] == '0') {
			num_zeros += 1;
		}
	}
	return num_zeros;
}

void fill(char* str, char c, int n) {
	for (int i = 0; i < n; i += 1) {
		str[i] = c;
	}
}

int binary_string_to_number(const char* bin_str) {
	int len = strlen(bin_str);
	int number = 0;
	for (int i = len - 1; i >= 0; i -= 1) {
		if (bin_str[i] == '1') {
			int bit_pos = len - i - 1;
			number |= (1 << bit_pos);
		}
	}
	return number;
}

int main(void) {
	unsigned char number_last_bit_index = 0;
	char number[31] = {0};
	char token[33] = {0};
	char flag;
	while (strcmp(token, "~") != 0) {
		scanf("%s32", token);
		if (strcmp(token, "#") == 0) {
			number[number_last_bit_index] = 0;
			printf("%d\n", binary_string_to_number(number));
			number[0] = 0;
			number_last_bit_index = 0;
		}
		else if (strcmp(token, "0") == 0) {
			flag = '1';
		}
		else if (strcmp(token, "00") == 0) {
			flag = '0';
		}
		else {
			int num_zeros = count_zeros(token);
			if (num_zeros == strlen(token)) {
				num_zeros -= 2;
				fill(number + number_last_bit_index, flag, num_zeros);
				number_last_bit_index += num_zeros;
			}
		}
	}
	return 0;
}