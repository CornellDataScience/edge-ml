# edge-ml

[![cpp-linter](https://github.com/cpp-linter/cpp-linter-action/actions/workflows/cpp-linter.yml/badge.svg)](https://github.com/cpp-linter/cpp-linter-action/actions/workflows/cpp-linter.yml)

# To Lint CPP
Make sure git-clang-format is installed with `npm install -g clang-format`
1. Call `clang-format.sh` under ci/
2. `git add` and `git commit`!

## To run 

`cd build` 

`cmake ..`

`make`

`./camera`

## Setting up Twilio

- `cd` to `src/message/`

- Make a `.env` file with `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` set to your account SID and Auth Token 

- macOS: `brew tap twilio/brew && brew install twilio`

- `twilio login`

- `pip install twilio`
