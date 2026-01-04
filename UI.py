import streamlit as st

def render_mcq_card(q_text, options, key=None, card_color=None, current_value=None):
    """
    Renders an MCQ card that remembers the user's selection.
    """
    # Calculate the index of the previously selected option
    default_index = None
    if current_value in options:
        default_index = options.index(current_value)

    with st.container():
        # Styled Question Header
        st.markdown(
            f"""
            <div style="
                background-color: var(--secondary-background-color);
                padding: 16px 20px;
                border-radius: 12px 12px 0px 0px;
                border: 1px solid rgba(128, 128, 128, 0.2);
                border-bottom: none;
                color: var(--text-color);
                font-weight: 600;
            ">
                {q_text}
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Radio buttons container
        st.markdown(
            '<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-top: none; border-radius: 0 0 12px 12px; padding: 10px 20px; margin-bottom: 20px;">', 
            unsafe_allow_html=True
        )
        
        choice = st.radio(
            label=q_text,
            options=options,
            index=default_index, # Uses the saved index instead of None
            key=key,
            label_visibility="collapsed"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
    return choice
