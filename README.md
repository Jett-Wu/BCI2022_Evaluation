# 准确率评估工具

【BCI2022比赛--海南大学脑机接口技术协会（自用）】

这是一个用于评估 fNIRS 数据识别算法准确率的 Python 工具。

## 使用说明

1. **文件准备**
   - 将您的预测结果文件 `test_label.mat` 放在本目录下
   - 真实标签文件 `true.mat` 已预置在目录中

2. **环境要求**
   - Python 3.x
   - 需要安装的依赖包：
     - scipy
     - numpy
   
3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **运行评估**
   ```bash
   python Accuracy_Evaluation.py
   ```

5. **输出结果**
   - 程序将显示准确率（小数形式）
   - 同时显示百分比形式的准确率

## 注意事项
- 确保 `test_label.mat` 文件中的预测标签格式正确（0表示静息，1表示MI）
- 预测标签数量应为160个样本
- 如遇到问题，程序会显示详细的错误信息 
