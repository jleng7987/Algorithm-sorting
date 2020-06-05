import turtle as t

# 参考网址https://segmentfault.com/a/1190000017867847

# 效果为turtle从坐标原点开始，按逆时针方向画出了一个圆。
# t.circle(100)        # 画一个半径为100的圆
# t.mainloop()  # 等效于t.done()


t.circle(100)        # 从原点开始按逆时针方向画圆，直径为100
t.circle(-100)       # 从鼠标所在点开始按顺时针方向画圆，直径为100
t.mainloop()