# _*_coding:utf-8 _*_
# @Author　 : Ric

"""
现有i张十元纸币，k张五元纸币，j张两元纸币，购物后要支付n元(i,j,k,n 为整数)。要求编写一个复杂度为O(1)的函数Changes(i,j,k, n),功能是计算出能否用现在手上拥有的纸币是否足够并能刚好拼凑齐n元，而不需要找零。
1、 如果可以，在屏幕输出一个方案并结束: (例子:“需要2张十元纸币，1张五元纸币，张两元纸币，刚好可凑齐27元”)
2. 如果不可以，在屏幕输出“不能刚好凑齐 n元”。
"""


def solution(i, j, k, n):
    print("你有{}张十元，{}张5元，{}张2元要买{}元东西".format(i, j, k, n))
    if i * 10 + j * 5 + k * 2 < n:
        print("无法找零！！")
    money = n
    temp = 0
    ten = money // 10
    if ten <= i:
        if money % 2 == 0:
            if money % 10 // 2 <= k:
                print("需要{}张10元，{}张2元".format(ten, money % 10 // 2))
            else:
                print("无法找零")

        else:
            if j <= 0:
                print("无法找零")
            else:
                if money % 5 == 0:
                    if j < 3:
                        print("无法找零")
                    else:
                        print("需要{}张10元，{}张5元".format(ten - 1, (money - ten * 10 + 10) // 5))
                else:
                    if (money % 10 + 5) // 2 > k:
                        print("无法找零")
                    else:
                        print("需要{}张10元，1张5元,{}张2元".format(ten - 1, (money % 10 + 5) // 2))
    else:
        if money % 2 == 0:
            temp = money - 10 * i
            if money % 10 // 2 > k:
                print("无法找零")
            else:
                temp = temp // 10 * 10
                if temp <= j * 5:
                    print("需要{}张10元，{}张5元,{}张2元".format(i, temp // 5, money % 10 // 2))
                else:
                    if j % 2 == 0:
                        if (temp - j * 5) // 2 > k - money % 10 // 2:
                            print("无法找零")
                        else:
                            print("需要{}张10元，{}张5元,{}张2元".format(i, j, (temp - j * 5) // 2))
                    else:
                        if (temp - (j - 1) * 5) // 2 > k - money % 10 // 2:
                            print("无法找零")
                        else:
                            print("需要{}张10元，{}张5元,{}张2元".format(i, j - 1, (money - 10 * i - (j - 1) * 5) // 2))
        else:
            if j <= 0:
                print("无法找零")
            else:
                if (money % 10 + 5) // 2 > k:
                    print("不")
                else:
                    temp = (money - (i + 1) * 10) // 10 * 10
                    if temp <= (j - 1) * 5:
                        print("需要{}张10元，{}张5元,{}张2元".format(i, temp // 5 + 1, (money % 10 + 5) // 2))
                    else:
                        if (j - 1) % 2 == 0:
                            if (temp - (j - 1) * 5) // 2 > (k - money % 10 + 5) // 2:
                                print("无法找零")
                            else:
                                print("需要{}张10元，{}张5元,{}张2元".format(i, j, (money - 10 * i - j * 5) // 2))
                        else:
                            if (temp - (j - 2) * 5) // 2 > k - (money % 10 + 5) // 2:
                                print("无法找零")
                            else:
                                print("需要{}张10元，{}张5元,{}张2元".format(i, j - 1, (money % 10 + 5) // 2))


if __name__ == '__main__':
    print("------")
    solution(10, 3, 6, 122)
    print("------")
    solution(10, 3, 5, 122)
    print("------")
    solution(10, 4, 6, 122)
    print("------")
    solution(10, 4, 6, 131)
    print("------")
    solution(10, 5, 6, 131)
    print("------")
    solution(20, 5, 6, 131)
