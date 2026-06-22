
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Food Wastage Management System",
    page_icon="🍲",
    layout="wide"
)

# ---------------------------
# DATABASE CONNECTION
# ---------------------------

engine = create_engine(
    "mysql+pymysql://root:Deekshu%4013@localhost/food_waste"
)

# ---------------------------
# LOAD DATA
# ---------------------------

@st.cache_data
def load_data():
    providers = pd.read_sql("SELECT * FROM providers", engine)
    receivers = pd.read_sql("SELECT * FROM receivers", engine)
    food = pd.read_sql("SELECT * FROM food_listings", engine)
    claims = pd.read_sql("SELECT * FROM claims", engine)

    return providers, receivers, food, claims


providers, receivers, food, claims = load_data()

# ---------------------------
# SIDEBAR
# ---------------------------

menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🏢 Providers",
        "🙋 Receivers",
        "🍛 Food Listings",
        "📦 Claims",
        "➕ Add Provider",
        "❌ Delete Provider",
        "📞 Provider Contacts"
    ]
)

# ---------------------------
# HOME
# ---------------------------

if menu == "🏠 Home":

    st.title("🍲 Local Food Wastage Management System")

    st.info("""
    Connect Food Providers with NGOs and Receivers.

    ✅ Reduce Food Wastage
    ✅ Increase Food Distribution
    ✅ Help Communities
    """)
    st.markdown("""
    ### Reducing Food Waste, Feeding Communities

   The Local Food Wastage Management System is a platform that connects food providers such as restaurants, grocery stores, and supermarkets with NGOs, community centers, and individuals in need.

    The system helps reduce food wastage by enabling providers to donate surplus food and allowing receivers to claim available food efficiently. Through data analysis and real-time tracking, the platform promotes sustainable food distribution and helps combat hunger in local communities.
   """)

# ---------------------------
# DASHBOARD
# ---------------------------

elif menu == "📊 Dashboard":

    st.title("📊 Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Providers", len(providers)) 
    c2.metric("Total Receivers", len(receivers)) 
    c3.metric("Food Listings", len(food)) 
    c4.metric("Total Claims", len(claims))

   

    food["Expiry_Date"] = pd.to_datetime(food["Expiry_Date"])

    expiring = food.sort_values("Expiry_Date").head(20)

    st.divider()

    st.subheader("Food Type Distribution")
    st.bar_chart(food["Food_Type"].value_counts())

    st.subheader("Meal Type Distribution")
    st.bar_chart(food["Meal_Type"].value_counts())

    st.subheader("Claim Status Distribution")
    st.bar_chart(claims["Status"].value_counts())

# ---------------------------
# PROVIDERS
# ---------------------------

elif menu == "🏢 Providers":

    st.title("🏢 Providers")

    city = st.selectbox(
        "Select City",
        ["All"] + list(providers["City"].dropna().unique())
    )

    if city == "All":
        st.dataframe(providers)
    else:
        st.dataframe(
            providers[providers["City"] == city]
        )

# ---------------------------
# RECEIVERS
# ---------------------------

elif menu == "🙋 Receivers":

    st.title("🙋 Receivers")

    st.dataframe(receivers)

# ---------------------------
# FOOD LISTINGS
# ---------------------------

elif menu == "🍛 Food Listings":

    st.title("🍛 Food Listings")

    food_type = st.selectbox(
        "Food Type",
        ["All"] + list(food["Food_Type"].dropna().unique())
    )

    if food_type == "All":
        st.dataframe(food)
    else:
        st.dataframe(
            food[food["Food_Type"] == food_type]
        )

# ---------------------------
# CLAIMS
# ---------------------------

elif menu == "📦 Claims":

    st.title("📦 Claims")

    status = st.selectbox(
        "Claim Status",
        ["All"] + list(claims["Status"].dropna().unique())
    )

    if status == "All":
        st.dataframe(claims)
    else:
        st.dataframe(
            claims[claims["Status"] == status]
        )

# ---------------------------
# ADD PROVIDER
# ---------------------------

elif menu == "➕ Add Provider":

    st.title("➕ Add Provider")

    provider_id = st.number_input(
        "Provider ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Provider Name")
    provider_type = st.text_input("Provider Type")
    address = st.text_area("Address")
    city = st.text_input("City")
    contact = st.text_input("Contact")

    if st.button("Add Provider"):

        query = text("""
        INSERT INTO providers
        (Provider_ID, Name, Type, Address, City, Contact)
        VALUES
        (:id, :name, :type, :address, :city, :contact)
        """)

        with engine.begin() as conn:
            conn.execute(
                query,
                {
                    "id": provider_id,
                    "name": name,
                    "type": provider_type,
                    "address": address,
                    "city": city,
                    "contact": contact
                }
            )

        st.success("✅ Provider Added Successfully")

# ---------------------------
# DELETE PROVIDER
# ---------------------------

elif menu == "❌ Delete Provider":

    st.title("❌ Delete Provider")

    provider_id = st.number_input(
        "Enter Provider ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Provider"):

        query = text("""
        DELETE FROM providers
        WHERE Provider_ID = :id
        """)

        with engine.begin() as conn:
            conn.execute(query, {"id": provider_id})

        st.success("✅ Provider Deleted Successfully")

# ---------------------------
# PROVIDER CONTACTS
# ---------------------------

elif menu == "📞 Provider Contacts":

    st.title("📞 Provider Contacts")

    provider = st.selectbox(
        "Select Provider",
        providers["Provider_ID"]
    )

    info = providers[
        providers["Provider_ID"] == provider
    ]

    st.dataframe(
        info[["Name", "Contact", "City"]]
    )

