def Info ():
    org = str(input("输入数字:"))
    org = list(org)
    return org

def Process_info (orglist):
    table_code = ['00','01','02','10','11','12','20','21','22']
    # -------------0----1----2----3----4----5----6----7----8----
    # tlen = len(table_code)
    olen = len(orglist)
    output_list = ['0','0','0','0','0','0','0','0','0','0',]
    # --------------0---1---2---3---4---5---6---7---8---9---
    i = 0
    while i < olen:
        tlcode = table_code[int(orglist[i])]
        # print(tlcode)
        output_list[2 * i] = tlcode[0]
        output_list[2 * i + 1] = tlcode[1]
        i=i+1

    return output_list

def InfoOutPuter (ListInfo):
    print("**********购物清单**************")
    LFood = ['鸡腿包','迷你小汉堡','猪扒包','海苔沙拉棒','瑞士卷','南瓜棒','牛奶排包','西泽蛋糕','金沙小面包','其它还有什么随便来点']
    LFlen = len(ListInfo)
    i = 0
    while i < LFlen:
        k = int(ListInfo[i])
        if k != 0:
            print(LFood[i],"*",k,"个")
        i = i + 1
    print("******************************")
def main():
    a=0
    InfoOutPuter(Process_info(Info()))
    while a != 885588 :
        a = input()
main()