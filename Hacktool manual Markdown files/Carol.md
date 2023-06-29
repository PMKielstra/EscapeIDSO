# Cracking Passwords

This document is part of the manual for the Hacktool.

To prevent hackers from stealing them, passwords are stored as *hashes*.  A hash is one-way encryption: it's easy to get the hash from the password, but, in principle, it's very hard to get the password from the hash.  The Hacktool can steal password hashes, but it can't crack them.

However, we can precompute hashes for common passwords in a *rainbow table* and look them up when we need to.  Use the `pword` command to tell the Hacktool which password corresponds to the hash it's found.

## Example

**Hacktool:** `Hashed password: 000c285457fc971f862a`

**User:** `pword monkey`

**Hacktool:** `Security measure bypassed.`

## Rainbow Table for Common Passwords

| Hash                 | Password |
| -------------------- | -------- |
| 000c285457fc971f862a | monkey   |
| 04e77bf8f95cb3e1a36a | princess |
| 0522a55e2d5f0993a3d6 | george   |
| 08ddff4ebe39249a9208 | ginger   |
| 09c587fb282c3423f086 | corvette |
| 102cf10b5286bad9fcfe | justin   |
| 136c67657614311f3223 | jordan   |
| 13b1f7ec5beaefc781e4 | freedom  |
| 1c8bfe8f801d79745c46 | letmein  |
| 1ecd41c03ef78bd6daea | chelsea  |
| 1ef7bb1ba959d2c3be7c | golfer   |
| 203b70b5ae883932161b | trustno1 |
| 299d6631d639256a762b | bailey   |
| 2bb80d537b1da3e38bd3 | secret   |
| 2cf24dba5fb0a30e26e8 | hello    |
| 308738b8195da46d65c9 | hockey   |
| 3b0fe0d342e9fa16a5c6 | internet |
| 3ef81cb18bdaac2f67a1 | hammer   |
| 502913bfdd49eab56428 | anthony  |
| 52e8e47b38e854580afc | amanda   |
| 5e884898da28047151d0 | password |
| 686f746a95b6f836d7d7 | love     |
| 78cde64c3e47f2cbfd9d | silver   |
| 81c9d6128b5fcd7bbe4b | diamond  |
| 85738f8f9a7f1b04b532 | whatever |
| 8588310a98676af6e225 | asdfgh   |
| 873ac9ffea4dd04fa719 | cheese   |
| 8f27f432fcbaa4b5180a | soccer   |
| a01edad91c00abe7be5b | baseball |
| a0561fd649cdb6baa784 | access   |
| a0b7c245fab334467e95 | heather  |
| a941a4c4fd0c01cddef6 | sunshine |
| a9c43be948c5cabd56ef | dragon   |
| aa97302150fce811425c | computer |
| aae5be5f6474904b686f | maggie   |
| b5ad121307b9c486471d | scooter  |
| b89dab808c585f889185 | klaster  |
| b9dd960c1753459a7811 | charlie  |
| bd3dae5fb91f88a4f097 | daniel   |
| c64975ba3cf3f9cd5845 | ashley   |
| cbeaff314ef5ad032caa | buster   |
| d081f5e402980b267f1f | guitar   |
| d7e83e28a04b537e6442 | cookie   |
| dbc4a04327176e6577b4 | ranger   |
| dc355ec75a2dc4a1d295 | jackson  |
| e4ad93ca07acb8d908a3 | iloveyou |
| e9a63a4eb15738ae85cd | hunter   |
| ed45d626b07112a8a501 | killer   |
| fa340114498cfb0f5dfe | bigdog   |
| fc52fabe94c0e037d2df | joshua   |


