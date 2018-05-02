# coding=utf-8from pwn import *n = 0xBACA954B2835186EEE1DAC2EF38D7E11582127FB9E6107CCAFE854AE311C07ACDE3AAC8F0226E1435D53F03DC9CE6701CF9407C77CA9EE8B5C0DEE300B11DD4D6DC33AC50CA9628A7FB3928943F90738BF6F5EC39F786D1E6AD565EB6E0F1F92ED3227658FDC7C3AE0D4017941E1D5B27DB0F12AE1B54664FD820736235DA626F0D6F97859E5969902088538CF70A0E8B833CE1896AE91FB62852422B8C29941903A6CF4A70DF2ACA1D5161E01CECFE3AD80041B2EE0ACEAA69C793D6DCCC408519A8C718148CF897ACB24FADD8485588B50F39BCC0BBF2BF7AD56A51CB3963F1EB83D2159E715C773A1CB5ACC05B95D2253EEFC3CCC1083A5EF279AF06BB92Fe = 0x10001s_box = [    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]def pad(s):    ret = ['\x00' for _ in range(256)]    for index, pos in enumerate(s_box):        ret[pos] = s[index]    return ''.join(ret)def str2int(s):    return int(s.encode('hex'), 16)def mul(x, y, z):    ret = 1    while y != 0:        if y & 1 != 0:            ret = (ret * x) % z        x = (x * x) % z        y >>= 1    return retflag = ""num = 255while len(flag) != 38:    p = remote("123.59.138.211", 23333)    p.recvuntil("choice :")    p.sendline("1")    p.recvuntil(": ")    p.sendline(chr(num) * 218)    p.recvuntil("Success")    p.sendline("1")    p.recvuntil(": ")    s = '\x02' * num    p.sendline(s)    p.recvuntil("Success")    p.sendline("2")    p.recvuntil("0x")    br = int(r.recvline().replace("\n",""),16)    for c in range(20,128):        if br == mul(str2int(pad(flag + chr(c) + s)), e, n):            flag += chr(c)            break    num = num - 1    p.close()print flag