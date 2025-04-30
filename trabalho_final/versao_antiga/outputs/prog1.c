#include <stdio.h>
#include <stdlib.h>

int main() {
	int a = 10;
	int b = 10;
	int c = 10;
	printf("a: %d\n", a);
	printf("b: %d\n", b);
	printf("c: %d\n", c);
	for (int j = 0; j < 10; j+=1) {
		for (int i = 0; i < 10; i+=1) {
			a = b + c;
			a = b - c;
		}
	}
	printf("a: %d\n", a);
	printf("b: %d\n", b);
	printf("c: %d\n", c);
    
    return 0;
}