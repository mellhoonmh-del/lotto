import random
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎱", layout="centered")

# 세션 상태 초기화 (새로고침해도 기록이 유지되도록 설정)
if "history" not in st.session_state:
  st.session_state.history = []

MAX_SETS = 5


def get_lotto_numbers():
  """1~45 중복 없는 6개 번호 추출 및 정렬"""
  return sorted(random.sample(range(1, 46), 6))


def get_ball_color(number):
  """실제 로또 공 색상 반환"""
  if number <= 10:
    return "#fbc400"
  elif number <= 20:
    return "#69c6f0"
  elif number <= 30:
    return "#ff7272"
  elif number <= 40:
    return "#aaaaaa"
  else:
    return "#b0d840"


# CSS 스타일 적용 (로또 공 디자인 및 레이아웃)
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        background-color: #4a90e2;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #357abd;
        color: white;
    }
    .lotto-row {
        display: flex;
        align-items: center;
        background-color: #ffffff;
        padding: 12px 16px;
        border-radius: 10px;
        border: 1px solid #eeeeee;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .set-label {
        font-weight: bold;
        color: #666666;
        margin-right: 20px;
        min-width: 50px;
    }
    .balls-container {
        display: flex;
        gap: 8px;
    }
    .ball {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 16px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2), 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🎱 로또 번호 생성기")
st.write(
    "버튼을 누르면 실제 로또 공 색상이 반영된 번호가 최대 5세트까지 표시됩니다."
)

# 번호 생성 버튼
if st.button("번호 생성하기"):
  new_numbers = get_lotto_numbers()
  st.session_state.history.insert(0, new_numbers)

  # 최대 5세트만 유지 (6번째 세트부터는 가장 오래된 항목 삭제)
  if len(st.session_state.history) > MAX_SETS:
    st.session_state.history.pop()

# 결과 출력 영역
st.markdown("### 생성된 번호 목록")

if not st.session_state.history:
  st.info("버튼을 눌러 로또 번호를 생성해 보세요!")
else:
  for idx, numbers in enumerate(st.session_state.history):
    balls_html = ""
    for num in numbers:
      color = get_ball_color(num)
      balls_html += f'<div class="ball" style="background-color: {color};">{num}</div>'

    st.markdown(
        f"""
        <div class="lotto-row">
            <div class="set-label">{idx + 1}세트</div>
            <div class="balls-container">{balls_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )