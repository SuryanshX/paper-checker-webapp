import streamlit as st

# --- Core Logic Functions ---
def calculate_scores(correct, wrong):
    """Calculates scores based on two different systems."""
    score1 = (correct * 2) - (wrong * 0.5)
    score2 = (correct * 1) - (wrong * 0.25)
    return score1, score2

# --- UI and State Management ---
def show_results():
    """Displays the final results in the app."""
    correct = st.session_state.get('correct', 0)
    wrong = st.session_state.get('wrong', 0)
    not_attempted = st.session_state.get('not_attempted', 0)

    score1, score2 = calculate_scores(correct, wrong)
    
    st.markdown("""---""")
    st.subheader("✅ Final Results")
    st.write(f"**Correct Answers:** {correct}")
    st.write(f"**Wrong Answers:** {wrong}")
    st.write(f"**Not Attempted:** {not_attempted}")
    st.write(f"---")
    st.write(f"**SSC (+2, -0.5) → Final Score = {score1}**")
    st.write(f"**UPSSSC PET (+1, -0.25) → Final Score = {score2}**")

def reset_counts():
    """Resets all session state variables to zero."""
    st.session_state.correct = 0
    st.session_state.wrong = 0
    st.session_state.not_attempted = 0
    st.session_state.show_results = False

def increment_count(category):
    """Increments the count for a given category."""
    st.session_state[category] += 1
    # Hide results when a new entry is made
    st.session_state.show_results = False

# --- App Initialization and Layout ---

# Initialize session state variables if they don't exist
if 'correct' not in st.session_state:
    st.session_state.correct = 0
if 'wrong' not in st.session_state:
    st.session_state.wrong = 0
if 'not_attempted' not in st.session_state:
    st.session_state.not_attempted = 0
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

st.set_page_config(page_title="Paper Checker", layout="centered")

st.title("📄 Paper Checker")
st.markdown("Use the buttons below to mark each question.")
st.markdown("""---""")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("✅ Correct", on_click=increment_count, args=('correct',), use_container_width=True)
with col2:
    st.button("❌ Wrong", on_click=increment_count, args=('wrong',), use_container_width=True)
with col3:
    st.button("➖ Not Attempted", on_click=increment_count, args=('not_attempted',), use_container_width=True)

st.markdown("""---""")

st.subheader("Current Count")
st.write(f"Correct: **{st.session_state.correct}**")
st.write(f"Wrong: **{st.session_state.wrong}**")
st.write(f"Not Attempted: **{st.session_state.not_attempted}**")

st.markdown("""---""")

col_final1, col_final2 = st.columns(2)

with col_final1:
    # Use a key to ensure this button is unique
    if st.button("Calculate Final Score", key="calculate_button", use_container_width=True):
        st.session_state.show_results = True

with col_final2:
    # Use a key to ensure this button is unique
    st.button("Reset", on_click=reset_counts, key="reset_button", use_container_width=True)

if st.session_state.show_results:
    show_results()




