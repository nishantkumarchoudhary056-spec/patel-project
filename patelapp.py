import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Social Empowerment Scheme Portal",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right,#f8fbff,#eef5ff);
}
h1,h2,h3 {
    color:#0f172a;
}
.card{
    background:white;
    padding:18px;
    border-radius:14px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:12px;
    border-left:6px solid #2563eb;
}
.footer{
    text-align:center;
    padding:15px;
    color:#374151;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
data = {
"Scheme Name":[
"Beti Bachao Beti Padhao",
"PM Awas Yojana",
"PM Kisan Samman Nidhi",
"PM Mudra Yojana",
"Skill India Mission",
"Stand Up India",
"Minority Scholarship",
"SC Student Scholarship",
"Ayushman Bharat",
"Ujjwala Yojana",
"Jan Dhan Yojana",
"Digital India"
],

"Category":[
"Women",
"Housing",
"Farmer",
"Business",
"Youth",
"Employment",
"Minority",
"SC/ST",
"Health",
"Women",
"Banking",
"Technology"
],

"Beneficiaries":[
50,120,200,150,90,30,35,45,180,140,250,100
],

"Year":[
2015,2016,2019,2015,2015,2016,2017,2018,2018,2016,2014,2015
]
}

df = pd.DataFrame(data)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌐 Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Home","Schemes","Eligibility","Updates","Dashboard","About","Team"]
)

# ---------------- HOME ----------------
if page == "Home":

    st.title("🇮🇳 Social Empowerment Scheme Portal")
    st.subheader("Modern Classical Website")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Schemes", len(df))
    c2.metric("Categories", df["Category"].nunique())
    c3.metric("Beneficiaries", f'{df["Beneficiaries"].sum()} Lakhs')

    st.markdown("---")

    st.success("Empowering Citizens Through Government Awareness")

    st.write("""
This portal provides information about schemes for Women, Youth,
Farmers, Minority, Health, Housing and Employment.
""")

# ---------------- SCHEMES ----------------
elif page == "Schemes":

    st.title("📋 Search Schemes")

    search = st.text_input("🔍 Search Scheme Name")

    category = st.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    filtered = df.copy()

    if search:
        filtered = filtered[
            filtered["Scheme Name"].str.contains(search, case=False)
        ]

    if category != "All":
        filtered = filtered[
            filtered["Category"] == category
        ]

    st.write("Results Found:", len(filtered))

    for i, row in filtered.iterrows():

        st.markdown(f"""
        <div class="card">
        <h4>{row['Scheme Name']}</h4>
        Category: {row['Category']} <br>
        Beneficiaries: {row['Beneficiaries']} Lakhs <br>
        Launch Year: {row['Year']}
        </div>
        """, unsafe_allow_html=True)

# ---------------- ELIGIBILITY ----------------
elif page == "Eligibility":

    st.title("✅ Eligibility Checker")

    age = st.slider("Select Age",18,60,22)

    gender = st.selectbox(
        "Gender",
        ["Male","Female","Other"]
    )

    social = st.selectbox(
        "Category",
        ["General","SC/ST","Minority","OBC"]
    )

    if st.button("Check Eligibility"):

        found = False

        if age >= 18:
            st.success("Eligible: Skill India Mission")
            st.success("Eligible: PM Mudra Yojana")
            found = True

        if gender == "Female":
            st.success("Eligible: Beti Bachao Beti Padhao")
            st.success("Eligible: Ujjwala Yojana")
            found = True

        if social == "Minority":
            st.success("Eligible: Minority Scholarship")
            found = True

        if social == "SC/ST":
            st.success("Eligible: SC Student Scholarship")
            found = True

        if found == False:
            st.error("No Eligible Scheme Found")

# ---------------- UPDATES ----------------
elif page == "Updates":

    st.title("📰 Latest Updates")

    st.info("PM Kisan new installment released.")
    st.info("Minority Scholarship forms open now.")
    st.info("Skill India new training batch started.")
    st.info("PM Awas verification process ongoing.")

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":

    st.title("📊 Dashboard")

    fig1 = px.bar(
        df,
        x="Scheme Name",
        y="Beneficiaries",
        color="Category",
        title="Beneficiaries by Scheme"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.pie(
        df,
        names="Category",
        title="Category Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- ABOUT ----------------
elif page == "About":

    st.title("📘 About Project")

    st.write("Project Name: Details of Social Empowerment Scheme of Government")
    st.write("Subject: Data Analysis and Visualization using Python")
    st.write("Branch: Mechanical Engineering")
    st.write("Semester: 2nd Semester")
    st.write("College: Centurion University of Technology and Management")

# ---------------- TEAM ----------------
elif page == "Team":

    st.title("👨‍💻 Team Members")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
Name: Vikash Kumar  
Reg No: 250101160010  
Branch: Mechanical Engineering
""")

    with col2:
        st.success("""
Name: Aashutosh Kumar  
Reg No: 250101160015  
Branch: Mechanical Engineering
""")

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Developed & Handled by Vikash Patel
</div>
""", unsafe_allow_html=True)