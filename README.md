<h1 align="center">LSB-Extraction-Script</h1>

Personal project of a Python script focused on extracting files and messages encripted, through LSB encoding, into RGB pixels of images. Done with the help of Afonso Gomes

--------------------------------

<h2 align="center">What Is LSB?</h2>

**LSB**, the **least significant bit** is the lowest bit in a series of numbers in binary, which is located at the far right of a string. For example, in the binary
number 111110, the least significant bit is the far right 0. Digital data, including picture files, are computed in binary format, where the rightmost digit is
considered the lowest digit whereas the leftmost is considered the highest digit.

The number of image pixels in a PNG file is generally composed of **RGB three primary colours** (red, green, and blue). Each colour occupies 8 bits, and the value
ranges from 0x00 to 0xFF, that is, there are 256 colours, which contain a total of 256 to the third power. Thus there are 16777216 colours in total. The human eye can
distinguish about 10 million different colours, which means that the human eye can't distinguish the remaining 6 million colours. LSB steganography is to **modify the
lowest binary bit (LSB) of RGB colour components**, modifying the lowest bit in the number of pixels, and human eyes will not notice before and after this change,
since each pixel can carry 3 bits of information.

LSB encoding is an important study case in forensics cybersecurity since **malicious** messages and files (such as virus or related rootkit commands) can be encoded
into images, without our knowledge, and be spread without anyone noticing.

--------------------------------

<h2 align="center">How To Use It</h2>

# Setup:

To run this script the user will need to install **Python3** and **pip**, more specifically **version 3.10** of it (tutorial about it can be easily found through
Google). After that you will need to install the required Python libraries and dependencies that are used in it. The first one is **cv2** from the opencv dependency,
and for it just type in the console:

```s
sudo apt-get install python3-opencv
```

For the **bitarray** and **numpy** dependencies type:

```s
pip install bitarray
pip install numpy
```

# Instructions:

Both the script and the Image files the user wants to decode need to be in the same folder. The resulting output of the decoding (_"Output_LSB"_ if choosen as a file
or _"Output_LSB_string"_ if choosen as a string message into a txt file) will be sent to that same folder after the script successfully finishes its task.

To run the script the user just needs to type:

```s
python3 LSB_Extractor.py
```

In the terminal, at the folder's location, and follow all the steps in the script in order to get the decoded result.
