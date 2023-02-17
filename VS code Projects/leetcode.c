#include <stdio.h>
struct course
{
 int courseno;
 char coursename[25];
};
int main()
{
 struct course c[] = { {102, "C"},
 {103, "C++"},
 {104, "Java"}
 };
 int *pointer = (c+2);
 printf("%d ", c[1].courseno);
 printf("%s\n", (*(c+2)).coursename);
 return 0;
}
