import streamlit as st

# 앱 제목 설정
st.title("🔢 세 수 중 가장 큰 수 찾기")

# 설명 글 작성
st.markdown("""
세 개의 정수 중에서 가장 큰 수를 찾으려면 최소 두 번의 비교가 필요합니다.
* 먼저 **a**와 **b**를 비교하여 둘 중 더 큰 값을 찾습니다. (1회 비교)
* 그 다음, 앞에서 찾은 큰 값과 **c**를 비교하여 최종적으로 가장 큰 값을 찾습니다. (1회 비교)
            
따라서 총 두 번의 비교를 통해 가장 큰 수를 알아낼 수 있습니다.
""")

st.divider()  # 구분선

# 기존 input() 부분을 스트림릿의 숫자 입력창(number_input)으로 변경
num1 = st.number_input("첫 번째 정수를 입력하세요 (num1)", value=0, step=1)
num2 = st.number_input("두 번째 정수를 입력하세요 (num2)", value=0, step=1)
num3 = st.number_input("세 번째 정수를 입력하세요 (num3)", value=0, step=1)

# 실행 버튼 (버튼을 누르면 비교 로직이 작동합니다)
if st.button("가장 큰 수 찾기"):
    
    # [원본 로직 유지]
    if num1 > num2:
        if num1 > num3:
            # print(num1) 대신 스트림릿 결과 출력 함수 사용
            st.success(f"가장 큰 수는 **{num1}** 입니다!")
        else:
            st.success(f"가장 큰 수는 **{num3}** 입니다!")
    else:
        if num2 > num3:
            st.success(f"가장 큰 수는 **{num2}** 입니다!")
        else:
            st.success(f"가장 큰 수는 **{num3}** 입니다!")