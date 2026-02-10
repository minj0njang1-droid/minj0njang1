#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
주가 데이터 수집 스크립트
네이버 금융에서 실시간 주가 정보를 가져옵니다.
"""

import requests
import json
from datetime import datetime
import time

def fetch_stock_data():
    """네이버 금융에서 주가 데이터 수집"""
    
    # 주요 종목 코드
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
        {'code': '086790', 'name': '하나금융지주'}
    ]
    
    results = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://finance.naver.com/'
    }
    
    for stock in stocks:
        try:
            # 네이버 금융 시세 API
            url = f"https://polling.finance.naver.com/api/realtime?query=SERVICE_ITEM:{stock['code']}"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('result') and data['result'].get('areas'):
                    item = data['result']['areas'][0]['datas'][0]
                    
                    # 가격 정보
                    current_price = int(item.get('nv', 0))
                    change_price = int(item.get('cv', 0))
                    change_percent = float(item.get('rf', 0))
                    volume = int(item.get('aq', 0))
                    
                    results.append({
                        'code': stock['code'],
                        'name': stock['name'],
                        'price': current_price,
                        'change': change_price,
                        'changePercent': change_percent,
                        'volume': volume,
                        'direction': 'up' if change_price > 0 else 'down' if change_price < 0 else 'flat'
                    })
                    
                    print(f"✅ {stock['name']}: {current_price:,}원 ({change_percent:+.2f}%)")
            
            time.sleep(0.1)  # API 과부하 방지
            
        except Exception as e:
            print(f"❌ Error fetching {stock['name']}: {e}")
            # 에러 시 기본값
            results.append({
                'code': stock['code'],
                'name': stock['name'],
                'price': 0,
                'change': 0,
                'changePercent': 0,
                'volume': 0,
                'direction': 'flat'
            })
    
    # JSON 저장
    output = {
        'updated': datetime.now().isoformat(),
        'updatedKST': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'stocks': results
    }
    
    with open('data/stocks.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Total: Fetched {len(results)} stocks")
    print(f"📁 Saved to: data/stocks.json")
    
    return results

if __name__ == '__main__':
    print("🚀 Starting stock data fetch...")
    fetch_stock_data()
    print("✅ Stock data fetch completed!")
