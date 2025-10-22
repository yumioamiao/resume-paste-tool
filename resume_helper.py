# resume_helper.py
import tkinter as tk
from tkinter import ttk
import re
import pyperclip  # 需要安装: pip install pyperclip

DATA_FILE = "resume_data.md"
current_data = {}

def load_resume_data():
    """从 Markdown 文件中读取 key: value 数据"""
    global current_data
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        key_value_pairs = {}
        current_key = None
        current_value = []

        for line in lines:
            line = line.rstrip()
            # 匹配 key: value 格式
            match = re.match(r'^\s*([^:#]+?):\s*(.*)$', line)
            if match:
                # 保存上一个 key 的值
                if current_key:
                    key_value_pairs[current_key] = '\n'.join(current_value).strip()
                # 开始新的 key
                current_key = match.group(1).strip()
                current_value = [match.group(2)] if match.group(2) else []
            elif line.startswith('  - ') or line.startswith('    ') and current_key:
                # 处理多行描述（如项目描述）
                current_value.append(line.strip())
            elif line.strip() == '' and current_key:
                continue

        # 保存最后一个
        if current_key:
            key_value_pairs[current_key] = '\n'.join(current_value).strip()

        current_data = key_value_pairs
        return key_value_pairs
    except Exception as e:
        show_status(f"错误：无法读取 {DATA_FILE} - {str(e)}", duration=5000)
        return {}

def create_gui():
    """创建 GUI 界面"""
    root = tk.Tk()
    root.title("秋招简历助手")
    root.geometry("800x600")
    root.configure(padx=10, pady=10)

    # 输入框（只读，用于展示复制的内容）
    tk.Label(root, text="点击按钮复制内容：", font=("Arial", 12)).pack(anchor='w', pady=5)
    display_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=display_var, width=80, font=("Arial", 11), state='readonly')
    entry.pack(fill='x', padx=5, pady=5)

    # 状态标签（显示“已复制”等提示）
    status_var = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_var, fg="green", font=("Arial", 10), height=1)
    status_label.pack(anchor='w', padx=5, pady=2)
    status_var.set("")  # 初始为空

    def show_status(msg, duration=1500):
        """显示状态信息，duration 毫秒后自动清除"""
        status_var.set(msg)
        root.after(duration, lambda: status_var.set("") if status_var.get() == msg else None)

    # 按钮区域（带滚动）
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 创建按钮：点击即复制 value 到剪贴板，并在 entry 显示内容 + 状态提示
    data = load_resume_data()
    num_cols = 3
    for idx, (key, value) in enumerate(data.items()):
        def make_command(val, key_name):
            return lambda: on_button_click(val, key_name, display_var, show_status)

        btn = tk.Button(
            scrollable_frame,
            text=key,
            width=25,
            height=2,
            wraplength=150,
            justify='left',
            anchor='w',
            command=make_command(value, key)
        )
        btn.grid(row=idx // num_cols, column=idx % num_cols, padx=5, pady=3, sticky='w')

    # 控制按钮
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(fill='x', pady=10)

    tk.Button(bottom_frame, text="清空显示", command=lambda: display_var.set("")).pack(side='left', padx=5)
    tk.Button(bottom_frame, text="重新加载数据", command=lambda: reload_data(root)).pack(side='left', padx=5)

    root.mainloop()

def on_button_click(value, key_name, display_var, show_status_func):
    """按钮点击：复制到剪贴板，显示内容，提示“已复制”"""
    if value.strip():
        pyperclip.copy(value)
        display_var.set(value)
        show_status_func(f"✅ '{key_name}' 的内容已复制到剪贴板")
    else:
        display_var.set("")
        show_status_func("⚠️ 内容为空", duration=1000)

def reload_data(root):
    """重新加载数据并刷新界面"""
    for widget in root.winfo_children():
        widget.destroy()
    create_gui()  # 重新创建（简单实现，实际可优化为局部刷新）

if __name__ == "__main__":
    create_gui()