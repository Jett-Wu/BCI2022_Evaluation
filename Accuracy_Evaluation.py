import scipy.io as sio
import numpy as np
import os

def calculate_accuracy(pred_path, true_path):
    """
    计算预测标签与真实标签之间的准确率
    
    参数:
    pred_path: 预测标签文件路径 (test_label.mat)
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

    # 加载.mat文件
    try:
        pred_data = sio.loadmat(pred_path)
        true_data = sio.loadmat(true_path)
        
        # 获取标签数据
        # 注意：.mat文件中的变量名可能需要根据实际情况调整
        pred_labels = pred_data['test_label'].flatten()
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
    pred_file = "test_label.mat"
    true_file = "true.mat"
    
    print("当前工作目录:", os.getcwd())
    print("正在查找文件:", pred_file, "和", true_file)
    
    # 计算准确率
    accuracy = calculate_accuracy(pred_file, true_file)
    
    if accuracy is not None:
        print(f"准确率: {accuracy:.5f}")
        print(f"准确率百分比: {accuracy*100:.3f}%")
