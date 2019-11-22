const express = require('express');
const app = express();

var JavaScriptObfuscator = require('javascript-obfuscator');
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Well this is my api for weird HTA')
});

app.post('/api/weirdhta', (req, res) => {
  const base64 = req.body.code;
  let data = base64;
  let buff = new Buffer(data, 'base64');
  let text = buff.toString('ascii');
  var obfuscationResult = JavaScriptObfuscator.obfuscate(
    `
    ${text}
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

  res.send(obfuscationResult.getObfuscatedCode());
});

const port = process.env.PORT || 4000;
app.listen(port, () => console.log(`listening on port ${port}....!`));
