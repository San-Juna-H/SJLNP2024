import streamlit as st

def intro_page():
    '''
    Intro 페이지 구성
    
    실험 설명, 개인정보 수집, 다음 페이지로 이동
    필수 정보를 모두 수집했을 경우에만 다음 페이지로 이동
    
    Args: None
        
    Returns: None
        
    '''
    # 제목
    st.title("🌟 성은준's Last Night Party 🌟")
    st.divider()  # 구분선

    # 실험 설명
    intro_explanation_block()
    
    # 개인정보 수집
    personal_information_block()

    # 제출
    submitted = st.button("제출 및 다음 세션으로 진행 ➡️")
    if submitted:
        # 필수 항목 검증
        user = st.session_state["personal_information"]
        if user["name"] and user["age"] and user["gender"] and user["education_level"]:
            # 성공 및 페이지 이동
            st.success("정보가 성공적으로 제출되었습니다. 다음 세션으로 이동합니다.")
            st.session_state["page"] = "experiment"
            st.rerun()
        else:
            # 오류 메시지 출력
            st.error("모든 필수 항목을 입력해주세요.")

def intro_explanation_block():
    '''
    개요 설명 블록
    
    주어진 텍스트 출력
    
    Args: None
        
    Returns: None
        
    '''
def intro_explanation_block():
    '''
    개요 설명 블록
    
    주어진 텍스트 출력
    
    Args: None
        
    Returns: None
        
    '''
    st.markdown(
        """
        # 🎉 2024년의 마지막 밤, 함께 해요! 🎉

        따뜻한 마음과 즐거운 에너지로 **2024년 마지막 밤**을 보내고자 합니다. 여러분의 참여를 기다리고 있어요!

        ##### 🕒 시간
        **2024년 12월 31일(화) 저녁 7시** ~ **2025년 1월 1일(수) 아침 7시**

        ##### 📍 장소
        **환대**  
        - [홈페이지 링크](https://benetory.kr/hwandae/)  
        - **주소**: 서울특별시 관악구 남부순환로 1848-6, 2층

        ##### 🎤 호스트
        **성은 & 준**

        ##### 🎧 Special Guest
        **DJ & Bartender 형우**

        ##### 〰 TIMELINE 〰

        | 시간           | 일정 내용                        |
        |----------------|----------------------------------|
        | **18:00~19:00** | 도착 (18시부터 열려 있으니 자유롭게 도착) |
        | **19:00~20:00** | 웰컴 디너 (무엇을 먹을지 고민해보세요) |
        | **20:00~21:00** | 2024 버킷 불태우기 🔥 (아쉬움, 미련, 후회를 태우며 새 출발을 다짐) |
        | **21:00~22:00** | 흑백바텐더 🍸 (나만의 2025 시그니처 칵테일 만들기) |
        | **22:00~23:00** | 올해의 GOAT 공연 선정 (최고의 공연을 투표로 뽑고 함께 감상) |
        | **23:00~24:00** | 애장품 교환식 (소중한 물건을 나누며 특별한 추억 만들기) |
        | **🎉 24:00**   | 새해 카운트다운 🎉 (함께 새해를 맞이하기) |
        | **24:00~**     | 즐거운 담소와 함께하는 시간 (새벽 해장 떡국 & 마무리) |

        **새해를 맞이하며 떡국을 나누고, 행복한 시간 보내세요!**
        """,
        unsafe_allow_html=True
    )

def personal_information_block():
    '''    
    개인 정보 수집 블록

    개인 정보 수집 후 st.session_state["personal_information"]에 저장
    이름, 나이, 성별, 최종 학력, 관련 경험 또는 친숙한 분야, 추가 정보
    
    Args: None
        
    Returns: None
        
    '''
    # 개인정보 수집
    container = st.container(border=True)
    user_name = container.text_input("*이름:", placeholder="예: 홍길동")
    user_age = container.number_input("*나이:", min_value=10, max_value=100, value=20)
    user_gender = container.radio("*성별:", ["남성", "여성", "기타"], horizontal=True)
    education_level = container.selectbox(
        "*최종 학력:",
        ["고등학교 졸업", "대학교 졸업", "대학원 석사 졸업", "대학원 박사 졸업"], index=1
    )
    familiar_fields = container.multiselect(
        "관련 경험 또는 친숙한 분야:",
        ["음식과 음료", "공연 예술", "비즈니스와 경제", "정치와 정부", "생물학", "화학", "컴퓨팅", "지구와 환경", "수학", "의학과 건강", "물리학", "공학", "기술"]
    )
    additional_info = container.text_area("추가 정보:", placeholder="본인의 특기 사항이나 취미 등을 입력해주세요.")

    # session_state에 저장
    st.session_state["personal_information"] = {
        "name": user_name,
        "age": user_age,
        "gender": user_gender,
        "education_level": education_level,
        "familiar_fields": familiar_fields,
        "additional_info": additional_info
    }