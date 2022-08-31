#include <stdio.h>
#include <stdlib.h>

p=(int*) malloc(5*sizeof(int))
p=(int*) realloc(p, 22*sizeof(int))

free(p)