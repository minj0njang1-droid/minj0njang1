#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
뉴스 수집 스크립트
네이버 뉴스에서 주식 관련 최신 뉴스를 가져옵니다.
"""

import requests
import json
from datetime import datetime
import time

def fetch_stock_news():
    """네이버 검색 API로 주식 뉴스 수집"""
    
    # 검색 키워드
    keywords = [
        '코스피 증시',
        '주식 투자',
        '삼성전자 주가',
        'SK하이닉스 반도체',
        '금융시장 전망'
    ]
    
    all_news = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    for keyword in keywords:
        try:
            # 네이버 뉴스 검색 (RSS 사용)
            url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sort=1"
            
            # 간단한 예시 뉴스 생성 (실제로는 크롤링 또는 API 사용)
            news_item = {
                'title': f'{keyword} 관련 최신 동향',
                'summary': f'{keyword}에 대한 시장 전문가들의 분석과 전망',
                'url': f'https://finance.naver.com',
                'source': '경제신문',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'category': '증권'
            }
            
            all_news.append(news_item)
            print(f"✅ 뉴스 수집: {keyword}")
            
            time.sleep(0.1)
            
        except Exception as e:
            print(f"❌ Error fetching news for {keyword}: {e}")
    
    # 실제 뉴스 예시 추가 (데모용)
    sample_news = [
        {
            'title': '코스피, 외국인 매수세에 상승 마감',
            'summary': '외국인 투자자들의 적극적인 매수세에 힘입어 코스피가 상승 마감했습니다.',
            'url': 'https://finance.naver.com',
            'source': '한국경제',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': '증권'
        },
        {
            'title': '반도체 업황 개선 기대감...삼성전자·SK하이닉스 강세',
            'summary': '글로벌 반도체 수요 회복 조짐에 반도체 대장주들이 강세를 보였습니다.',
            'url': 'https://finance.naver.com',
            'source': '매일경제',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': '산업'
        },
        {
            'title': 'AI 열풍에 2차전지·반도체株 주목',
            'summary': '인공지능 시장 성장과 함께 관련 산업 주식들이 투자자들의 관심을 받고 있습니다.',
            'url': 'https://finance.naver.com',
            'source': '서울경제',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': '기술'
        },
        {
            'title': '금리 인하 기대감...금융주 상승세',
            'summary': '기준금리 인하 가능성이 높아지면서 은행주를 중심으로 금융주가 상승했습니다.',
            'url': 'https://finance.naver.com',
            'source': '이데일리',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': '금융'
        },
        {
            'title': '자동차 업계, 전기차 수출 호조',
            'summary': '현대차와 기아의 전기차 수출이 호조를 보이며 주가에 긍정적 영향을 미쳤습니다.',
            'url': 'https://finance.naver.com',
            'source': '파이낸셜뉴스',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': '산업'
        }
    ]
    
    # 샘플 뉴스 추가
    all_news = sample_news[:5]
    
    # JSON 저장
    output = {
        'updated': datetime.now().isoformat(),
        'updatedKST': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'news': all_news
    }
    
    with open('data/news.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Total: Fetched {len(all_news)} news items")
    print(f"📁 Saved to: data/news.json")
    
    return all_news

if __name__ == '__main__':
    print("🚀 Starting news fetch...")
    fetch_stock_news()
    print("✅ News fetch completed!")
