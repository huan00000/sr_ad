import urllib.request

# 原 GitHub 文件的直链
SOURCE_URL = "https://raw.githubusercontent.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever/refs/heads/release/sr_ad_only.conf"

def fetch_and_clean():
    try:
        # 下载原文件
        req = urllib.request.urlopen(SOURCE_URL)
        lines = req.read().decode('utf-8').splitlines()
    except Exception as e:
        print(f"下载失败: {e}")
        return

    clean_rules = []
    
    for line in lines:
        line = line.strip()
        # 跳过注释行、空行和 [Rule] 标签
        if not line or line.startswith('#') or line.startswith('['):
            continue
            
        # 按照逗号分割
        parts = line.split(',')
        
        # 只要包含至少两个部分（比如 DOMAIN-SUFFIX 和 域名），我们就提取前两部分
        if len(parts) >= 2:
            rule_type = parts[0]
            domain = parts[1]
            # 重新组合，不带后面的 Reject
            clean_rules.append(f"{rule_type},{domain}")

    # 将清洗后的规则写入新文件
    with open("sr_ad_clean.txt", "w", encoding='utf-8') as f:
        f.write("# 自动提取自 Johnshall 仓库，已去除策略(Reject)\n")
        f.write("\n".join(clean_rules))
        f.write("\n")
        
    print("规则转换完成并保存为 sr_ad_clean.txt")

if __name__ == "__main__":
    fetch_and_clean()
