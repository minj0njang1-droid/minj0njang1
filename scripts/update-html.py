#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML 업데이트 스크립트
분석 결과를 index.html에 반영
"""

import json
import re
from datetime import datetime

def update_html():
    """분석 결과를 index.html에 업데이트합니다."""
    
    # 분석 결과 읽기
    try:
        with open('data/analysis.json', 'r', encoding='utf-8') as f:
            analysis = json.load(f)
        
        with open('data/news.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
    except FileNotFoundError as e:
        print(f"❌ 파일을 찾을 수 없습니다: {e}")
        return False
    
    # index.html 읽기
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("❌ index.html 파일을 찾을 수 없습니다!")
        return False
    
    print("📝 HTML 업데이트 시작...")
    
    # stockData 업데이트
    defensive_data = json.dumps(analysis['defensive'][:10], ensure_ascii=False, indent=12)
    aggressive_data = json.dumps(analysis['aggressive'][:10], ensure_ascii=False, indent=12)
    
    # stockData 패턴 찾기 및 교체
    stock_data_pattern = r'const stockData = \{[\s\S]*?\};'
    new_stock_data = f'''const stockData = {{
            defensive: {defensive_data},
            aggressive: {aggressive_data}
        }};'''
    
    html_content = re.sub(stock_data_pattern, new_stock_data, html_content)
    
    # newsData 업데이트
    news_items = news_data.get('news', [])[:5]  # 최대 5개
    news_data_str = json.dumps(news_items, ensure_ascii=False, indent=12)
    
    news_data_pattern = r'const newsData = \[[\s\S]*?\];'
    new_news_data = f'const newsData = {news_data_str};'
    
    html_content = re.sub(news_data_pattern, new_news_data, html_content)
    
    # 업데이트 시간 표시
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time_pattern = r'(<!-- 매일 오전 8시 업데이트 -->)'
    new_time = f'<!-- 매일 오전 8시 업데이트 --> <!-- 마지막 업데이트: {update_time} -->'
    
    html_content = re.sub(time_pattern, new_time, html_content)
    
    # index.html 저장
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ HTML 업데이트 완료!")
    print(f"   - 안정형: {len(analysis['defensive'])}개")
    print(f"   - 공격형: {len(analysis['aggressive'])}개")
    print(f"   - 뉴스: {len(news_items)}개")
    print(f"   - 업데이트 시간: {update_time}")
    
    return True

if __name__ == '__main__':
    print("🔄 HTML 업데이트 시작...")
    success = update_html()
    if success:
        print("✅ 완료!")
    else:
        print("❌ 실패!")
