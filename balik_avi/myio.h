#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef TEST
#define SEED 49 /* 🔒 Test ortamı: deterministik */
#else
#define SEED time(NULL) /* 🎲 Normal oyun: rastgele */
#endif

void fun(void) __attribute__((constructor));
void fun(void) { srand(SEED); }
