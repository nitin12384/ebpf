# run in project examples directory with:
# sudo ./hello_world.py"

from bcc import BPF

prog = ""
with open("hello_world.bpf.c", 'r') as f:
    prog = f.read()


# This may not work for 4.17 on x64, you need replace kprobe__sys_clone with kprobe____x64_sys_clone
BPF(text=prog).trace_print()