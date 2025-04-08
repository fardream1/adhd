################################################
# 非全局，子模块内部使用的default or constant values
# D, default; C, constant, S, setting
################################################
import types

D_SIMILITY_THRESHOLD = 0.8     # default threshold for similarity
D_SIMILITY_METHOD = 'cosine'   # default method for similarity

# GPT default limit is 8,192 tokens, 约 32,768 characters(英语 1 token 约4 char; 中文1 token 约 1 hanzi，in+out);
# GPT-4-32K 32,768 tokens, 约 131,072 characters
D_MAX_PROMPT_LEN = 4000        # default max length of prompt

# 项目数据存放位置及SCHEMA文件名
S_TRAINING_PATH = 'training'
S_PROMPT_FILE = 'LLM/prompt.txt'         # prompt file name

if __name__ == '__main__':
    all_vars = locals()

    # 收集所有需要转换的变量
    to_convert = {var_name: var_value for var_name, var_value in all_vars.items() if isinstance(var_value, dict)}

    # 将所有字典类型的变量转换为 MappingProxyType
    for var_name, var_value in to_convert.items():
        all_vars[var_name] = types.MappingProxyType(var_value)

    # 打印所有变量名和类型
    for var_name, var_value in all_vars.items():
        print(f"{var_name}: {type(var_value)}")
