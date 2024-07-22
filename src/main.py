import json
import sys

def load_data(filepath):
    # 加载JSON文件数据

    data = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                data.append(json.loads(line))

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        data = []

    # print(f"Loaded data from {filepath}: {data}")

    return data

def select_course(student, courses) -> dict:
    # 选课

    course_id = input("请输入课程ID：")
    flag = False

    for course in courses:
        if course['id'] == course_id:
            flag = True

            # 检查是否已选课 / 时间冲突
            for selected_course_id in student['selected']:
                if selected_course_id == course_id:
                    print(f"课程ID：{course_id} 已选。")
                    return student
                else:
                    for selected_course in courses:
                        if selected_course['id'] == selected_course_id:
                            if selected_course['time'] == course['time']:
                                print(f"课程 {course_id} 与 {selected_course_id} 时间冲突。")
                                return student

            student['selected'].append(course_id)
            print(f"选课成功：{course['name']}")
            break

    if not flag:
        print(f"未找到课程ID：{course_id}")


    return student

def view_selected_courses(student):
    # 查看已选课程

    print(f"姓名：{student['name']}")
    if len(student['selected']) == 0:
        print("未选课程")
    else:
        print(f"已选课程：{student['selected']}")

def save_data(filepath, data):
    # 保存数据到JSON文件

    try:
        with open(filepath, 'w') as file:
            for item in data:
                file.write(json.dumps(item) + '\n')

    except FileNotFoundError:
        print(f"File not found: {filepath}")


def print_menu():
    print("\n选课系统菜单：")
    print("1. 选课")
    print("2. 查看已选课程")
    print("3. 退出")

def main(student_file, courses_file):
    students = load_data(student_file)
    courses = load_data(courses_file)

    while True:
        print_menu()
        choice = input("请选择一个操作（1-3）：")

        if choice == '1': # 选课

            student_id = input("请输入学生ID：")
            flag = False
            for index, student in enumerate(students):
                if student['id'] == student_id:
                    flag = True
                    student_selected = select_course(student, courses)
                    students[index] = student_selected # 更新学生数据
                    break

            if not flag: # 学生不存在时新建学生信息
                print(f"新学生ID：{student_id}")
                student = {
                    'id': student_id,
                    'name': input("请输入学生姓名："),
                    'selected': []
                }
                student_selected = select_course(student, courses)
                students.append(student_selected)


        elif choice == '2': # 查看已选课程

            student_id = input("请输入学生ID：")
            flag = False
            for student in students:
                if student['id'] == student_id:
                    flag = True # 标记找到了学生
                    view_selected_courses(student)
                    break

            if not flag:
                print(f"未找到学生ID：{student_id}")

        elif choice == '3':
            print("退出系统。")
            break
        else:
            print("无效的输入，请重新选择。")

    # 保存学生数据
    save_data(student_file, students)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <student_filepath> <courses_filepath>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
