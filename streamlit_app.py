import os
import streamlit as st
import pandas as pd

# 获取当前目录下的files文件夹中的所有.md和.xlsx文件
def get_files():
    files = os.listdir('files')
    md_files = [f for f in files if f.endswith('.md')]
    xlsx_files = [f for f in files if f.endswith('.xlsx')]
    all_files = md_files + xlsx_files
    # 过滤出文件名以数字开头的文件
    filtered_files = [f for f in all_files if f[0].isdigit()]
    # 按文件名开头的数字排序
    sorted_files = sorted(filtered_files, key=lambda x: int(x.split('_')[0]))
    return sorted_files

# 显示文件内容
def display_file_content(file_name):
    file_path = os.path.join('files', file_name)
    if file_name.endswith('.md'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        st.markdown(content)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(file_path)
        st.dataframe(df)

# 主程序
def main():
    with st.expander("项目说明"):
        st.write("本项目用于展示我在一生一芯项目中的体会和项目要求提交的内容。为了方便编辑，本项目改用markdown和xlsx文件而非streamlit页面。在侧边栏选择要显示的文件，下面是选中的文件内容。")
    
    # 获取排序后的文件列表
    files = get_files()
    
    # 在侧边栏创建单选按钮
    selected_file = st.sidebar.radio("选择文件", [os.path.splitext(f)[0] for f in files])
    
    # 根据选择的文件显示内容
    for file in files:
        if selected_file == os.path.splitext(file)[0]:
            display_file_content(file)
            break

if __name__ == "__main__":
    main()
