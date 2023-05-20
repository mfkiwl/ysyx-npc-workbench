//========== include headers ==========

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#include <malloc.h>
#include <getopt.h>

#include "verilated.h"
#include "verilated_vcd_c.h"
#include "obj_dir/Vnpc.h"

//========== macro definations ==========
#define mem_start 0x90000000
#define mem_end   0x9fffffff
#define mem_size mem_end - mem_start

//========== Verilator/Simulation functions ==========

VerilatedContext* contextp = NULL;
VerilatedVcdC* tfp = NULL;

static Vnpc* top;

void step_and_dump_wave(){
    top -> eval();
    contextp -> timeInc(1);
    tfp -> dump(contextp -> time());
}

void sim_init(){
    contextp = new VerilatedContext;
    tfp = new VerilatedVcdC;
    top = new Vnpc;
    contextp -> traceEverOn(true);
    top -> trace(tfp, 0);
    tfp -> open("dump.vcd");
}

void sim_exit(){
    step_and_dump_wave();
    tfp -> close();
}

//========== Memory manipulation functions ==========

static uint8_t *pmem = NULL;

static inline uint64_t host_read(void *addr, int len) {
    switch (len) {
        case 1: return *(uint8_t  *)addr;
        case 2: return *(uint16_t *)addr;
        case 4: return *(uint32_t *)addr;
        case 8: return *(uint64_t *)addr;
        default: printf("Host Read: Invalid length\n"); assert(0);
  }
}

static inline void host_write(void *addr, int len, uint64_t data) {
    switch (len) {
        case 1: *(uint8_t  *)addr = data; return;
        case 2: *(uint16_t *)addr = data; return;
        case 4: *(uint32_t *)addr = data; return;
        case 8: *(uint64_t *)addr = data; return;
        default: printf("Host Write: Invalid length\n"); assert(0);
  }
}

void mem_init(){
    pmem = (uint8_t *)malloc(mem_size);
    assert(pmem);
    printf("Physical Memory area is [0x%x,0x%x], size is 0x%x\n", mem_start, mem_end, mem_size);
    return;
}

uint8_t* guest_to_host(uint64_t paddr)  {return pmem + paddr - mem_start;}
uint64_t host_to_guest(uint8_t *haddr)  {return haddr - pmem + mem_start;}
bool     mem_in_bound(uint64_t addr)    {return addr - mem_start < mem_size;}

static uint64_t pmem_read(uint64_t addr, int len)                {uint64_t ret = host_read(guest_to_host(addr), len); return ret;}
static void pmem_write(uint64_t addr, int len, uint64_t data)    {host_write(guest_to_host(addr), len, data);}

uint64_t paddr_read(uint64_t addr, int len) {
    if (mem_in_bound(addr)) return pmem_read(addr, len);
    printf("Physical Memory Read : ADDRESS OUT OF BOUND at %lx\n", addr);
    assert(addr - mem_start < mem_size);
    return 0;
}

void paddr_write(uint64_t addr, int len, uint64_t data) {
    if (mem_in_bound(addr)) { pmem_write(addr, len, data); return; }
    printf("Physical Memory Write : ADDRESS OUT OF BOUND at %lx\n", addr);
    assert(addr - mem_start < mem_size);
    return;
}

uint64_t mem_read(uint64_t addr, int len)                   {return paddr_read(addr, len);}
uint64_t mem_write(uint64_t addr, int len, uint64_t val)    {paddr_write(addr, len, val); return val;}

//========== Parse args ==========

char* log_file = NULL;
char* diff_so_file = NULL;
char* elf_file = NULL;
char* das_file = NULL;
char* img_file = NULL;
int difftest_port = 1234;

static int parse_args(int argc, char *argv[]) {
    const struct option table[] = {
        {"batch"    , no_argument      , NULL, 'b'},
        {"log"      , required_argument, NULL, 'l'},
        {"diff"     , required_argument, NULL, 'd'},
        {"port"     , required_argument, NULL, 'p'},
        {"help"     , no_argument      , NULL, 'h'},
        {"readelf"  , required_argument, NULL, 'r'},
        {"readdiasm", required_argument, NULL, 'a'},
        {0          , 0                , NULL,  0 },
  };
  int o;
    while ( (o = getopt_long(argc, argv, "-bhl:d:p:r:a:", table, NULL)) != -1) {
        switch (o) {
            case 'b': /*sdb_set_batch_mode();*/ break;
            case 'p': sscanf(optarg, "%d", &difftest_port); break;
            case 'l': log_file = optarg; printf("log_file = \"%s\"\n", log_file); break;
            case 'd': diff_so_file = optarg; printf("diff_so_file = \"%s\"\n", diff_so_file); break;
            case 'r': elf_file = optarg; printf("elf_file = \"%s\"\n", elf_file); break;
            case 'a': das_file = optarg; printf("das_file = \"%s\"\n", das_file); break;
            case 1: img_file = optarg; printf("img_file = \"%s\"\n", img_file); return 0;
            default:
                printf("Usage: %s [OPTION...] IMAGE [args]\n\n", argv[0]);
                printf("\t-b,--batch              run with batch mode\n");
                printf("\t-l,--log=FILE           output log to FILE\n");
                printf("\t-d,--diff=REF_SO        run DiffTest with reference REF_SO\n");
                printf("\t-p,--port=PORT          run DiffTest with port PORT\n");
                printf("\n");
                exit(0);
    }
  }
  return 0;
}

//========== Initialize image ==========

//========== Initialize monitor ==========
void init_monitor(int argc, char *argv[]){
    printf("Welcome to YSYX-Basic-NPC simulation/verifacation environment\n");
    printf("For help, type \"help\"\n");
    parse_args(argc, argv);
}

//========== Debugger User Interface functions ==========

void sdb_c(){
    return;
}

void sdb_si(){
    return;
}

void sdb_showreg(){
    return;
}

void sdb_showmem(){
    return;
}

//========== main function ==========
int main(int argc, char *argv[]){
    init_monitor(argc, argv);
    return 0;
}