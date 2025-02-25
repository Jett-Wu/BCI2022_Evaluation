import scipy.io as sio
import numpy as np
import os

def calculate_accuracy(pred_path, true_path):
    """
    计算预测标签与真实标签之间的准确率
    
    参数:
    pred_path: 预测标签文件路径 (submission.mat)
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
        # 加载.mat文件
        pred_data = sio.loadmat(pred_path)
        true_data = sio.loadmat(true_path)
        
        # 获取标签数据
        # 尝试不同的可能的变量名
        possible_names = ['prediction', 'label', 'test_label', 'pred_label']
        pred_labels = None
        
        # 打印可用的变量名，帮助调试
        print(f"submission.mat 文件包含以下变量: {list(pred_data.keys())}")
        
        # 尝试所有可能的变量名
        for name in possible_names:
            if name in pred_data:
                pred_labels = pred_data[name].flatten()
                print(f"使用变量名 '{name}' 读取预测标签")
                break
                
        if pred_labels is None:
            # 如果找不到预定义的变量名，尝试使用第一个非系统变量
            valid_keys = [k for k in pred_data.keys() if not k.startswith('__')]
            if valid_keys:
                first_key = valid_keys[0]
                pred_labels = pred_data[first_key].flatten()
                print(f"使用变量名 '{first_key}' 读取预测标签")
            else:
                raise ValueError(f"在submission.mat中找不到预测标签。请确保文件包含以下变量之一: {possible_names}")
        
        # 获取真实标签
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
    pred_file = "submission.mat"
    true_file = "true.mat"
    
    print("当前工作目录:", os.getcwd())
    print("正在查找文件:", pred_file, "和", true_file)
    
    # 计算准确率
    accuracy = calculate_accuracy(pred_file, true_file)
    
    if accuracy is not None:
        print(f"准确率: {accuracy:.5f}")
        print(f"准确率百分比: {accuracy*100:.3f}%")
