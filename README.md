# edge-ml

[![cpp-linter](https://github.com/cpp-linter/cpp-linter-action/actions/workflows/cpp-linter.yml/badge.svg)](https://github.com/cpp-linter/cpp-linter-action/actions/workflows/cpp-linter.yml)

## Installing pre-commit hooks

Install pre-commmit following the directions from [here](https://pre-commit.com/#install). If you're on a Mac with `homebrew`, the easiest way is `brew install pre-commit`.

Then, run `pre-commit install`. You only need to do this once.

Now, pre-commit will run automatically when you make a commit, and will fix files for you. Make sure to add the changed files after pre-commit runs!

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

## Running the client

- `python app.py` in `client/`
- Make a `.env` file with `SECRET_KEY` and `MONGODB_URI`
- `requirements.txt` in `client/`
- http://127.0.0.1:5000
