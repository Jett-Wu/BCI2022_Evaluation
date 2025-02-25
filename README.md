# BCI2022 准确率评估工具 (Accuracy Evaluation Tool)

[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

【BCI2022比赛--海南大学脑机接口技术协会（自用）】

基于 fNIRS (功能性近红外光谱成像) 数据的机器学习模型评估工具。支持 .csv 和 .mat 格式的预测结果文件。

## 功能特点 (Features)

- 支持多种格式的预测结果文件 (.csv, .mat)
- 自动识别常见的标签列名和变量名
- 详细的运行信息和错误提示
- 支持中英文输出

## 环境要求 (Requirements)

- Python 3.6+
- 依赖包 (Dependencies)：
  ```bash
  pip install -r requirements.txt
  ```

## 使用说明 (Usage)

### CSV 格式文件评估 (CSV Format)

1. 准备文件 (Prepare Files)：
   - 预测结果：`submission.csv`
   - 真实标签：`true.mat`

2. 运行评估 (Run Evaluation)：
   ```bash
   python Accuracy_Evaluation_csv.py
   ```

CSV 文件要求 (CSV Requirements)：
- 包含预测标签列，支持的列名：
  - 'label', 'Label'
  - 'prediction', 'Prediction'
  - 'class', 'Class'
- 或仅包含单列数据（将自动作为预测标签）

### MAT 格式文件评估 (MAT Format)

1. 准备文件 (Prepare Files)：
   - 预测结果：`submission.mat`
   - 真实标签：`true.mat`

2. 运行评估 (Run Evaluation)：
   ```bash
   python Accuracy_Evaluation_mat.py
   ```

MAT 文件要求 (MAT Requirements)：
- 包含预测标签变量，支持的变量名：
  - 'prediction'
  - 'label'
  - 'test_label'
  - 'pred_label'
- 或使用文件中的第一个非系统变量

## 输出说明 (Output)

程序将输出以下信息：
- 当前工作目录路径
- 待评估文件名称
- 文件中的变量/列名信息
- 最终准确率（小数和百分比形式）

## 注意事项 (Notes)

- 预测标签必须为二元值：
  - 0：静息态 (Rest)
  - 1：运动想象 (Motor Imagery, MI)
- 预测标签数量必须为 160 个样本
- 建议使用标准的列名/变量名以确保正确识别

## 错误处理 (Error Handling)

程序会检查并提示以下错误：
- 文件不存在
- 无法识别的标签列/变量
- 预测标签与真实标签长度不匹配
- 其他运行时错误

## 贡献 (Contributing)

欢迎提交 Issues 和 Pull Requests 来帮助改进代码。

## 许可证 (License)

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。
