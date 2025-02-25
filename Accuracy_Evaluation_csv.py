import scipy.io as sio
import numpy as np
import os
import pandas as pd

def calculate_accuracy(pred_path, true_path):
    """
    计算预测标签与真实标签之间的准确率
    
    参数:
    pred_path: 预测标签文件路径 (submission.csv)
    true_path: 真实标签文件路径 (true.mat)
    
    返回:
    accuracy: 准确率
    """
    # 检查文件是否存在
    if not os.path.exists(pred_path):
        print(f"错误: 找不到预测标签文件 '{pred_path}'")
        print(f"请确保文件 '{pred_path}' 在当前目录: {os.getcwd()}")
        return None
        
    if not os.path.exists(true_path):
        print(f"错误: 找不到真实标签文件 '{true_path}'")
        print(f"请确保文件 '{true_path}' 在当前目录: {os.getcwd()}")
        return None

    try:
        # 加载CSV文件
        pred_data = pd.read_csv(pred_path)
        
        # 检查CSV文件的列名
        columns = pred_data.columns.tolist()
        print(f"CSV文件包含以下列: {columns}")
        
        # 尝试不同的可能的列名
        label_column = None
        possible_names = ['label', 'Label', 'prediction', 'Prediction', 'class', 'Class']
        
        for col_name in possible_names:
            if col_name in pred_data.columns:
                label_column = col_name
                break
                
        if label_column is None:
            # 如果只有一列，直接使用第一列
            if len(pred_data.columns) == 1:
                label_column = pred_data.columns[0]
            else:
                raise ValueError(f"在CSV文件中找不到标签列。请确保文件包含以下列名之一: {possible_names}\n"
                               f"或者确保CSV文件只包含一列预测标签。")
        
        # 获取预测标签列
        pred_labels = pred_data[label_column].values
        
        # 加载.mat文件中的真实标签
        true_data = sio.loadmat(true_path)
        true_labels = true_data['test_label'].flatten()
        
        # 确保标签长度相同
        if len(pred_labels) != len(true_labels):
            raise ValueError("预测标签和真实标签的长度不一致！")
            
        # 计算真阳性和真阴性
        true_positives = np.sum((pred_labels == 1) & (true_labels == 1))
        true_negatives = np.sum((pred_labels == 0) & (true_labels == 0))
        
        # 计算总样本数
        total_samples = len(true_labels)
        
        # 计算准确率
        accuracy = (true_positives + true_negatives) / total_samples
        
        return accuracy
        
    except Exception as e:
        print(f"错误: {str(e)}")
        return None

if __name__ == "__main__":
    # 文件路径
    pred_file = "submission.csv"
    true_file = "true.mat"
    
    print("当前工作目录:", os.getcwd())
    print("正在查找文件:", pred_file, "和", true_file)
    
    # 计算准确率
    accuracy = calculate_accuracy(pred_file, true_file)
    
    if accuracy is not None:
        print(f"准确率: {accuracy:.5f}")
        print(f"准确率百分比: {accuracy*100:.3f}%") 