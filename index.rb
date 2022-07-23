#!/usr/bin/ruby

# ======================================================================
# Neo's Monaco Note
# ======================================================================


# Requires
# ======================================================================

require 'cgi'
require 'fileutils'


# Constants
# ======================================================================

# Private Directory Path
PRIVATE_DIRECTORY_PATH = '/PATH/TO/private'
# Credential File Path
CREDENTIAL_FILE_PATH = "#{PRIVATE_DIRECTORY_PATH}/credential.txt"
# Monaco Note File Path
MONACO_NOTE_FILE_PATH = "#{PRIVATE_DIRECTORY_PATH}/neos-monaco-note/index.html"


# Global Variables
# ======================================================================

# CGI Object
$cgi = CGI.new


# Functions
# ======================================================================

def main()
  print("Content-Type: text/html; charset=utf-8\n\n")
  unless is_valid_credential
    print_access_denied()
    return
  end
  print(File.read(MONACO_NOTE_FILE_PATH))
end

def is_valid_credential()
  credential_param = $cgi['credential']
  credential = ''
  File.open(CREDENTIAL_FILE_PATH, 'r:UTF-8') { |credential_file|
    credential = credential_file.read.chomp
  }
  return credential_param == credential
end

def print_access_denied()
  print(<<"EOL")
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex,nofollow">
    <title>Neo's Monaco Note</title>
    <link rel="icon" href="/favicon.ico">
  </head>
  <body>
    <h1>Access Denied</h1>
  </body>
</html>
EOL
end


# Execute
# ======================================================================

main
