import utils

#Hex notation of ciphertext1 file using hex editor online
c1 = "72efd8a5f04bb1df13996b2a492f1c1a2445fcaf57d4dac988a6822b22817988d695c04ffa91402010c29b7982b2de303e640fde65678a464bb9ff0f1a2e095d3bfd27edea927a179bfe11eaec10b3e149fdc593da6753b6e52c06fc0de76a58dd09656938fcf3a4e7748c9f39d74c49400daa08848d37f07ed3b322d2b6bff8e526c9e7408ac06dba3253a72aab7d97d1503625f78ac56c73834929ba5b04ba8b28edda61463eb73ea1e7c45d4b8182830ca089e4fbff79a693d61b81563b385637f2090fa8866628a406435fe6e9dd709c2e2bb0a9da7471b98ff4b012d96422b6c9d016524820091381d2be22e0da1c695591a2ca8fc23b309ce1f73511f20024721cacd05cba8b18a2de7ccc5b796013098b0d4637199de9ae54bdffed58122f4ba99967a16e4f33590d";

#Hex notation of ciphertext2 file using hex editor online
c2 = "6bf381bfe207b98c40956933516a5a002642fce25bc3dac0cdb49622208678d7d689c902f9dd1d794090997ac5f7cf2f2b2a14982c47cf5e4fa5ff311c200f5d64b531e1e6d174569ef60eb3ae1eb8e01ee18097c63555bbe42c11fc40ff6b599b016d6734eebfbbf6359f9c75f145460e19ac15909373d077dbb17e8bc2b6f3a175f7e14ccdc078e97543ad3aab399ddd502a23e7c28c4063834129ba540beeab33f895675d7fad22e485de405ad5ab860cb2dda9c0d318dadddd16c4707219461aef0a19a8a97a33ac546e5ffee9d4718f2c62b3eccd7a249e8facb815d53736a8dd9f0a49497400569fddec08e08217785fd8e6d489c06936d3e4ec7b0bb301623018eed946bbc54eb69b22dc06387e0b408d07163d0c9dc5a01dbbedfb43073e1fd5dc60a8784a284e4a";

c1_bin = utils.hex2Bin(c1);
c2_bin = utils.hex2Bin(c2);
res1 = utils.xor(c1_bin, c2_bin);

res1_hex = utils.bin2Hex(res1);

fh = open("originalText.txt", "w");
trial_seq = "is";
for i in range(1, len(c1_bin) - len(trial_seq)+1):
    t1 = trial_seq.rjust(i)
    t1_str = t1 * (len(c1_bin) // len(t1))
    trial_str_bin = utils.ascii2Bin(t1_str)
    t = utils.xor(res1, trial_str_bin)
    t_ascii = utils.bin2Ascii(t)
    fh.write(t_ascii + '\n')
    fh.write('\n')

fh.close();
