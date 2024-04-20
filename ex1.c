#include <stdio.h>

void count_bits( int val ){
    int mask = 1;
    int n_bits = 0;
    int zero = 0;
    int one = 0;
    while(n_bits < 32){
        if((mask & val) == 0) zero++; else one++;
        mask = mask << 1;
        n_bits++;
    }
    printf("Numero de 0: %d \n", zero);
    printf("Numero de 1: %d \n", one);
}

void print_fibonnaci( int N ){
    if( N == 0) return;
    int a = 0;
    int b = 1;
    int result = 0;
    for(int i = 0; i < N; i++){
        result = a + b;
        printf("Fibonnacci Sequence %d: %d \n", i, result);
        a = b;
        b = result;
    }
}

int file_symbol_freq( char *file_name, char symbol ){
    FILE *fp=fopen(file_name,"r");
    if(fp == NULL){
        printf("Erro ao abrir o arquivo \n");
        return -1;
    }
    int c = fgetc(fp);
    int count = 0;

    while( c != EOF){
        if(c == symbol) count++;
        c=fgetc(fp);
    }

    if(count == 0) return -1;
    else return count;
}

void file_histogram( char *file_name ) {
    
    FILE *fp=fopen(file_name,"r");
    if(fp == NULL){
        printf("Erro ao abrir o arquivo \n");
        return;
    }
    char c = fgetc(fp);
    int array [255] = {0};
    
    while( c != EOF){
        array[c]++;
        c = fgetc(fp);
    }

    for(int i = 0; i < 255; i++){
        if(array[i] != 0)
            printf("%c: %d \n", i, array[i]);
    }

}

void reverse_file( char *input_file_name, char *output_file_name){
    FILE *fp=fopen(input_file_name,"r");
    FILE *op=fopen(output_file_name,"w");

    if(fp == NULL || op == NULL) {
        printf("Erro ao abrir um dos arquivos \n");
        return;
    }

    fseek(fp, 0, SEEK_END);
    long end_file = ftell(fp);
    char c;
    for(long i = 0; i <= end_file; i++){
        fseek(fp, -i, SEEK_END);
        c = fgetc(fp);
        fputc(c, op);
    }
    
}



void main(){
    int val = 3;
    count_bits(val);
    print_fibonnaci(val);
    int freq = file_symbol_freq("resources/alice29.txt",'s');
    printf("Frequencia do symbol %c: %d \n",'$',freq);
    file_histogram("resources/test.txt");
    reverse_file("resources/test.txt", "/workspaces/CD/test2.txt");
}