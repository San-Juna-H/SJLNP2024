import streamlit as st
from datetime import time
import save

def intro_page():
    '''
    Intro 페이지 구성
    
    실험 설명, 개인정보 수집, 다음 페이지로 이동
    필수 정보를 모두 수집했을 경우에만 다음 페이지로 이동
    
    Args: None
        
    Returns: None
        
    '''
    # 제목 중앙 정렬
    st.snow()  # 애니메이션 효과
    st.markdown(
        """
        <h1 style="text-align: center;">🌟 성은준's Last Night Party 🌟</h1>
        """,
        unsafe_allow_html=True
    )

    # 내용 중앙 정렬
    st.markdown(
        """
        <h3 style="text-align: center;">🎉 2024년의 마지막 밤, 함께 해요! 🎉</h3>
        <p style="text-align: center;">따뜻한 마음과 즐거운 에너지로 <strong>2024년 마지막 밤</strong>을 보내고자 합니다. 여러분의 참여를 기다리고 있어요!</p>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()  # 구분선

    # 실험 설명
    intro_explanation_block()
    
    # 개인정보 수집
    personal_information_block()

    # 제출
    submitted = st.button("🥳 제출 🥳")

    if submitted:
        # 필수 항목 검증
        user = st.session_state["personal_information"]
        if user["name"] and user["arrival_time"]:
            # 성공 및 페이지 이동
            st.success("정보가 성공적으로 제출되었습니다! 파티에서 만나요!")
            st.balloons()  # 애니메이션 효과

            responses = process_response()
            save.record_to_sheets(responses)

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
    st.markdown(
        """
        ##### 🕒 시간
        **2024년 12월 31일(화) 저녁 7시** ~ **2025년 1월 1일(수) 아침 7시**
        
        ##### 📍 장소
        **환대**  
        - [홈페이지 링크](https://benetory.kr/hwandae/)  
        - **주소**: 서울특별시 관악구 남부순환로 1848-6, 2층
        
        ##### 🎤 호스트
        **성은 & 준**

        ##### 💰 참가비
        - **참가비: 6만원**
        - 파티의 원활한 진행을 위한 대관비, 식사 및 주류 구매 비용입니다.
        - 입금 계좌: 카카오뱅크 3333-08-8659620 지준
        
        ##### 🎧 Special Guest
        **DJ & Bartender 김형우**
        
        ##### 〰 TIMELINE 〰

        | 시간           | 일정 내용                        |
        |----------------|----------------------------------|
        | **19:00~19:30** | 도착 |
        | **19:30~20:30** | 웰컴 디너 🥗🐓🍲 |
        | **20:30~22:00** | 흑백바텐더 🍸 (feat. 고죠 김형우)\* |
        | **22:00~23:00** | 올해의 GOAT 공연 선정 및 감상 |
        | **23:00~24:00** | 애장품 교환식\** |
        | **🎉 24:00 🎉**   | **🎉 새해 카운트다운 🎉** |
        | **24:00~**     | 새벽 해장 떡국 |

        \* 흑백 바텐더에 사용하고 싶은 술 및 음료 등은 자유롭게 지참 가능\n
        \** 애장품 교환식을 위한 애장품 지참 **필수**   
        (**구매 불가.** 단, 포장 - 박스, 쇼핑백 등에 한해 구매 가능. 미스터리한 포장으로 💕**두근두근**💕 레벨 업!)
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
    user_tel = container.text_input("*연락처:", placeholder="예: 010-1234-5678")
    arrival_time = container.time_input("*도착 시간을 선택하세요:", value=time(19, 0))
    additional_info = container.text_area("추가 정보:", placeholder="호스트에게 하고 싶은 말이 있다면 자유롭게 적어주세요!")

    # session_state에 저장
    st.session_state["personal_information"] = {
        "name": user_name,
        "tel": str(user_tel),
        "arrival_time": str(arrival_time),
        "additional_info": additional_info,
    }

def process_response():
    responses = []
    
    # personal_information에서 각 값을 꺼내서 responses에 추가
    responses.append(st.session_state["personal_information"]['name'])
    responses.append(st.session_state["personal_information"]['tel'])
    responses.append(st.session_state["personal_information"]['arrival_time'])
    responses.append(st.session_state["personal_information"]['additional_info'])

    return responses