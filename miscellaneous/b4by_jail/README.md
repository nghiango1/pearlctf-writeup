tag: easy e4stw1nd

Just a baby jail. Nothing special!

```sh
nc dyn.ctf.pearlctf.in 30017
```

## Solve

Python just cast format character to normal, using this [site](https://lingojam.com/ItalicTextGenerator) i get the flag in italic and just run the expression in the eval(). Don't be fool with banner() that all

```sh
nc dyn.ctf.pearlctf.in 30017
>>> 𝘧𝘭𝘢𝘨
pearl{it_w4s_t00_e4sy}
```

## Eh, what did I have done

Read the document for Eval
> Eval can take two type of input, a statement or a compiled object

And thinking that
> Compiled object could be the only solution here, let craft a byte sequenced that can escape the blacklist. This may require python/c API so let get our library ready
    ```sh
    sudo apt-get install python3-dev
    ```

then done a bunch of c code but meh, not needed
