from transformers import AutoTokenizer, BertForSequenceClassification

# 初始化tokenizer和模型
tokenizer = AutoTokenizer.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
model = BertForSequenceClassification.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
config = model.config

def predict_icd_code(text):
    # 编码输入文本
    encoded_input = tokenizer(text, return_tensors='pt')
    
    # 获取模型输出
    output = model(**encoded_input)
    
    # 处理输出，获取前5个预测的ICD-10代码
    results = output.logits.detach().cpu().numpy()[0].argsort()[::-1][:5]
    answer = [config.id2label[ids] for ids in results]
    
    return answer

# 示例调用
text = "autism"
predicted_codes = predict_icd_code(text)
print(predicted_codes)
