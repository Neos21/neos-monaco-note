#!/usr/bin/env node

// Neo's Monaco Note : Load Content
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
  if(process.env.REQUEST_METHOD !== 'GET') return responseError('Invalid Request Method');
  
  // CORS
  console.log('Access-Control-Allow-Origin: *');
  
  // Check Credential
  const credential = (await fs.promises.readFile(credentialFilePath, 'utf-8')).trim();
  if(process.env.QUERY_STRING !== `credential=${credential}`) return responseError('Invalid Credential');
  
  // Check The Note File Is Exist : If The Note File Does Not Exist, Create Empty File
  const isExistFile = await fs.promises.stat(noteFilePath).then(() => true).catch(() => false);
  if(!isExistFile) {
    try {
      await fs.promises.writeFile(noteFilePath, '', 'utf-8');
    }
    catch(_error) {
      return responseError('Failed To Touch Note File');
    }
  }
  
  // Load Note File
  try {
    const text = await fs.promises.readFile(noteFilePath, 'utf-8');
    console.log(`\n${JSON.stringify({ result: text })}`);
  }
  catch(_error) {
    responseError('Failed To Load Note File');
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
