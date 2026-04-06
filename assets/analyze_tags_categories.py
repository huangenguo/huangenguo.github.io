#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分类和标签分析工具

功能：
1. 分析站点所有文章的分类和标签使用情况
2. 统计各类别和标签的使用频率
3. 基于文章内容智能推荐分类和标签
4. 生成分类和标签的使用报告

使用方法：
1. 在站点根目录运行：python analyze_tags_categories.py
2. 输入文章内容或文件路径，获取推荐的分类和标签
3. 查看分类和标签的使用统计报告
"""

import os
import re
import sys
import json
from collections import Counter

# 站点根目录
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(SITE_ROOT, '_posts')

class CategoryTagAnalyzer:
    def __init__(self):
        self.posts = []
        self.categories = Counter()
        self.tags = Counter()
        self.category_pattern = re.compile(r'categories:\s*\n(\s*-.*\n)+', re.MULTILINE)
        self.tag_pattern = re.compile(r'tags:\s*\n(\s*-.*\n)+', re.MULTILINE)
        self.item_pattern = re.compile(r'\s*-\s*(.+)')
    
    def load_posts(self):
        """加载所有文章并分析分类和标签"""
        for filename in os.listdir(POSTS_DIR):
            if filename.endswith('.md'):
                filepath = os.path.join(POSTS_DIR, filename)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                # 提取分类
                cat_match = self.category_pattern.search(content)
                if cat_match:
                    cat_section = cat_match.group(0)
                    cats = self.item_pattern.findall(cat_section)
                    for cat in cats:
                        self.categories[cat.strip()] += 1
                
                # 提取标签
                tag_match = self.tag_pattern.search(content)
                if tag_match:
                    tag_section = tag_match.group(0)
                    tags = self.item_pattern.findall(tag_section)
                    for tag in tags:
                        self.tags[tag.strip()] += 1
                
                # 保存文章信息
                self.posts.append({
                    'filename': filename,
                    'content': content
                })
    
    def get_category_recommendations(self, content):
        """基于内容推荐分类"""
        # 简单的关键词匹配
        category_keywords = {
            'Tech': ['技术', '编程', '代码', '开发', '软件', '硬件', 'AI', '人工智能', '科技'],
            'Education': ['教育', '学习', '教学', '课程', '培训', '知识'],
            'Blog': ['博客', '心得', '经验', '分享', '随笔'],
            'Life': ['生活', '日常', '感悟', '故事'],
            'Tutorial': ['教程', '指南', '入门', '实战', '例子']
        }
        
        scores = {}
        for category, keywords in category_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in content:
                    score += 1
            scores[category] = score
        
        # 按得分排序
        sorted_categories = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [cat for cat, score in sorted_categories if score > 0]
    
    def get_tag_recommendations(self, content, max_tags=5):
        """基于内容推荐标签"""
        # 从现有标签中匹配
        matched_tags = []
        for tag, count in self.tags.items():
            if tag in content and count > 0:
                matched_tags.append((tag, count))
        
        # 按使用频率排序
        matched_tags.sort(key=lambda x: x[1], reverse=True)
        return [tag for tag, count in matched_tags[:max_tags]]
    
    def generate_report(self):
        """生成分类和标签使用报告"""
        report = {
            'total_posts': len(self.posts),
            'categories': dict(self.categories),
            'tags': dict(self.tags),
            'top_categories': self.categories.most_common(10),
            'top_tags': self.tags.most_common(20)
        }
        return report
    
    def analyze_file(self, filepath):
        """分析单个文件"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        recommended_categories = self.get_category_recommendations(content)
        recommended_tags = self.get_tag_recommendations(content)
        
        return {
            'recommended_categories': recommended_categories,
            'recommended_tags': recommended_tags
        }
    
    def analyze_content(self, content):
        """分析文本内容"""
        recommended_categories = self.get_category_recommendations(content)
        recommended_tags = self.get_tag_recommendations(content)
        
        return {
            'recommended_categories': recommended_categories,
            'recommended_tags': recommended_tags
        }

def main():
    analyzer = CategoryTagAnalyzer()
    analyzer.load_posts()
    
    print("=== 分类和标签分析工具 ===")
    print(f"分析了 {len(analyzer.posts)} 篇文章")
    print()
    
    # 显示分类统计
    print("=== 分类使用情况 ===")
    for category, count in analyzer.categories.most_common():
        print(f"{category}: {count} 篇")
    print()
    
    # 显示标签统计
    print("=== 标签使用情况（前20个）===")
    for tag, count in analyzer.tags.most_common(20):
        print(f"{tag}: {count} 篇")
    print()
    
    # 交互式分析
    while True:
        print("请选择操作：")
        print("1. 分析文件")
        print("2. 分析文本内容")
        print("3. 退出")
        
        choice = input("输入选项: ")
        
        if choice == '1':
            filepath = input("请输入文件路径: ")
            if os.path.exists(filepath):
                result = analyzer.analyze_file(filepath)
                print("推荐分类:", result['recommended_categories'])
                print("推荐标签:", result['recommended_tags'])
            else:
                print("文件不存在！")
        
        elif choice == '2':
            print("请输入文本内容（输入 'EOF' 结束）:")
            lines = []
            while True:
                line = input()
                if line.strip() == 'EOF':
                    break
                lines.append(line)
            content = '\n'.join(lines)
            result = analyzer.analyze_content(content)
            print("推荐分类:", result['recommended_categories'])
            print("推荐标签:", result['recommended_tags'])
        
        elif choice == '3':
            break
        
        print()

if __name__ == '__main__':
    main()