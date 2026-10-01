import streamlit as st

from kanji_converter import (
    grade_kanji,
    load_kanji_reading,
    rewrite_sentence,
)


# -------------------------
# ページ設定
# -------------------------

st.set_page_config(
    page_title="小学生向け漢字変換",
    page_icon="📚",
    layout="centered",
)


# -------------------------
# データ読み込み
# -------------------------

kanji_reading = load_kanji_reading()


# -------------------------
# タイトル
# -------------------------

st.title("小学生向け漢字変換ツール")

st.write(
    "入力した文章を、指定した学年までに習う漢字を使った文章に変換します。"
)


# -------------------------
# 学年選択
# -------------------------

target_grade = st.selectbox(
    "対象学年",
    options=[1, 2, 3, 4, 5, 6],
    format_func=lambda x: f"小学{x}年生",
)


# -------------------------
# 入力
# -------------------------

text = st.text_area(
    "変換する文章",
    height=200,
    placeholder="例：今日は警察へ相談してください。",
)


# -------------------------
# 変換
# -------------------------

if st.button(
    "漢字を変換",
    type="primary",
    use_container_width=True,
):

    if not text.strip():
        st.warning("文章を入力してください。")

    else:

        result = rewrite_sentence(
            text=text,
            target_grade=target_grade,
            grade_kanji=grade_kanji,
            kanji_reading=kanji_reading,
        )

        st.subheader("変換結果")

        st.text_area(
            "結果",
            value=result,
            height=200,
        )