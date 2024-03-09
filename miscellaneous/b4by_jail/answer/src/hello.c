#include <Python.h>
#include <stdio.h>

int main() {
  PyCodeObject *c;
  char *conda = "\x65\x00\x83\x00\x46\x00\x64\x00\x53\x00";
  c = (PyCodeObject *)conda;

  printf("Hello");
}
