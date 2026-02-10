#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
주가 데이터 수집 스크립트
네이버 금융 API에서 실시간 주가 정보를 가져와 JSON으로 저장
"""

import requests
import json
import time
import os
from datetime import datetime, timezone, timedelta

def safe_int(value):
    """값을 안전하게 int로 변환"""
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value.replace(',', ''))
    return int(value)

def safe_float(value):
    """값을 안전하게 float로 변환"""
    if isinstance(value, float):
        return value
    if isinstance(value, str):
        return float(value.replace(',', ''))
    return float(value)

def fetch_stock_data():
    """주요 종목의 실시간 주가 데이터를 수집합니다."""
    
    # data 폴더 생성
    os.makedirs('data', exist_ok=True)
    
    # 주요 종목 리스트 (코드, 이름)
    stocks = [
        {'code': '005930', 'name': '삼성전자'},
        {'code': '000660', 'name': 'SK하이닉스'},
        {'code': '373220', 'name': 'LG에너지솔루션'},
        {'code': '207940', 'name': '삼성바이오로직스'},
        {'code': '005490', 'name': 'POSCO홀딩스'},
        {'code': '035420', 'name': 'NAVER'},
        {'code': '051910', 'name': 'LG화학'},
        {'code': '006400', 'name': '삼성SDI'},
        {'code': '035720', 'name': '카카오'},
        {'code': '028260', 'name': '삼성물산'},
        {'code': '012330', 'name': '현대모비스'},
        {'code': '066570', 'name': 'LG전자'},
        {'code': '003550', 'name': 'LG'},
        {'code': '017670', 'name': 'SK텔레콤'},
        {'code': '096770', 'name': 'SK이노베이션'},
        {'code': '000270', 'name': '기아'},
        {'code': '005380', 'name': '현대차'},
        {'code': '105560', 'name': 'KB금융'},
        {'code': '055550', 'name': '신한지주'},
        {'code': '086790', 'name': '하나금융지주'},
    ]
    
    results = []
    
    for stock in stocks:
        try:
            # 네이버 금융 API 호출
            url = f"https://polling.finance.naver.com/api/realtime?query=SERVICE_ITEM:{stock['code']}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': 'https://finance.naver.com/'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            
            # 데이터 파싱
            item_data = data['result']['areas'][0]['datas'][0]
            
            stock_info = {
                'code': stock['code'],
                'name': stock['name'],
                'price': safe_int(item_data['nv']),
                'change': safe_int(item_data['cv']),
                'changePercent': safe_float(item_data['rf']),
                'volume': safe_int(item_data['aq']),
                'direction': 'up' if safe_int(item_data['cv']) > 0 else ('down' if safe_int(item_data['cv']) < 0 else 'flat')
            }
            
            results.append(stock_info)
            print(f"✅ {stock['name']}: {stock_info['price']:,}원 ({stock_info['changePercent']:+.2f}%)")
            
            # API 호출 간격 (과도한 요청 방지)
            time.sleep(0.1)
            
        except Exception as e:
            print(f"❌ {stock['name']} 데이터 수집 실패: {str(e)}")
            # 실패 시 기본값 추가
            results.append({
                'code': stock['code'],
                'name': stock['name'],
                'price': 0,
                'change': 0,
                'changePercent': 0.0,
                'volume': 0,
                'direction': 'flat'
            })
    
    # 결과 저장
    output_data = {
        'updated': datetime.now(timezone.utc).isoformat(),
        'updatedKST': (datetime.now(timezone.utc) + timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S'),
        'stocks': results
    }
    
    # JSON 파일로 저장
    with open('data/stocks.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 총 {len(results)}개 종목 데이터 수집 완료!")
    print(f"⏰ 업데이트 시간: {output_data['updatedKST']}")
    
    return output_data

if __name__ == '__main__':
    print("🚀 주가 데이터 수집 시작...")
    fetch_stock_data()
    print("✅ 완료!")
