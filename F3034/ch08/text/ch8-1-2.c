/* ���椣�P�����B�⤸���B�� */
#include <stdio.h>

int main()
{
    int score1 = 56;            /* �B�⤸1 */ 
    int score2 = 67;            /* �B�⤸2 */
    int sum = score1 + score2;  /* �p��2���ܼƬۥ[ */ 
	
    /* ���score1+score2�B�⦡���B�⵲�G */
    printf("�ܼ�score1�� = %d\n", score1);
    printf("�ܼ�score2�� = %d\n", score2);
    printf("score1+score2 = %d\n", sum);
    
    score1 = score1 + 10;       /* �p���ܼƥ[�`�ƭ� */
    /* ���score1+10�B�⦡���B�⵲�G */  
    printf("�ܼ�score1�[10�� = %d\n", score1);

    return 0;
}