# Security++

tag: easy n0tsane

More keys = More security. Prove me wrong!

```sh
nc dyn.ctf.pearlctf.in 30015
```

## Solve

Look like a AES implement, i see [s_box](https://en.wikipedia.org/wiki/Rijndael_S-box) in the enc.py

`nc` is a encrypt machine, which may mean that there is a side channel attack in this AES implement

our text being used to pad the flag
key is seperated with 2 part, each 16 character


