# Credit @NGROCKER
# Please Don't remove credit.
# Born to make history @NGROCKER !
# Thank you NGROCKER for helping us in this Journey
# 🥰  Thank you for giving me credit @NGROCKER  🥰
# for any error please contact me -> telegram @NGROCKERr or insta @NGROCKERr 
# rip paid developers 🤣 - >> No need to buy paid source code while @NGROCKER is here 😍😍
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
