#include <stdio.h>

int main() {
int X;
int Y;
int B;
int Z;
X = 5;
Y = 2;
B = 0;
Z = 0;
printf("'Z = 0;' => Z = %d\n", Z);
for (int i = X; i > Y; --i) {
if (B) {
Z = Z + 2;
printf("'Z = Z + 2;' => Z = %d\n", Z);
} else {
Z = Z + 1;
printf("'Z = Z + 1;' => Z = %d\n", Z);
}
}

return 0;
}