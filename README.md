# Pearlctf write up

Online jeopardy CTF from CyberLabs, IIT (ISM) Dhanbad, India. More info can be found [here](https://ctftime.org/event/2231/)
- Time: Fri, 08 March 2024, 12:00 UTC — Sat, 09 March 2024, 23:59 UTC (36 hours)
- Rating weight: 23.95
- Official URL: https://play.pearlctf.in/

Tools used:
- Python
- Online: Vigenere cipher automate decrypt, jupiter notebook, google

## Success attemp:

### Machine Trouble

[`miscellaneous/Machine Trouble/`](/miscellaneous/Machine%20Trouble): This is quite new, but can take it in 3 stages
- Find the key length: Use connected stage machine that accept every character, eg:
    ```
    q0 @ q1 @ q2 @ q3 ... @ qn
    ```
    Change n until we have 1 as result, I get `key_length = 11`
- Find the character that build up key: Use the connected stage machine (with found length) that block one character, eg:
    ```
    q0 ~a q1 ~a q2 ~a ... ~a q11
    ```
    Until we found all character that stuck the machine (which mean they is the part of the key). I get `white_list = "_acdefhk"`
- Find each character that build up the key: Trie and error every spot from begin to end stage, block only one character from the white list in that only spot
    ```
    q0 ~a q1 @ q2 @ ... @ q11
    ```
    If it stuck, it mean that position of key is that character, repeat until found all. I get the string `dfa_hacked`

### 3 spies

[`crypto/3 spies/`](/crypto/3%20spies/): RSA attack, then a blob Base64 encode img for web to get flag

### Rick roll

[`crypto/Rick Roll/`](/crypto/Rick%20Roll/): Vigenere cipher with key PEARLCTF, the next stage text use a random key combine `o` and `n` shift

### b4by_jail

[`miscellaneous/b4by_jail/`](/miscellaneous/b4by_jail/): Python blacklist jail can't detect formated string, call `𝘧𝘭𝘢𝘨` and get the key



## Fail attempt

`crypto/Security++_(fail)/`: Fail to manage time to try and finish this

`crypto/Baby's Message Out (fail)/`: Fail to manage time to try and finish this

`crypto/three letter acronyms (fail)/`: Can't understand the problem

`game/Guesso_(fail)/`: The similarity result is weird and I'm unsure if it bigger mean better. Try to create my own model and the similarity score can go over ~1200.

`osint/lost_lette_(fail)/`: I think I will need a native friend for this one

`web/learn_HTTP_(fail)/`: Can't bypass admin check to get flag

## Final score

> More can be found here [ylsolo team profile](https://play.pearlctf.in/teams/594)

- Team placement: 65th, with 1205 points (thank nap =)!)

    ![image](https://github.com/nghiango1/pearlctf-writeup/assets/31164703/488223a5-f2f5-4891-b54b-009e929604fd)

- Point distribution:

    ![image](https://github.com/nghiango1/pearlctf-writeup/assets/31164703/9c00ec85-eb67-4444-acf0-50b53a041131)
