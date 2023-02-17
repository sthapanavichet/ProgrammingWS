#include <stdio.h>
char * add(char * s);
char * addBinary(char * a, char * b){
    lenA = sizeof(a)/sizeof(a[0]);
    lenB = sizeof(b)/sizeof(b[0]);
    for(int i = 0; i < 10; i++) {
        if(b[i] == '1') {
            add(a+i);
        }
    }
    for(int i = 0, i < lenA, i++) {
        a[0+i] = a[lenA-i];
    }
    return a;
}


char * add(char * s) {
    char * a = s;
    if(*a == '1') {
        *a = '0';
        add(a+1);
    }
    else if(*a == '0' || *a == '\0') {
        *a = '1';
    }
    return a;
}

void inverse(char * s) {
    char a[]
    for(int i)
}
int main() {
    char a[5] = "11", b[3] = "1";
    char * c;
    c = addBinary(a, b);
    printf("%s", c);
    return 0;
}
