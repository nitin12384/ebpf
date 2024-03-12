# ebpf
EBPF notes and example code

## Chapter 1
- `strace -c echo "hello"`
   - So many syscalls made by a process

```
ubuntu@test-instance3:~$ strace -c curl localhost:8080
Webserver at 8080 says Hello for req no. 1
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 66.03    0.044928         976        46           mprotect
 11.49    0.007821          50       154           mmap
  5.47    0.003724          57        65        14 openat
  4.06    0.002763          67        41           read
  3.27    0.002225          39        56         1 newfstatat
  2.48    0.001687          88        19           futex
  2.23    0.001518          25        59           close
  1.42    0.000964          34        28           rt_sigaction
  0.61    0.000418         418         1           execve
  0.34    0.000233         116         2           getrandom
  0.27    0.000185         185         1           getsockname
  0.23    0.000156          22         7           poll
  0.21    0.000142         142         1           rseq
  0.20    0.000138          46         3         3 connect
  0.15    0.000101          25         4           socket
  0.15    0.000101          50         2         1 arch_prctl
  0.14    0.000095          15         6           fcntl
  0.12    0.000084          84         1           sysinfo
  0.12    0.000081          81         1           socketpair
  0.11    0.000076          19         4           setsockopt
  0.11    0.000073          36         2           recvfrom
  0.10    0.000071          71         1           geteuid
  0.10    0.000069          13         5           brk
  0.09    0.000062          15         4           pread64
  0.09    0.000060          60         1           sendto
  0.06    0.000042          42         1           write
  0.06    0.000040          40         1           pipe2
  0.06    0.000039          19         2           ioctl
  0.05    0.000034          34         1           set_robust_list
  0.05    0.000033          33         1           set_tid_address
  0.04    0.000024          24         1         1 access
  0.03    0.000018          18         1           lseek
  0.03    0.000018          18         1           munmap
  0.01    0.000007           7         1           getpeername
  0.01    0.000007           7         1           getsockopt
  0.01    0.000004           4         1           prlimit64
------ ----------- ----------- --------- --------- ----------------
100.00    0.068041         129       526        20 total
ubuntu@test-instance3:~$
```

### Questions 
what is the PID of the process that executes these syscalls ? Is it 1 ?



# Links
https://github.com/lizrice/learning-ebpf.