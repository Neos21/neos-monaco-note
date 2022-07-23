#!/usr/bin/env node

// Neo's Monaco Note : Save Content
// ================================================================================

/** Credential File Path */
const credentialFilePath = '/PATH/TO/private/credential.txt';
/** Note File Path */
const noteFilePath       = '/PATH/TO/private/neos-monaco-note/note.md';

// ================================================================================

const fs = require('fs');

process.on('uncaughtException', _error => responseError('Uncaught Exception'));

(async () => {
  console.log('Content-Type: application/json; charset=UTF-8');
  if(process.env.REQUEST_METHOD !== 'POST') return responseError('Invalid Request Method');
  
  // CORS
  console.log('Access-Control-Allow-Origin: *');
  console.log('Access-Control-Allow-Methods: POST, OPTIONS');
  console.log('Access-Control-Allow-Headers: Accept, Content-Type');
  if(process.env.REQUEST_METHOD === 'OPTIONS') return console.log('Status: 200\n');
  
  // Get POST Body
  const postBody = await getPostBody();
  if(!postBody) return responseError('Failed To Parse Post Body');
  
  // Check Credential
  const credential = (await fs.promises.readFile(credentialFilePath, 'utf-8')).trim();
  if(postBody.credential !== credential) return responseError('Invalid Credential');
  
  // Required Parameter
  const content = postBody.content;
  if(content == null) return responseError('Invalid Parameters');
  
  // Save Note File
  try {
    await fs.promises.writeFile(noteFilePath, content, 'utf-8');
    console.log(`\n${JSON.stringify({ result: 'OK' })}`);
  }
  catch(_error) {
    return responseError('Failed To Save Note File');
  }
})();

/**
 * Response Error
 * 
 * @param {string} errorMessage Error Message
 */
function responseError(errorMessage) {
  console.log(`Status: 400\n\n${JSON.stringify({ error: errorMessage })}`);
}

/**
 * Get POST Body
 * 
 * @return {Promise<Object>|undefined} POST Body Or `undefined` If Error
 */
async function getPostBody() {
  try {
    let postBodyStr = '';
    for await(const chunk of process.stdin) postBodyStr += chunk;
    return JSON.parse(postBodyStr);
  }
  catch(_error) { }  // Return `undefined`
}
