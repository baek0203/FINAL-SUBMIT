import streamlit as st
from model import predict

# Streamlit 애플리케이션 설정
st.title("비만도 진단")

# 성별 선택 라디오 버튼 추가
gender_option = st.radio('성별을 선택하세요', ('남성', '여성'))
Gender = 1 if gender_option == '남성' else 0  # Assuming Gender is binary in your model

# 사용자로부터 나이, 키, 몸무게 입력 받기
age = st.number_input('나이', min_value=0, max_value=120, value=25)
height = st.number_input('키 (cm)', min_value=0, max_value=250, value=170)
weight = st.number_input('몸무게 (kg)', min_value=0, max_value=200, value=70)

# 추가 질문
family_history = st.radio('과체중이나 비만을 겪은 가족원이 있나요?', ('예', '아니오'))
high_calorie_food = st.radio('고칼로리 음식을 빈번하게 먹나요?', ('예', '아니오'))
vegetable_intake = st.radio('식사할 때 보통 야채를 먹나요?', ('그렇지 않다', '가끔', '항상'))
meal_frequency = st.radio('하루에 식사를 몇 번 하나요?', ('1~2번', '3번', '3번 이상'))
snacking_frequency = st.radio('식사 사이에 음식을 얼마나 섭취하나요?', ('하지 않음', '가끔', '자주', '항상'))
water_intake = st.radio('하루에 물을 얼마나 마시나요?', ('1L 미만', '1~2L', '2L 이상'))
calorie_check = st.radio('매일 섭취한 칼로리를 확인하나요?', ('예', '아니오'))
physical_activity = st.radio('신체 활동(운동)을 얼마나 자주 하나요?', ('하지 않음', '1~2일', '2~4일', '4~5일'))
screen_time = st.radio('스마트폰, 비디오게임, TV, 컴퓨터 등의 전자기기를 얼마나 사용하나요?', ('0~2시간', '3~5시간', '5시간 이상'))
alcohol_consumption = st.radio('술을 얼마나 자주 마시나요?', ('마시지 않음', '가끔', '자주', '매일'))
transportation_mode = st.radio('어떤 교통수단을 주로 사용하나요?', ('자가용', '오토바이', '자전거', '대중교통', '도보'))

# 입력된 데이터를 저장하고 예측 수행
if st.button('제출'):
    data = {
        'Gender': Gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'family_history_with_overweight': 1 if family_history == '예' else 0,
        'FAVC': 1 if high_calorie_food == '예' else 0,
        'FCVC': 2.0 if vegetable_intake == '항상' else (1.0 if vegetable_intake == '가끔' else 0.0),
        'NCP': 3.0 if meal_frequency == '3번 이상' else (2.0 if meal_frequency == '3번' else 1.0),
        'CAEC': snacking_frequency,
        'SMOKE': 0,
        'CH2O': 2.0 if water_intake == '2L 이상' else (1.0 if water_intake == '1~2L' else 0.0),
        'SCC': 1 if calorie_check == '예' else 0,
        'FAF': physical_activity,
        'TUE': screen_time,
        'CALC': alcohol_consumption,
        'MTRANS': transportation_mode
    }

    prediction = predict(data)
    st.subheader("예측 결과")
    st.write(f"예측된 비만도 수준: {prediction[0]}")

# Run the Streamlit app using the command: streamlit run main.py
