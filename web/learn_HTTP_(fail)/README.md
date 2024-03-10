
Notthing much, just need to get admin check to '/flag' url (read from source code). This link specificly `https://learn-http.ctf.pearlctf.in/flag`. We have this code from `main.js` function

```js
let to_req = `http://localhost:5001/resp?body=${encodeURIComponent(req_body)}`

childProcess.spawn('node', ['./bot.js', JSON.stringify({
    url: to_req,
    token: genToken()
})]);

return res.status(200).send("Admin will check!")
```

And the `bot.js` will process that with

    JSON.parse(process.argv[2])

	let url = obj['url'];
	let token = obj['token'];

I think that that JSON parse can be a problem here, so we focus just that

Meh, fail

