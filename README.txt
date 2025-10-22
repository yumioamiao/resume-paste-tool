🧾 秋招简历助手 Resume Helper Tool
一键复制简历内容，告别重复填写，专为高效秋招而生 💼



🌟 项目简介

在秋招过程中，你是否也厌倦了在各个招聘网站重复填写相同的简历信息？
简历助手 就是为解决这个问题而生！

它是一个轻量级桌面工具，通过结构化管理你的简历内容（如实习经历、项目描述等），让你只需点击一个按钮，就能将对应内容复制到剪贴板，直接粘贴使用。

🎯 目标：提升简历填写效率 10 倍，把时间留给更重要的事情。

🚀 核心功能

功能 说明
------ ------
🔑 结构化数据 使用 key: value 格式管理简历信息（resume_data.md）
🖱️ 一键复制 点击按钮 → 自动复制内容到剪贴板
👁️ 内容预览 在输入框中实时显示复制的文本
🟢 静默提示 状态栏显示“已复制”，1.5 秒后自动消失，不打扰
💾 数据分离 简历内容与代码分离，便于维护和更新
📦 可打包运行 支持打包为 .exe，Windows 用户可直接运行

📦 快速开始
1. 安装依赖

bash
pip install -r requirements.txt
2. 编辑简历数据

打开 resume_data.md，按格式填写你的信息：

markdown
项目经历
项目1名称: 分布式缓存系统
项目1描述: >
基于 Redis + 一致性哈希实现分布式缓存
QPS 提升 5 倍，缓存命中率 92%
使用 Go 编写核心模块
3. 运行程序

bash
python resume_helper.py
4. （可选）打包为独立 exe（Windows）

bash
pyinstaller --onefile --windowed resume_helper.py

生成的 .exe 文件位于 dist/ 目录，可直接分发使用。

📂 项目结构

resume-helper/
├── resume_helper.py # 主程序 (GUI + 逻辑)
├── resume_data.md # 简历数据源 (key: value)
├── requirements.txt # 依赖列表
├── README.md # 本说明文件
└── demo.png # (可选) 界面截图

🧩 依赖说明
[pyperclip](https://pypi.org/project/pyperclip/)：用于剪贴板操作
tkinter：Python 内置 GUI 库，无需安装

安装命令：
bash
pip install pyperclip

🛠️ 后续优化计划
🔍 添加搜索功能，快速定位字段
📁 支持分类折叠（教育、实习、项目）
✏️ 增加编辑模式，直接在 GUI 中修改
📄 支持导出为 PDF / Word
🌐 多语言支持（中英文切换）

欢迎提交 Issue 或 PR！

📜 开源许可

本项目采用 [MIT License](LICENSE) 开源，欢迎学习、使用和改进。

🙌 致谢

感谢你在秋招路上的坚持！
希望这个小工具能为你节省时间，多准备一场面试，多拿下一个 Offer！

🎯 GitHub 地址: https://github.com/yumioamiao/resume-paste-tool
由 @yumioamiao 开发 秋招加油 💪