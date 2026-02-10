#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 주식 분석 스크립트
수집된 주가 데이터를 분석하여 안정형/공격형 TOP 10 선정
"""

import json
import os
from datetime import datetime

def analyze_stocks():
    """주가 데이터를 분석하여 안정형/공격형 TOP 10을 선정합니다."""
    
    # stocks.json 읽기
    try:
        with open('data/stocks.json', 'r', encoding='utf-8') as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print("❌ stocks.json 파일을 찾을 수 없습니다!")
        return None
    
    stocks = stock_data['stocks']
    
    # 가격이 0인 종목 제외 (데이터 수집 실패)
    valid_stocks = [s for s in stocks if s['price'] > 0]
    
    print(f"📊 분석 대상: {len(valid_stocks)}개 종목")
    
    # 안정형: 변동성이 낮고 꾸준한 종목
    # 기준: 등락률 ±2.5% 이내, 거래량 적당
    defensive_stocks = []
    for stock in valid_stocks:
        # 안정성 점수 계산
        volatility_score = 100 - abs(stock['changePercent']) * 10  # 변동성 낮을수록 높은 점수
        
        stock_with_score = stock.copy()
        stock_with_score['score'] = volatility_score
        stock_with_score['reason'] = f"안정적인 {abs(stock['changePercent']):.2f}% 변동"
        
        defensive_stocks.append(stock_with_score)
    
    # 안정성 점수 기준 정렬
    defensive_stocks.sort(key=lambda x: x['score'], reverse=True)
    defensive_top10 = defensive_stocks[:10]
    
    print("\n🛡️ 안정형 TOP 10:")
    for i, stock in enumerate(defensive_top10, 1):
        print(f"  {i}. {stock['name']}: {stock['price']:,}원 ({stock['changePercent']:+.2f}%) - 점수: {stock['score']:.1f}")
    
    # 공격형: 높은 수익률 또는 상승 잠재력이 높은 종목
    # 기준: 높은 등락률, 높은 거래량
    aggressive_stocks = []
    for stock in valid_stocks:
        # 공격성 점수 계산
        momentum_score = stock['changePercent'] * 10  # 상승률이 높을수록 높은 점수
        volume_score = min(stock['volume'] / 1000000, 100)  # 거래량 (최대 100점)
        
        total_score = momentum_score + volume_score
        
        stock_with_score = stock.copy()
        stock_with_score['score'] = total_score
        
        if stock['changePercent'] > 0:
            stock_with_score['reason'] = f"강한 상승세 {stock['changePercent']:+.2f}%"
        elif stock['changePercent'] < 0:
            stock_with_score['reason'] = f"반등 기회 {stock['changePercent']:+.2f}%"
        else:
            stock_with_score['reason'] = "보합세 유지"
        
        aggressive_stocks.append(stock_with_score)
    
    # 공격성 점수 기준 정렬
    aggressive_stocks.sort(key=lambda x: x['score'], reverse=True)
    aggressive_top10 = aggressive_stocks[:10]
    
    print("\n⚔️ 공격형 TOP 10:")
    for i, stock in enumerate(aggressive_top10, 1):
        print(f"  {i}. {stock['name']}: {stock['price']:,}원 ({stock['changePercent']:+.2f}%) - 점수: {stock['score']:.1f}")
    
    # 결과 저장
    analysis_result = {
        'analyzed': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'defensive': defensive_top10,
        'aggressive': aggressive_top10,
        'summary': {
            'total_stocks': len(valid_stocks),
            'avg_change': sum(s['changePercent'] for s in valid_stocks) / len(valid_stocks) if valid_stocks else 0,
            'positive_stocks': len([s for s in valid_stocks if s['changePercent'] > 0]),
            'negative_stocks': len([s for s in valid_stocks if s['changePercent'] < 0]),
        }
    }
    
    # JSON 파일로 저장
    with open('data/analysis.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 분석 완료!")
    print(f"   - 평균 등락률: {analysis_result['summary']['avg_change']:+.2f}%")
    print(f"   - 상승 종목: {analysis_result['summary']['positive_stocks']}개")
    print(f"   - 하락 종목: {analysis_result['summary']['negative_stocks']}개")
    
    return analysis_result

if __name__ == '__main__':
    print("🤖 AI 주식 분석 시작...")
    analyze_stocks()
    print("✅ 완료!")
