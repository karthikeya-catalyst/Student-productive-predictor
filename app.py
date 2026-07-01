import streamlit  as st 
import pandas as pd
import joblib

st.set_page_config(
    page_title = "Student productivity predictor",
    page_icon = "🎓",
    layout = "wide"

)
st.title("STUDENT PRODUCTIVITY PREDICTOR")
st.caption("predicts the student productivity score by the Machine learning model ")
st.sidebar.title("About")

st.sidebar.write("""
**Model:** Random Forest Regressor

**Dataset:** Student Productivity Dataset

**Developer:** Thalanki Kartikeya
""")
# load trained ml model
model = joblib.load("notebook/productivity_model.pkl")


# student input details
st.header("Enter Student Details")

study_hours = st.slider(
    "📚 Study Hours Per Day",
    min_value=0.0,
    max_value=12.0,
    value=4.0
)

sleep_hours = st.slider(
    "😴 Sleep Hours Per Night",
    min_value=0.0,
    max_value=12.0,
    value=7.0
)

social_media = st.slider(
    "📱 Social Media Hours",
    min_value=0.0,
    max_value=12.0,
    value=2.0
)

attendance = st.number_input(
    "🏫 Attendance Percentage",
    min_value=0,
    max_value=100,
    step =1,
    value=85
)

assignments = st.number_input(
    "📝 Assignments Completed",
    min_value=0,
    max_value=100,
    step= 5,
    value=80
)

stress = st.slider(
    "😰 Stress Level",
    min_value=1,
    max_value=10,
    value=5
)

physical_activity = st.slider(
    "🏃 Physical Activity Hours Per Week",
    min_value=0.0,
    max_value=20.0,
    value=3.0
)

gpa = st.number_input(
    "🎓 Previous Semester GPA",
    min_value=0.0,
    max_value=10.0,
    step = 0.1,
    value=7.5
)
st.write("")
st.write("")
st.write("")
predict = st.button("🚀 Predict MY Productivity")
if predict:
    
    input_data = {
    "Student_ID": 1,
    "Age": 19,
    "Study_Hours_Per_Day": study_hours,
    "Sleep_Hours_Per_Night": sleep_hours,
    "Screen_Time_Hours": 3,
    "Social_Media_Hours": social_media,
    "Attendance_Percentage": attendance,
    "Assignments_Completed": assignments,
    "Class_Participation_Score": 5,
    "Physical_Activity_Hours_Per_Week": physical_activity,
    "Stress_Level": stress,
    "Motivation_Level": 5,
    "Extracurricular_Involvement": 0,
    "AI_Tool_Usage_Hours_Per_Week": 2,
    "Previous_Semester_GPA": gpa,
    "Gender_Male": False,
    "Gender_Other": False,
    "Internet_Quality_Good": True,
    "Internet_Quality_Poor": False,
    "Part_Time_Job_Yes": False,
    "Performance_Category_Low": False,
    "Performance_Category_Medium": False
}

    input_df =pd.DataFrame([input_data])
    predection =model.predict(input_df)
    score = predection[0]

    st.success("🎯 Prediction Completed!")

    st.metric(
        label="Predicted Productivity Score",
        value=f"{score:.2f}/100"
    )

    st.subheader("💡 Personalized Recommendations")

if study_hours < 4:
    st.write("📚 consider increasing your daily study hours for better productivity.") 

if sleep_hours < 7:
    st.write("😴 aim for 7–8 hours of sleep every night.")

if social_media > 3:
    st.write("📱 Reduce social media usage to may help to improve focous.")

if attendance < 85:
    st.write("🏫 Improve your attendance for better academic performance.")

if assignments < 80:
    st.write("📝 Complete assignments regularly and on time.")

if stress > 7:
    st.write("😌 Your stress level is high. Take regular breaks and manage stress.")

if physical_activity < 3:
    st.write("🏃 Increase your physical activity to stay healthy and focused.")

if gpa < 7:
    st.write("🎓 Focus on improving your GPA through consistent study.")

if (
    study_hours >= 4 and
    sleep_hours >= 7 and
    social_media <= 3 and
    attendance >= 85 and
    assignments >= 80 and
    stress <= 7 and
    physical_activity >= 3 and
    gpa >= 7
):
    st.success("🎉 Excellent! Your habits are well balanced. Keep maintaining this routine.") 

st.markdown("---")

st.caption(
    "Built by Thalanki Kartikeya • Machine Learning Portfolio Project"
)       