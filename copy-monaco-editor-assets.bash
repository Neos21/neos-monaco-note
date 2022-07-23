#!/bin/bash

# Copy Monaco Editor AMD Assets

cp -r ./node_modules/monaco-editor/min .
zip -r min.zip ./min
