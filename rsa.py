from Crypto.PublicKey.RSA import generate;
print(generate(1024));

from Crypto.PublicKey import RSA;
keyGenerator = RSA.generate;
print(RSA.generate(1024));
print(keyGenerator(1024));

import Crypto.PublicKey.RSA as Encryptor;
print(Encryptor.generate(1024));

import Crypto.PublicKey.RSA;
print(Crypto.PublicKey.RSA.generate(1024));

"""
import Crypto.PublicKey.RSA.generate;
print(generate(1024));
"""
