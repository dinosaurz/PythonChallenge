import string

lvl = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr \
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr\
ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() \
gq pcamkkclbcb. lmu ynnjw ml rfc spj"
rot = string.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab")

trans = string.translate(lvl, rot)
print trans
