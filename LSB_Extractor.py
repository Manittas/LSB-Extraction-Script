# ------------------------------------------ #
#   Automated LSB extractor for RGB images   #
# ------------------------------------------ #
#         Project done by Manittas           #
#          Python 3.10.4 version             #
# ------------------------------------------ #

import cv2
import numpy as np
import types
import sys
from bitarray import bitarray

#
# converts into binary
# --------------------
def toBinary(pixel):

    # checks the type
    if type(pixel) == str:
        return ''.join([ format(ord(i), "08b") for i in pixel ])
    elif type(pixel) == bytes or type(pixel) == np.ndarray:
        return [ format(i, "08b") for i in pixel ]
    elif type(pixel) == int or type(pixel) == np.uint8:
        return format(pixel, "08b")
    else:
        # resolves the errors
        print("\nERROR <LSB_Extractor.py>: input type not supported, terminating process.")
        exit(1)

#
# decodes the message as a string into a file
# -------------------------------------------
def decode_text(output):

    # organizes the bits into a message
    message = ""
    message_aux = bytearray(output)

    # checks when message stops
    for i in range(len(message_aux)):
        try:
            message += message_aux[i:i+1].decode("ascii")
        except UnicodeDecodeError:
            break

    # writes the result into a file
    f = open("Output_LSB_string", "w")
    f.write(message)
    f.close()

#
# decodes the message as a string into a file
# -------------------------------------------
def decode_file(output):

    # converts the result into a file
    f = open("Output_LSB", "wb")
    output.tofile(f)
    f.close()

#
# decodes the message as a file
# -----------------------------
def decode_message(image, n_bits, colorChannel):

    # output of the LSB
    output = bitarray()

    # starts decoding
    for content in image:
        for pixel in content:

            # convert the rgb into binary values
            b, g, r = toBinary(pixel)
            bit = 8 - n_bits

            # finds which case is needed
            match colorChannel:
                case 1:
                    output.extend(r[bit:8])
                case 2:
                    output.extend(g[bit:8])
                case 3:
                    output.extend(b[bit:8])
                case 4:
                    output.extend(r[bit:8])
                    output.extend(g[bit:8])
                case 5:
                    output.extend(r[bit:8])
                    output.extend(b[bit:8])
                case 6:
                    output.extend(g[bit:8])
                    output.extend(r[bit:8])
                case 7:
                    output.extend(g[bit:8])
                    output.extend(b[bit:8])
                case 8:
                    output.extend(b[bit:8])
                    output.extend(r[bit:8])
                case 9:
                    output.extend(b[bit:8])
                    output.extend(g[bit:8])
                case 10:
                    output.extend(r[bit:8])
                    output.extend(g[bit:8])
                    output.extend(b[bit:8])
                case 11:
                    output.extend(r[bit:8])
                    output.extend(b[bit:8])
                    output.extend(g[bit:8])
                case 12:
                    output.extend(g[bit:8])
                    output.extend(r[bit:8])
                    output.extend(b[bit:8])
                case 13:
                    output.extend(g[bit:8])
                    output.extend(b[bit:8])
                    output.extend(r[bit:8])
                case 14:
                    output.extend(b[bit:8])
                    output.extend(r[bit:8])
                    output.extend(g[bit:8])
                case 15:
                    output.extend(b[bit:8])
                    output.extend(g[bit:8])
                    output.extend(r[bit:8])

    # asks user if wants to extract message or file
    print("\nDecode result as a file? If not will be decoded as a string message. (y/n)\n> ", end = " ")
    message = input()

    if message.upper() == "Y" or message.upper() == "YES":
        decode_file(output)
    else:
        decode_text(output)

    # message telling script ended successfully
    print("\n>> Decoding finished with success!")

#
# decode the data in the image
# ----------------------------
def decode_image():

    # gets the file to extract
    print("\nExtract LSB from which file?\n> ", end = " ")
    image_name = input()

    # read the image that contains an hidden message or file and asserts possible errors
    image = cv2.imread(image_name)
    if image is None:
        print("\nERROR <LSB_Extractor.py>: unable to find given image, terminating process.")
        exit(1)

    # ask for the amount of LSB bits
    print("\nHow many LSB bits to extract?\n> ", end = " ")
    n_bits = input()

    # checks if given values were correct
    if not str.isdigit(n_bits):
        print("\nERROR <LSB_Extractor.py>: numbers of bits should be an integer, terminating process.")
        exit(1)
    else:
        if int(n_bits) < 1 or int(n_bits) > 8:
            print("\nERROR <LSB_Extractor.py>: numbers of bits should be between 1 and 8, terminating process.")
            exit(1)

    # transforms it to an int argument
    bits = int(n_bits)

    # asks for color combination
    print("\nWhich color channel's combination?")
    print("\n1 - r / 2 - g / 3 - b / 4 - rg / 5 - rb / 6 - gr / 7 - gb / 8 - br")
    print("\n9 - bg / 10 - rgb / 11 - rbg / 12 - grb / 13 - gbr / 14 - brg / 15 - bgr")
    print("\n> ", end = " ")
    colorChannel = input()

    # checks if values were correct
    if not str.isdigit(colorChannel):
        print("\nERROR <LSB_Extractor.py>: option not available, terminating process.")
        exit(1)
    else:
        if int(colorChannel) > 15 or int(colorChannel) < 1:
            print("\nERROR <LSB_Extractor.py>: option not available, terminating process.")
            exit(1)

    # transforms it to an int argument
    channelCombination = int(colorChannel)

    # sends to function that decodes
    decode_message(image, bits, channelCombination)

#
# starts the script
# -----------------
decode_image()