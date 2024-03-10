# jail_time

tag: medium e4stw1nd

You just need to escape the jail. How hard can that be?

```
nc dyn.ctf.pearlctf.in 30016
```

# Solve

Trier and error all possible unicode character
```
0 b'Sorry no valid output to show.\n'
1 b'\x01\n'
2 b'\x02\n'
3 b'\x03\n'
4 b'\x04\n'
5 b'\x05\n'
6 b'\x06\n'
7 b'\x07\n'
8 b'\x08\n'
9 b'\t\n'
10 b'Sorry no valid output to show.\n'
11 b'\x0b\n'
12 b'\x0c\n'
13 b'Sorry no valid output to show.\n'
14 b'\x0e\n'
15 b'\x0f\n'
16 b'\x10\n'
17 b'\x11\n'
18 b'\x12\n'
19 b'\x13\n'
20 b'\x14\n'
21 b'\x15\n'
22 b'\x16\n'
23 b'\x17\n'
24 b'\x18\n'
25 b'\x19\n'
26 b'\x1a\n'
27 b'\x1b\n'
28 b'\x1c\n'
29 b'\x1d\n'
30 b'\x1e\n'
31 b'\x1f\n'
32 b' \n'
33 b'n increased by 2 years for attempted escape.\n'
34 b'Sorry no valid output to show.\n'
35 b'n increased by 2 years for attempted escape.\n'
36 b'n increased by 2 years for attempted escape.\n'
37 b'n increased by 2 years for attempted escape.\n'
38 b'n increased by 2 years for attempted escape.\n'
39 b'Sorry no valid output to show.\n'
40 b'(\n'
41 b')\n'
42 b'n increased by 2 years for attempted escape.\n'
43 b'+\n'
44 b'n increased by 2 years for attempted escape.\n'
45 b'-\n'
46 b''
47 b'n increased by 2 years for attempted escape.\n'
48 b'n increased by 2 years for attempted escape.\n'
49 b'n increased by 2 years for attempted escape.\n'
50 b'n increased by 2 years for attempted escape.\n'
51 b'n increased by 2 years for attempted escape.\n'
52 b'n increased by 2 years for attempted escape.\n'
53 b'n increased by 2 years for attempted escape.\n'
54 b'n increased by 2 years for attempted escape.\n'
55 b'n increased by 2 years for attempted escape.\n'
56 b'n increased by 2 years for attempted escape.\n'
57 b'n increased by 2 years for attempted escape.\n'
58 b'n increased by 2 years for attempted escape.\n'
59 b'n increased by 2 years for attempted escape.\n'
60 b'n increased by 2 years for attempted escape.\n'
61 b'=\n'
62 b'n increased by 2 years for attempted escape.\n'
63 b'?\n'
64 b'n increased by 2 years for attempted escape.\n'
65 b'n increased by 2 years for attempted escape.\n'
66 b'n increased by 2 years for attempted escape.\n'
67 b'n increased by 2 years for attempted escape.\n'
68 b'n increased by 2 years for attempted escape.\n'
69 b'n increased by 2 years for attempted escape.\n'
70 b'n increased by 2 years for attempted escape.\n'
71 b'n increased by 2 years for attempted escape.\n'
72 b'n increased by 2 years for attempted escape.\n'
73 b'n increased by 2 years for attempted escape.\n'
74 b'n increased by 2 years for attempted escape.\n'
75 b'n increased by 2 years for attempted escape.\n'
76 b'n increased by 2 years for attempted escape.\n'
77 b'n increased by 2 years for attempted escape.\n'
78 b'n increased by 2 years for attempted escape.\n'
79 b'n increased by 2 years for attempted escape.\n'
80 b'n increased by 2 years for attempted escape.\n'
81 b'n increased by 2 years for attempted escape.\n'
82 b'n increased by 2 years for attempted escape.\n'
83 b'n increased by 2 years for attempted escape.\n'
84 b'n increased by 2 years for attempted escape.\n'
85 b'n increased by 2 years for attempted escape.\n'
86 b''
87 b'n increased by 2 years for attempted escape.\n'
88 b'n increased by 2 years for attempted escape.\n'
89 b'n increased by 2 years for attempted escape.\n'
90 b'n increased by 2 years for attempted escape.\n'
91 b'n increased by 2 years for attempted escape.\n'
92 b'\n'
93 b'n increased by 2 years for attempted escape.\n'
94 b'n increased by 2 years for attempted escape.\n'
95 b'n increased by 2 years for attempted escape.\n'
96 b'`\n'
97 b'a\n'
98 b'n increased by 2 years for attempted escape.\n'
99 b'c\n'
100 b'n increased by 2 years for attempted escape.\n'
101 b'n increased by 2 years for attempted escape.\n'
102 b'n increased by 2 years for attempted escape.\n'
103 b'n increased by 2 years for attempted escape.\n'
104 b'h\n'
105 b'n increased by 2 years for attempted escape.\n'
106 b'n increased by 2 years for attempted escape.\n'
107 b'n increased by 2 years for attempted escape.\n'
108 b'n increased by 2 years for attempted escape.\n'
109 b'n increased by 2 years for attempted escape.\n'
110 b'n increased by 2 years for attempted escape.\n'
111 b'n increased by 2 years for attempted escape.\n'
112 b'n increased by 2 years for attempted escape.\n'
113 b'q\n'
114 b'r\n'
115 b'n increased by 2 years for attempted escape.\n'
116 b'n increased by 2 years for attempted escape.\n'
117 b'n increased by 2 years for attempted escape.\n'
118 b'n increased by 2 years for attempted escape.\n'
119 b'w\n'
120 b'n increased by 2 years for attempted escape.\n'
121 b'n increased by 2 years for attempted escape.\n'
122 b'n increased by 2 years for attempted escape.\n'
123 b'n increased by 2 years for attempted escape.\n'
124 b'|\n'
125 b'n increased by 2 years for attempted escape.\n'
126 b'n increased by 2 years for attempted escape.\n'
127 b'\x7f\n'
128 b'\xc2\x80\n'
129 b'\xc2\x81\n'
130 b'\xc2\x82\n'
131 b'\xc2\x83\n'
132 b'\xc2\x84\n'
133 b'\xc2\x85\n'
134 b'\xc2\x86\n'
135 b'\xc2\x87\n'
136 b'\xc2\x88\n'
137 b'\xc2\x89\n'
138 b'\xc2\x8a\n'
139 b'\xc2\x8b\n'
140 b'\xc2\x8c\n'
141 b'\xc2\x8d\n'
142 b'\xc2\x8e\n'
143 b'\xc2\x8f\n'
144 b'\xc2\x90\n'
145 b'\xc2\x91\n'
146 b'\xc2\x92\n'
147 b'\xc2\x93\n'
148 b'\xc2\x94\n'
149 b'\xc2\x95\n'
150 b'\xc2\x96\n'
151 b'\xc2\x97\n'
152 b'\xc2\x98\n'
153 b'\xc2\x99\n'
154 b'\xc2\x9a\n'
155 b'\xc2\x9b\n'
156 b'\xc2\x9c\n'
157 b'\xc2\x9d\n'
158 b'\xc2\x9e\n'
159 b'\xc2\x9f\n'
160 b' \n'
161 b'\xc2\xa1\n'
162 b'\xc2\xa2\n'
163 b'\xc2\xa3\n'
164 b'\xc2\xa4\n'
165 b'\xc2\xa5\n'
166 b'\xc2\xa6\n'
167 b'\xc2\xa7\n'
168 b' \xcc\x88\n'
169 b'\xc2\xa9\n'
170 b'a\n'
171 b'\xc2\xab\n'
172 b'\xc2\xac\n'
173 b'\xc2\xad\n'
174 b'\xc2\xae\n'
175 b' \xcc\x84\n'
176 b'\xc2\xb0\n'
177 b'\xc2\xb1\n'
178 b'n increased by 2 years for attempted escape.\n'
179 b'n increased by 2 years for attempted escape.\n'
180 b' \xcc\x81\n'
181 b'\xce\xbc\n'
182 b'\xc2\xb6\n'
183 b'\xc2\xb7\n'
184 b' \xcc\xa7\n'
185 b'n increased by 2 years for attempted escape.\n'
186 b'n increased by 2 years for attempted escape.\n'
187 b'\xc2\xbb\n'
188 b'n increased by 2 years for attempted escape.\n'
189 b'n increased by 2 years for attempted escape.\n'
190 b'n increased by 2 years for attempted escape.\n'
191 b'\xc2\xbf\n'
192 b'\xc3\x80\n'
193 b'\xc3\x81\n'
194 b'\xc3\x82\n'
195 b'\xc3\x83\n'
196 b'\xc3\x84\n'
197 b'\xc3\x85\n'
198 b'\xc3\x86\n'
199 b'\xc3\x87\n'
200 b'\xc3\x88\n'
201 b'\xc3\x89\n'
202 b'\xc3\x8a\n'
203 b'\xc3\x8b\n'
204 b'\xc3\x8c\n'
205 b'\xc3\x8d\n'
206 b'\xc3\x8e\n'
207 b'\xc3\x8f\n'
208 b'\xc3\x90\n'
209 b'\xc3\x91\n'
210 b'\xc3\x92\n'
211 b'\xc3\x93\n'
212 b'\xc3\x94\n'
213 b'\xc3\x95\n'
214 b'\xc3\x96\n'
215 b'\xc3\x97\n'
216 b'\xc3\x98\n'
217 b'\xc3\x99\n'
218 b'\xc3\x9a\n'
219 b'\xc3\x9b\n'
220 b'\xc3\x9c\n'
221 b'\xc3\x9d\n'
222 b'\xc3\x9e\n'
223 b'\xc3\x9f\n'
224 b'\xc3\xa0\n'
225 b'\xc3\xa1\n'
226 b'\xc3\xa2\n'
227 b'\xc3\xa3\n'
228 b'\xc3\xa4\n'
229 b'\xc3\xa5\n'
230 b'\xc3\xa6\n'
231 b'\xc3\xa7\n'
232 b'\xc3\xa8\n'
233 b'\xc3\xa9\n'
234 b'\xc3\xaa\n'
235 b'\xc3\xab\n'
236 b'\xc3\xac\n'
237 b'\xc3\xad\n'
238 b'\xc3\xae\n'
239 b'\xc3\xaf\n'
240 b'\xc3\xb0\n'
241 b'\xc3\xb1\n'
242 b'\xc3\xb2\n'
243 b'\xc3\xb3\n'
244 b'\xc3\xb4\n'
245 b'\xc3\xb5\n'
246 b'\xc3\xb6\n'
247 b'\xc3\xb7\n'
248 b'\xc3\xb8\n'
249 b'\xc3\xb9\n'
250 b'\xc3\xba\n'
251 b'\xc3\xbb\n'
252 b'\xc3\xbc\n'
253 b'\xc3\xbd\n'
254 b'\xc3\xbe\n'
255 b'\xc3\xbf\n'
256 b'\xc4\x80\n'
257 b'\xc4\x81\n'
258 b'\xc4\x82\n'
259 b'\xc4\x83\n'
260 b'\xc4\x84\n'
261 b'\xc4\x85\n'
262 b'\xc4\x86\n'
263 b'\xc4\x87\n'
264 b'\xc4\x88\n'
265 b'\xc4\x89\n'
266 b'\xc4\x8a\n'
267 b'\xc4\x8b\n'
268 b'\xc4\x8c\n'
269 b'\xc4\x8d\n'
270 b'\xc4\x8e\n'
271 b'\xc4\x8f\n'
272 b'\xc4\x90\n'
273 b'\xc4\x91\n'
274 b'\xc4\x92\n'
275 b'\xc4\x93\n'
276 b'\xc4\x94\n'
277 b'\xc4\x95\n'
278 b'\xc4\x96\n'
279 b'\xc4\x97\n'
280 b'\xc4\x98\n'
281 b'\xc4\x99\n'
282 b'\xc4\x9a\n'
283 b'\xc4\x9b\n'
284 b'\xc4\x9c\n'
285 b'\xc4\x9d\n'
286 b'\xc4\x9e\n'
287 b'\xc4\x9f\n'
288 b'\xc4\xa0\n'
289 b'\xc4\xa1\n'
290 b'\xc4\xa2\n'
291 b'\xc4\xa3\n'
292 b'\xc4\xa4\n'
293 b'\xc4\xa5\n'
294 b'\xc4\xa6\n'
295 b'\xc4\xa7\n'
296 b'\xc4\xa8\n'
297 b'\xc4\xa9\n'
298 b'\xc4\xaa\n'
299 b'\xc4\xab\n'
300 b'\xc4\xac\n'
301 b'\xc4\xad\n'
302 b'\xc4\xae\n'
303 b'\xc4\xaf\n'
304 b'\xc4\xb0\n'
305 b'\xc4\xb1\n'
306 b'n increased by 2 years for attempted escape.\n'
307 b'n increased by 2 years for attempted escape.\n'
308 b'\xc4\xb4\n'
309 b'\xc4\xb5\n'
310 b'\xc4\xb6\n'
311 b'\xc4\xb7\n'
312 b'\xc4\xb8\n'
313 b'\xc4\xb9\n'
314 b'\xc4\xba\n'
315 b'\xc4\xbb\n'
316 b'\xc4\xbc\n'
317 b'\xc4\xbd\n'
318 b'\xc4\xbe\n'
319 b'n increased by 2 years for attempted escape.\n'
320 b'n increased by 2 years for attempted escape.\n'
321 b'\xc5\x81\n'
322 b'\xc5\x82\n'
323 b'\xc5\x83\n'
324 b'\xc5\x84\n'
325 b'\xc5\x85\n'
326 b'\xc5\x86\n'
327 b'\xc5\x87\n'
328 b'\xc5\x88\n'
329 b'n increased by 2 years for attempted escape.\n'
330 b'\xc5\x8a\n'
331 b'\xc5\x8b\n'
332 b'\xc5\x8c\n'
333 b'\xc5\x8d\n'
334 b'\xc5\x8e\n'
335 b'\xc5\x8f\n'
336 b'\xc5\x90\n'
337 b'\xc5\x91\n'
338 b'\xc5\x92\n'
339 b'\xc5\x93\n'
340 b'\xc5\x94\n'
341 b'\xc5\x95\n'
342 b'\xc5\x96\n'
343 b'\xc5\x97\n'
344 b'\xc5\x98\n'
345 b'\xc5\x99\n'
346 b'\xc5\x9a\n'
347 b'\xc5\x9b\n'
348 b'\xc5\x9c\n'
349 b'\xc5\x9d\n'
350 b'\xc5\x9e\n'
351 b'\xc5\x9f\n'
352 b'\xc5\xa0\n'
353 b'\xc5\xa1\n'
354 b'\xc5\xa2\n'
355 b'\xc5\xa3\n'
356 b'\xc5\xa4\n'
357 b'\xc5\xa5\n'
358 b'\xc5\xa6\n'
359 b'\xc5\xa7\n'
360 b'\xc5\xa8\n'
361 b'\xc5\xa9\n'
362 b'\xc5\xaa\n'
363 b'\xc5\xab\n'
364 b'\xc5\xac\n'
365 b'\xc5\xad\n'
366 b'\xc5\xae\n'
367 b'\xc5\xaf\n'
368 b'\xc5\xb0\n'
369 b'\xc5\xb1\n'
370 b'\xc5\xb2\n'
371 b'\xc5\xb3\n'
372 b'\xc5\xb4\n'
373 b'\xc5\xb5\n'
374 b'\xc5\xb6\n'
375 b'\xc5\xb7\n'
376 b'\xc5\xb8\n'
377 b'\xc5\xb9\n'
378 b'\xc5\xba\n'
379 b'\xc5\xbb\n'
380 b'\xc5\xbc\n'
381 b'\xc5\xbd\n'
382 b'\xc5\xbe\n'
383 b'n increased by 2 years for attempted escape.\n'
384 b'\xc6\x80\n'
385 b'\xc6\x81\n'
386 b'\xc6\x82\n'
387 b'\xc6\x83\n'
388 b'\xc6\x84\n'
389 b'\xc6\x85\n'
390 b'\xc6\x86\n'
391 b'\xc6\x87\n'
392 b'\xc6\x88\n'
393 b'\xc6\x89\n'
394 b'\xc6\x8a\n'
395 b'\xc6\x8b\n'
396 b'\xc6\x8c\n'
397 b'\xc6\x8d\n'
398 b'\xc6\x8e\n'
399 b'\xc6\x8f\n'
400 b'\xc6\x90\n'
401 b'\xc6\x91\n'
402 b'\xc6\x92\n'
403 b'\xc6\x93\n'
404 b'\xc6\x94\n'
405 b'\xc6\x95\n'
406 b'\xc6\x96\n'
407 b'\xc6\x97\n'
408 b'\xc6\x98\n'
409 b'\xc6\x99\n'
410 b'\xc6\x9a\n'
411 b'\xc6\x9b\n'
412 b'\xc6\x9c\n'
413 b'\xc6\x9d\n'
414 b'\xc6\x9e\n'
415 b'\xc6\x9f\n'
416 b'\xc6\xa0\n'
417 b'\xc6\xa1\n'
418 b'\xc6\xa2\n'
419 b'\xc6\xa3\n'
420 b'\xc6\xa4\n'
421 b'\xc6\xa5\n'
422 b'\xc6\xa6\n'
423 b'\xc6\xa7\n'
424 b'\xc6\xa8\n'
425 b'\xc6\xa9\n'
426 b'\xc6\xaa\n'
427 b'\xc6\xab\n'
428 b'\xc6\xac\n'
429 b'\xc6\xad\n'
430 b'\xc6\xae\n'
431 b'\xc6\xaf\n'
432 b'\xc6\xb0\n'
433 b'\xc6\xb1\n'
434 b'\xc6\xb2\n'
435 b'\xc6\xb3\n'
436 b'\xc6\xb4\n'
437 b'\xc6\xb5\n'
438 b'\xc6\xb6\n'
439 b'\xc6\xb7\n'
440 b'\xc6\xb8\n'
441 b'\xc6\xb9\n'
442 b'\xc6\xba\n'
443 b'\xc6\xbb\n'
444 b'\xc6\xbc\n'
445 b'\xc6\xbd\n'
446 b'\xc6\xbe\n'
447 b'\xc6\xbf\n'
448 b'\xc7\x80\n'
449 b'\xc7\x81\n'
450 b'\xc7\x82\n'
451 b'\xc7\x83\n'
452 b'n increased by 2 years for attempted escape.\n'
453 b'n increased by 2 years for attempted escape.\n'
454 b'n increased by 2 years for attempted escape.\n'
455 b'n increased by 2 years for attempted escape.\n'
456 b'n increased by 2 years for attempted escape.\n'
457 b'n increased by 2 years for attempted escape.\n'
458 b'n increased by 2 years for attempted escape.\n'
459 b'n increased by 2 years for attempted escape.\n'
460 b'n increased by 2 years for attempted escape.\n'
461 b'\xc7\x8d\n'
462 b'\xc7\x8e\n'
463 b'\xc7\x8f\n'
464 b'\xc7\x90\n'
465 b'\xc7\x91\n'
466 b'\xc7\x92\n'
467 b'\xc7\x93\n'
468 b'\xc7\x94\n'
469 b'\xc7\x95\n'
470 b'\xc7\x96\n'
471 b'\xc7\x97\n'
472 b'\xc7\x98\n'
473 b'\xc7\x99\n'
474 b'\xc7\x9a\n'
475 b'\xc7\x9b\n'
476 b'\xc7\x9c\n'
477 b'\xc7\x9d\n'
478 b'\xc7\x9e\n'
479 b'\xc7\x9f\n'
480 b'\xc7\xa0\n'
481 b'\xc7\xa1\n'
482 b'\xc7\xa2\n'
483 b'\xc7\xa3\n'
484 b'\xc7\xa4\n'
485 b'\xc7\xa5\n'
486 b'\xc7\xa6\n'
487 b'\xc7\xa7\n'
488 b'\xc7\xa8\n'
489 b'\xc7\xa9\n'
490 b'\xc7\xaa\n'
491 b'\xc7\xab\n'
492 b'\xc7\xac\n'
493 b'\xc7\xad\n'
494 b'\xc7\xae\n'
495 b'\xc7\xaf\n'
496 b'\xc7\xb0\n'
497 b'n increased by 2 years for attempted escape.\n'
498 b'n increased by 2 years for attempted escape.\n'
499 b'n increased by 2 years for attempted escape.\n'
500 b'\xc7\xb4\n'
501 b'\xc7\xb5\n'
502 b'\xc7\xb6\n'
503 b'\xc7\xb7\n'
504 b'\xc7\xb8\n'
505 b'\xc7\xb9\n'
506 b'\xc7\xba\n'
507 b'\xc7\xbb\n'
508 b'\xc7\xbc\n'
509 b'\xc7\xbd\n'
510 b'\xc7\xbe\n'
511 b'\xc7\xbf\n'
512 b'\xc8\x80\n'
513 b'\xc8\x81\n'
514 b'\xc8\x82\n'
515 b'\xc8\x83\n'
516 b'\xc8\x84\n'
517 b'\xc8\x85\n'
518 b'\xc8\x86\n'
519 b'\xc8\x87\n'
520 b'\xc8\x88\n'
521 b'\xc8\x89\n'
522 b'\xc8\x8a\n'
523 b'\xc8\x8b\n'
524 b'\xc8\x8c\n'
525 b'\xc8\x8d\n'
526 b'\xc8\x8e\n'
527 b'\xc8\x8f\n'
528 b'\xc8\x90\n'
529 b'\xc8\x91\n'
530 b'\xc8\x92\n'
531 b'\xc8\x93\n'
532 b'\xc8\x94\n'
533 b'\xc8\x95\n'
534 b'\xc8\x96\n'
535 b'\xc8\x97\n'
536 b'\xc8\x98\n'
537 b'\xc8\x99\n'
538 b'\xc8\x9a\n'
539 b'\xc8\x9b\n'
540 b'\xc8\x9c\n'
541 b'\xc8\x9d\n'
542 b'\xc8\x9e\n'
543 b'\xc8\x9f\n'
544 b'\xc8\xa0\n'
545 b'\xc8\xa1\n'
546 b'\xc8\xa2\n'
547 b'\xc8\xa3\n'
548 b'\xc8\xa4\n'
549 b'\xc8\xa5\n'
550 b'\xc8\xa6\n'
551 b'\xc8\xa7\n'
552 b'\xc8\xa8\n'
553 b'\xc8\xa9\n'
554 b'\xc8\xaa\n'
555 b'\xc8\xab\n'
556 b'\xc8\xac\n'
557 b'\xc8\xad\n'
558 b'\xc8\xae\n'
559 b'\xc8\xaf\n'
560 b'\xc8\xb0\n'
561 b'\xc8\xb1\n'
562 b'\xc8\xb2\n'
563 b'\xc8\xb3\n'
564 b'\xc8\xb4\n'
565 b'\xc8\xb5\n'
566 b'\xc8\xb6\n'
567 b'\xc8\xb7\n'
568 b'\xc8\xb8\n'
569 b'\xc8\xb9\n'
570 b'\xc8\xba\n'
571 b'\xc8\xbb\n'
572 b'\xc8\xbc\n'
573 b'\xc8\xbd\n'
574 b'\xc8\xbe\n'
575 b'\xc8\xbf\n'
576 b'\xc9\x80\n'
577 b'\xc9\x81\n'
578 b'\xc9\x82\n'
579 b'\xc9\x83\n'
580 b'\xc9\x84\n'
```


Sample black list
```
00 int = 33
01 int = 35
02 int = 36
03 int = 37
04 int = 38
05 int = 42
06 int = 44
07 int = 47
08 int = 48
09 int = 49
10 int = 50
11 int = 51
12 int = 52
13 int = 53
14 int = 54
15 int = 55
16 int = 56
17 int = 57
18 int = 58
19 int = 59
20 int = 60
21 int = 62
22 int = 64
23 int = 65
24 int = 66
25 int = 67
26 int = 68
27 int = 69
28 int = 70
29 int = 71
30 int = 72
31 int = 73
32 int = 74
33 int = 75
34 int = 76
35 int = 77
36 int = 78
37 int = 79
38 int = 80
39 int = 81
40 int = 82
41 int = 83
42 int = 84
43 int = 85
44 int = 87
45 int = 88
46 int = 89
47 int = 90
48 int = 91
49 int = 93
50 int = 94
51 int = 95
52 int = 98
53 int = 100
54 int = 101
55 int = 102
56 int = 103
57 int = 105
58 int = 106
59 int = 107
60 int = 108
61 int = 109
62 int = 110
63 int = 111
64 int = 112
65 int = 115
66 int = 116
67 int = 117
68 int = 118
69 int = 120
70 int = 121
71 int = 122
72 int = 123
73 int = 125
74 int = 126
75 int = 178
76 int = 179
77 int = 185
78 int = 186
79 int = 188
80 int = 189
81 int = 190
82 int = 306
83 int = 307
84 int = 319
85 int = 320
86 int = 329
87 int = 383
88 int = 452
89 int = 453
90 int = 454
91 int = 455
92 int = 456
93 int = 457
94 int = 458
95 int = 459
96 int = 460
97 int = 497
98 int = 498
99 int = 499
```