#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
뉴스 수집 스크립트
주식 관련 뉴스를 수집하여 JSON으로 저장
"""

import json
import os
from datetime import datetime

def fetch_news():
    """주식 관련 뉴스를 수집합니다."""
    
    # data 폴더 생성
    os.makedirs('data', exist_ok=True)
    
    # 샘플 뉴스 데이터
    # 실제 환경에서는 뉴스 API나 웹 크롤링으로 수집
    news_items = [
        {
            'title': '코스피, 외국인 매수세에 상승 마감',
            'summary': '외국인과 기관의 동반 매수에 코스피가 상승세를 보였습니다.',
            'source': '한국경제',
            'url': 'https://www.hankyung.com',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'title': '삼성전자, 신규 반도체 공장 투자 발표',
            'summary': '삼성전자가 차세대 반도체 생산을 위한 대규모 투자를 발표했습니다.',
            'source': '매일경제',
            'url': 'https://www.mk.co.kr',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'title': 'SK하이닉스, AI 반도체 수요 증가로 실적 개선',
            'summary': 'AI 시장 성장에 따른 HBM 메모리 수요가 급증하고 있습니다.',
            'source': '서울경제',
            'url': 'https://www.sedaily.com',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'title': '2차전지 관련주, 글로벌 수주 소식에 강세',
            'summary': 'LG에너지솔루션과 삼성SDI가 유럽 자동차 업체로부터 대규모 수주를 확보했습니다.',
            'source': '이데일리',
            'url': 'https://www.edaily.co.kr',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'title': '금리 인하 기대감에 증시 훈풍',
            'summary': '한국은행의 금리 인하 가능성이 높아지면서 투자 심리가 개선되고 있습니다.',
            'source': '연합뉴스',
            'url': 'https://www.yna.co.kr',
            'published': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    ]
    
    # 결과 저장
    output_data = {
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'news': news_items
    }
    
    # JSON 파일로 저장
    with open('data/news.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"📰 총 {len(news_items)}개 뉴스 수집 완료!")
    print(f"⏰ 업데이트 시간: {output_data['updated']}")
    
    return output_data

if __name__ == '__main__':
    print("📰 뉴스 수집 시작...")
    fetch_news()
    print("✅ 완료!")
