import streamlit as st
from resume_parser import file_extraction
from utils import text_processing
from similarity import similarity_score
from skill_extractor import skill_database,skill_extraction
from display_skills import display

st.set_page_config(page_title="ATS",layout="wide")
st.header("ATS - Resume Screening and Skill matching system for Data Science and Analytical roles")
st.text("Upload a resume and compare it against a job description to identify skill matches, gaps, and ATS compatibility")

col1,col2=st.columns(2)
#FILE UPLOAD
with col1:
    resume=st.file_uploader(label="**Upload your Resume**", max_upload_size=2, accept_multiple_files=False, type=["pdf","docx"])

    if resume is not None:
        st.write(f"**File uploaded**: {resume.name} ")
        st.success("File Uploaded Successfully", icon="✅")

#RESUME PARSING - TEXT EXTRACTION
        extracted_text=file_extraction(resume)
    #st.subheader("Extracted Text:")
    #st.text(extracted_text)
with col2:
    jd=st.text_area("**Job Description:**")
#st.subheader("JD")
#st.text(jd)

if st.button(label="Analyse",):
    resume_cleaned=text_processing(extracted_text)   
    jd_cleaned=text_processing(jd)

    col1,col2=st.columns(2)

    with col1:
        score=similarity_score(resume_cleaned,jd_cleaned)
        st.subheader(f"🎯 **ATS Similarity Score:** {score:.2f}%" )
        st.progress(score*0.01)

    resume_skills,jd_skills,match,miss=skill_extraction(resume_cleaned, jd_cleaned)

    with col2:
        if len(jd_skills)!=0:
            skill_match_percent=(len(match)/len(jd_skills))*100
            st.subheader(f"📊 **Skill Match Percentage:** {skill_match_percent:.2f}%")
            st.progress(skill_match_percent*0.01)
        else:
            st.write("JD doesn't contain skills matching with database")

    tab1,tab2,tab3,tab4,tab5=st.tabs(["**Resume Skills**","**JD Skills**","**Matching Skills**","**Missing skills**","**Recommended Skills**"])
    with tab1:
        st.subheader("📑 Resume Skills")
        display(resume_skills)
    with tab2:
        st.subheader("📋 JD Skills")
        display(jd_skills)
    with tab3:
        st.subheader(f"✅ Matching Skills: ({len(match)})")
        display(match)
    with tab4:
        st.subheader(f"❌ Missing Skills: ({len(miss)})")
        display(miss)
    with tab5:
        if (len(miss)>0) & (len(miss)<=5):
            st.subheader("⚙️✔️ Recommended skills to learn")
            display(miss)
        elif(len(miss)>5):
            st.subheader("⚙️✔️ Recommended skills to learn")
            for i in miss[:5]:
                st.write("*",i.upper())


    