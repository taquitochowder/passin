# Passin

## Problem to solve: generating and retrieving passwords with ease :lock:

Passin is an interesting solution to the problem for the following reasons:

- No data is stored (except for a secret key)
- Generating and retrieving passwords are the same action

Passwords are generated with a hashing algorithm, which are one-to-one functions, so if you know what generated the password, you'll be able to get it. In Passin's case, all the user needs to remember is their master password and the service name. For additional security, a secret key is generated to be used in password generation.

## Usage

Passin is used on the command line with the following commands:

```console
passin setup
passin get 'service_name'
passin reset
```