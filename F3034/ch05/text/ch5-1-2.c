/* 執行不同種類運算元的運算 */
#include <stdio.h>

int main()
{
    int score1 = 56;            /* 運算元1 */ 
    int score2 = 67;            /* 運算元2 */
    int sum = score1 + score2;  /* 計算2個變數相加 */ 
	
    /* 顯示score1+score2運算式的運算結果 */
    printf("變數score1值 = %d\n", score1);
    printf("變數score2值 = %d\n", score2);
    printf("score1+score2 = %d\n", sum);
    
    score1 = score1 + 10;       /* 計算變數加常數值 */
    /* 顯示score1+10運算式的運算結果 */  
    printf("變數score1加10分 = %d\n", score1);

    return 0;
}