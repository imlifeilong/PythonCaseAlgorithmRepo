def main(n):
    bin_text = bin(int(n))[2:]
    result = []
    for i in range(len(bin_text), 0, -7):
        # 左右 边界
        right = i
        left = i - 7 if i > 7 else 0
        sub_bin_text = bin_text[left:right]

        sub_bin_text_length = len(sub_bin_text)
        # 字节长度不够7位，用0补充
        if sub_bin_text_length < 7:
            # sub_bin_text = '0' * (7 - sub_bin_text_length) + sub_bin_text
            sub_bin_text = sub_bin_text.zfill(7)
        # 截取的长度小于7说明后面没有数据了，用0补充
        if i - 7 <= 0:
            real_sub_bin_text = '0' + sub_bin_text
        else:
            real_sub_bin_text = '1' + sub_bin_text
        # zfill(2) 字符长度小于2时，前面用0填充
        hex_text = hex(int(real_sub_bin_text, 2)).upper()[2:].zfill(2)

        result.append(hex_text)
    print(''.join(result))


n = '1000'
main(n)
