#include<stdbool.h>
#include<stdio.h>

int iringbuf_size = 0;

void itrace_init(){
    printf("trace: itrace enabled\n");
    if(remove("itrace.txt")==0){
        printf("NEMU removed previous itrace records.\n");
    } // So previous traces will not be recorded
    return;
}

void itrace_write(char* messageWrite){
    FILE *itrace_file = fopen("itrace.txt", "a+");
    assert(itrace_file != NULL);
    fputs(messageWrite, itrace_file);
    fclose(itrace_file);
    return;
}

void iringbuf_init(int size){
    iringbuf_size = size;
    printf("trace: iringbuf enabled, ring size is %d\n", iringbuf_size);
    if(remove("iringbuf.txt")==0){
        printf("NEMU removed previous iringbuf records.\n");
    } // So previous traces will not be recorded
    return;
}

void mtrace_init(){
    printf("trace: mtrace enabled\n");
    if(remove("$mtrace.txt")==0){
        printf("NEMU removed previous mtrace records.\n");
    } // So previous traces will not be recorded
    return;
}

void ftrace_init(){
    printf("trace: ftrace enabled\n");
    if(remove("ftrace.txt")==0){
        printf("NEMU removed previous ftrace records.\n");
    } // So previous traces will not be recorded
    return;
}

void trace_init(){
    IFDEF(CONFIG_InstructionTrace, itrace_init());
    IFDEF(CONFIG_InstructionRingBuffer, iringbuf_init(64));
    IFDEF(CONFIG_MemoryTrace, mtrace_init());
    IFDEF(CONFIG_FunctionTrace, ftrace_init());
    return;
}