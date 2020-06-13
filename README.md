## **PROJECT NAME**
> PUBLIC-KEY CRYPTOSYSTEMS

---
### **Table of contents**
- [Description](#description)
- [Environment](#environment)
- [Requirements](#requirements)
- [Installing](#installing)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## **Description**
This is the way to install rsa-algorithm which is one of the important algorithms in public-key-cryptosystems

---

## **Environment**
- Window 10 or Ubuntu 18.04

---

## **Requirements**
- [Python 2.7.12 or Python(>=3.6)](https://www.python.org/downloads/);
- PyQt5;

---

## **Installing**
```
git clone https://github.com/tainp98/rsa_algorithm.git
cd rsa_algorithm
py -m pip install pyqt5 (on Window)
python/python3 -m pip install pyqt5(on Ubuntu)
```

---

## **How To Use**
1. Run program
   - py window.py (on Window)
   - python/python3 window.py (on Ubuntu)
2. Label and Button
   - Input:
     - Label `threshold` : threshold to create 2 prime numbers
     - Label `error 1/4^` : setup error for algorithm
     - Label `input text` : plaintext to exchange
   - Output:
     - Button `output` : to generate output
     - Button `clear` : clear output
     - Label `p-q-n-e-d` : the corresponding values in the rsa-algorithm
     - Label `plaintext` : plaintext to encrypt
     - Label `ciphertext` : ciphertext after encrypt
     - Label `decrypt ciphertext` : text after decrypt ciphertext  

---

## **Author Info**
- Students of Hanoi University of Science And Technology:
  - ``` Nguyen Phu Tai```