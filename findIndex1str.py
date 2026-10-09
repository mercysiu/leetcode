# dieu kien: chuoi can tim < chuoi da co
# thoa dieu kien:
# chay tu dau chuoi den do dai con lai toi thieu de co the chua chuoi can tim:
# kiem tra ki tu dang chay voi ki tu dau tien cua chuoi can tim
# neu co ki tu giong
# kiem tra chuoi tu ki tu dau(dua tren do dai cua chuoi can tim)
# neu co tra ve i
# khong tra ve -1
class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        con = len(haystack) - len(needle)
        for i in range(0, len(haystack)):
            last_point = i + len(needle)
            if i > con:
                return -1
            if haystack[i] == needle[0]:
                if haystack[i: last_point] == needle:
                    return i
        return -1


