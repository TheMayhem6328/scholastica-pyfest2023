# Question 18

## Introduction

The Vigenère cipher is a classic encryption technique that enhances the security of the Caesar cipher by using a keyword to shift each letter of the plaintext by a varying amount. Let's dive into the details of the Vigenère cipher and apply it to a scenario.

## Explanation

The Vigenère cipher works as follows:

1. You have a plaintext message.
2. You also have a secret keyword, which is a word or phrase.
3. To encrypt the message, you repeat the keyword to match the length of the plaintext.
4. For each letter in the plaintext, you shift it forward in the alphabet by the corresponding letter's position in the keyword (`A=0`, `B=1`, `C=2`, `...`).
5. Wrap around the alphabet if necessary (e.g., shifting `'Z'` forward by `1` gives `'A'`).
6. Combine the shifted letters to form the encrypted message.

## Scenario

Imagine you want to send the message "SECRET" using the keyword "KEY." Let's walk
through the encryption process step by step.

- Plaintext: `SECRET`
- Keyword: `KEY`
- Repeated Keyword: `KEYKEY`
- Encryption:
  - `S` + `K` = `C`
  - `E` + `E` = `I`
  - `C` + `Y` = `A`
  - `R` + `K` = `B`
  - `E` + `E` = `I`
  - `T` + `Y` = `R`

So, the encrypted message is `"CIABIR"`.

## Task

1. Encrypt the message `"ENCRYPTED"` using the keyword `"SECURITYISKEY"`.
2. Decrypt the message `"WEXAHAKMNP"` using the keyword `"CHALLENGEACCEPTED"`.
3. Encrypt the message `"EXTRACTION"` using the keyword `"COMPLEXITY"`.
4. Decrypt the message `"VWHUJARZTM"` using the keyword `"ENCRYPTIONISFUN"`.
5. Implement a function that can automatically find the length of the keyword used to encrypt a Vigenère ciphered message. Use this function to find the keyword length of the message `"JTOHYZSFOCQXQY"` and provide the length.

## Note

Attempt to provide all of the necessary validations and make the code as efficient as possible. Lack of validation and an inefficient code will merit the deduction of marks
