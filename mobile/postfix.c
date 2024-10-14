#include <stdio.h>  
#include <stdlib.h>  
#define SIZE 50
int st[SIZE];  
int top = -1;  
void push(int item) {  
    if (top >= SIZE - 1) {  
printf("Stack Overflow\n");  
        return;  
    }  
    top++;  
    st[top] = item;  
}  
int pop() {  
    if (top < 0) {  
printf("Stack Underflow\n");  
        return -1;  
    }  
    int item = st[top];  
    top--;  
    return item;  
}  
int is_operator(char sy) {  
    if (sy == '+' || sy == '-' || sy == '*' || sy == '/') {  
        return 1;  
    }  
    return 0;  
}  
int evaluate(char* expression) {  
    int i = 0;  
    char sy = expression[i];  
    int op1, op2, r;  
  
    while (sy != '\0') {  
        if (sy >= '0' && sy <= '9') {  
            int num = sy - '0';  
            push(num);  
        }  
        else if (is_operator(sy)) {  
            op2 = pop();  
            op1 = pop();  
            switch(sy) {  
                case '+': r = op1 + op2; break;  
                case '-': r = op1 - op2; break;  
                case '*': r = op1 * op2; break;  
                case '/': r = op1 / op2; break;  
            }  
            push(r);  
        }  
        i++;  
        sy = expression[i];  
    }  
    r = pop();  
    return r;  
}  
  
int main() {  
    char expression[] = "2 3 * 2 1 - / 5 4 1 - * +";  
    int r = evaluate(expression);  
printf("Result= %d\n", r);  
return 0;  
}