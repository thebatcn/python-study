import tkinter as tk
from datetime import datetime, timedelta

def calculate_days():
    start_date = datetime.strptime(entry_start_date.get(), '%Y-%m-%d')
    end_date = datetime.strptime(entry_end_date.get(), '%Y-%m-%d')
    delta = end_date - start_date
    label_result.config(text=f"日期之间的天数差异为：{delta.days} 天")

datetime.strftime()
# 创建窗口
window = tk.Tk()
window.title("日期计算器")

# 创建标签和输入框
label_start_date = tk.Label(window, text="开始日期（YYYY-MM-DD）：")
label_start_date.pack()
entry_start_date = tk.Entry(window)
entry_start_date.pack()

label_end_date = tk.Label(window, text="结束日期（YYYY-MM-DD）：")
label_end_date.pack()
entry_end_date = tk.Entry(window)
entry_end_date.pack()

# 创建计算按钮
button_calculate = tk.Button(window, text="计算", command=calculate_days)
button_calculate.pack()

# 显示结果的标签
label_result = tk.Label(window, text="")
label_result.pack()

# 运行窗口主循环
window.mainloop()
