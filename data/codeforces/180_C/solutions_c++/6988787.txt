#include <stdio.h>
int ac, r, isu;
char c;
char end;
int main(void){
  end = 0;
  for (;;) {
    for (;(c=getchar())!='\n';) {
      if (feof(stdin)) {
        end = 1;
        break;
      }
      ac+=isu=c>='a'&&c<='z';
      r=(ac+isu<r+!isu)?ac+isu:r+!isu;
    }
    if (end) break;
    printf("%d\n", r);
  }
  return 0;
}