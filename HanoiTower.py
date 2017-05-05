# coding:utf-8
import datetime

'''
汉诺塔规则：
背景：3根柱子，其中一根柱子上从上到下，从小到大依次放着64个盘子
目标：把所有盘子移动到另外一根柱子上
要求：每次只能移动一个盘子，小盘子必须在大盘子上面
假设：三根柱子分别为a,b,c  64个盘子在a上，需要移动到c上
'''

STEP = []
COUNT = 0


def mov(n, a, b, c):
    global COUNT
    try:
        if n == 1:
            # STEP.append('%s号盘:' % str(n) + a + '->' + c)
            print '%s号盘:' % str(n) + a + '->' + c
            COUNT += 1
            return
        mov(n - 1, a, c, b)
        # STEP.append('%s号盘:' % str(n) + a + '->' + c)
        print '%s号盘:' % str(n) + a + '->' + c
        COUNT += 1
        mov(n - 1, b, a, c)
    except:
        print "Error!"


if __name__ == '__main__':
    begin = datetime.datetime.now()
    mov(64, 'A', 'B', 'C')
    end = datetime.datetime.now()
    print "总共需:" + str(COUNT) + "步"
    print "耗时：" + str(end - begin)
