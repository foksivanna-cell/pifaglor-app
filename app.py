import streamlit as st
import math

st.set_page_config(page_title="Пифагор", page_icon="📐")
st.title("📐 Калькулятор теоремы Пифагора")
st.write("Введите известные стороны (оставьте неизвестную равной 0).")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Катет a", min_value=0, value=0, step=1)
    b = st.number_input("Катет b", min_value=0, value=0, step=1)
    c = st.number_input("Гипотенуза c", min_value=0, value=0, step=1)

if st.button("Рассчитать", type="primary"):
    st.subheader("Решение")
    
    filled = sum(1 for x in (a, b, c) if x > 0)
    
    if filled != 2:
        st.error("Ошибка! Нужно ввести ровно две стороны больше нуля. Третью оставьте на 0.")
    else:
        # --- ИЩЕМ ГИПОТЕНУЗУ ---
        if c == 0:
            c_sq = a**2 + b**2
            result = math.sqrt(c_sq)
            
            st.write("**Шаг 1.** Запишем теорему Пифагора:")
            st.latex(r"c^2 = a^2 + b^2")
            
            st.write("**Шаг 2.** Подставим известные значения катетов:")
            st.latex(rf"c^2 = {a}^2 + {b}^2")
            
            st.write("**Шаг 3.** Возведем числа в квадрат:")
            st.latex(rf"c^2 = {a**2} + {b**2}")
            
            st.write("**Шаг 4.** Сложим результаты:")
            st.latex(rf"c^2 = {c_sq}")
            
            st.write("**Шаг 5.** Извлечем квадратный корень, чтобы найти c:")
            if result.is_integer():
                st.latex(rf"c = \sqrt{{{c_sq}}} = {int(result)}")
            else:
                st.latex(rf"c = \sqrt{{{c_sq}}} \approx {result:.4f}")
                
            st.success(f"**Ответ: c = {result:.4f}**" if not result.is_integer() else f"**Ответ: c = {int(result)}**")

        # --- ИЩЕМ КАТЕТ A ---
        elif a == 0:
            if c <= b:
                st.error("Ошибка: гипотенуза c должна быть больше катета b!")
            else:
                a_sq = c**2 - b**2
                result = math.sqrt(a_sq)
                
                st.write("**Шаг 1.** Запишем теорему Пифагора:")
                st.latex(r"a^2 + b^2 = c^2")
                
                st.write("**Шаг 2.** Выразим неизвестный катет a:")
                st.latex(r"a^2 = c^2 - b^2")
                
                st.write("**Шаг 3.** Подставим известные значения:")
                st.latex(rf"a^2 = {c}^2 - {b}^2")
                
                st.write("**Шаг 4.** Возведем числа в квадрат:")
                st.latex(rf"a^2 = {c**2} - {b**2}")
                
                st.write("**Шаг 5.** Вычтем:")
                st.latex(rf"a^2 = {a_sq}")
                
                st.write("**Шаг 6.** Извлечем корень:")
                if result.is_integer():
                    st.latex(rf"a = \sqrt{{{a_sq}}} = {int(result)}")
                else:
                    st.latex(rf"a = \sqrt{{{a_sq}}} \approx {result:.4f}")
                    
                st.success(f"**Ответ: a = {result:.4f}**" if not result.is_integer() else f"**Ответ: a = {int(result)}**")

        # --- ИЩЕМ КАТЕТ B ---
        elif b == 0:
            if c <= a:
                st.error("Ошибка: гипотенуза c должна быть больше катета a!")
            else:
                b_sq = c**2 - a**2
                result = math.sqrt(b_sq)
                
                st.write("**Шаг 1.** Запишем теорему Пифагора:")
                st.latex(r"a^2 + b^2 = c^2")
                
                st.write("**Шаг 2.** Выразим неизвестный катет b:")
                st.latex(r"b^2 = c^2 - a^2")
                
                st.write("**Шаг 3.** Подставим известные значения:")
                st.latex(rf"b^2 = {c}^2 - {a}^2")
                
                st.write("**Шаг 4.** Возведем числа в квадрат:")
                st.latex(rf"b^2 = {c**2} - {a**2}")
                
                st.write("**Шаг 5.** Вычтем:")
                st.latex(rf"b^2 = {b_sq}")
                
                st.write("**Шаг 6.** Извлечем корень:")
                if result.is_integer():
                    st.latex(rf"b = \sqrt{{{b_sq}}} = {int(result)}")
                else:
                    st.latex(rf"b = \sqrt{{{b_sq}}} \approx {result:.4f}")
                    
                st.success(f"**Ответ: b = {result:.4f}**" if not result.is_integer() else f"**Ответ: b = {int(result)}**")