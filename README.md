# 选课系统

## 简介

这是一个简单的选课系统，实现了基础的选课、查看已选课程和保存选课信息的功能。

## 如何运行

1. 确保Python环境已安装。
2. 在命令行中，导航到项目目录。
3. 运行命令 `python src/main.py data/student.jsonl data/courses.jsonl`

   其中 `data/student.jsonl` 和 `data/courses.jsonl` 是包含学生信息和课程信息的文件。

## 功能说明

- **启动**：通过命令行参数指定学生信息和课程信息的文件路径。
- **读取**：读取并解析JSON文件中的学生信息和课程信息。
- **选课**：根据课程列表选择课程。
- **查看**：查看已选的课程列表。
- **保存**：将学生的选课信息保存到文件中。

## 已完成

- 补全 `load_data` 函数以加载JSON文件数据。
- 实现 `select_course` 函数以完成选课逻辑。
- 实现 `view_selected_courses` 函数以查看已选课程。
- 实现 `save_data` 函数以保存数据到JSON文件。
