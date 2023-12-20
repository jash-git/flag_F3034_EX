#include <stdio.h>

int main()
{
    int score1, sum;
    printf("請輸入分數1 =>");
    scanf("%d", &score1);
    int score2;
    printf("請輸入分數2 =>");
    scanf("%d", &score2);
    sum = score1 + score2;
    printf("分數總和 = %d\n" , sum);
        
	return 0;
}