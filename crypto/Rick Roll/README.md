# Rick Roll

tag: easy SRPG

I hope you know your crypto basics.

flag format: pearl{string with "_"}

## Solve

Text base ciper need text base solution. I head on to [dcode](https://www.dcode.fr/vigenere-cipher) to get "PEARLCTF" key for the first phase

```
Never Gonna Give You Up
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm
feeling Gotta make you understand
Never gonna give you up Never gonna let you down
Never gonna run around and desert you Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you We've known each other for so long
Your heart's been aching but you're too shy to say it Inside we both know what's been going on
evqx ebzyvbt vg qvtsvqhzg gb ibqrffgnbq
We know the game and we're gonna play it And if you ask me how I'm feeling
Don't tell me you're too blind to see Never gonna give you up
Never gonna let you down
Never gonna run around and desert you Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you Never gonna give you up
Never gonna let you down
Never gonna run around and desert you Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you Never gonna give, never gonna give (Give you up)
(Ooh) Never gonna give, never gonna give (Give you up)
```

These parse not seem right
```
evqx ebzyvbt vg qvtsvqhzg gb ibqrffgnbq
```

I have no ideal what this could be, but after some trier and error, `n` and `o` as key can get me parse like this
```
rick rolling is ...
```

So my assumtion is that we need to make a key base on those character. I quite give up in this step and just asumming the flag is a make sense words by merging decrypted character with key = `n` and key = `o` and replacing the space with `_`
- msg : `evqx ebzyvbt vg qvtsvqhzg gb ibqrffgnbq`
- flag: `rick_rolling_is_difficult_to_understand`
- key : `nnonnnonnonnonnonnononnnoonnonnnon`

That right, and i also add `pearlctf{}` while hoping it the right answer, can't really make sense the key by any mean
