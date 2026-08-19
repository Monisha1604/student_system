import streamlit as st
from collections import deque

# ==========================================================
#          STUDENT MANAGEMENT SYSTEM
#          USING QUEUE DATA STRUCTURE
# ==========================================================

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- QUEUE ----------------

if "students" not in st.session_state:
    st.session_state.students = deque()


# ---------------- TITLE ----------------

st.title("🎓 Student Management System")
st.write("### Data Structures Project")
st.info("Main Data Structure Used: Queue | Principle: FIFO (First In, First Out)")


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("📚 Student Management")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "🏠 Home",
        "➕ Add Student",
        "📋 Display Students",
        "✏️ Update Student",
        "🔍 Search Student",
        "🗑️ Delete Student"
    ]
)


# ==========================================================
# HOME
# ==========================================================

if menu == "🏠 Home":

    st.header("Welcome to Student Management System 🎓")

    st.write(
        "This application manages student records using "
        "the **Queue Data Structure**."
    )

    st.write("### Data Structures Used")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Main Data Structure", "Queue")

    with col2:
        st.metric("Queue Principle", "FIFO")

    with col3:
        st.metric(
            "Total Students",
            len(st.session_state.students)
        )

    st.write("---")

    st.subheader("Available Operations")

    col1, col2 = st.columns(2)

    with col1:
        st.write("➕ **Add Student**")
        st.write("📋 **Display Students**")
        st.write("✏️ **Update Student**")

    with col2:
        st.write("🔍 **Search Student**")
        st.write("🗑️ **Delete Student**")

    st.write("---")

    st.subheader("Queue Representation")

    if len(st.session_state.students) == 0:

        st.warning("Queue is empty.")

    else:

        queue_text = "FRONT → "

        for student in st.session_state.students:

            queue_text += (
                "[" +
                str(student["ID"]) +
                " - " +
                student["Name"] +
                "] → "
            )

        queue_text += "REAR"

        st.success(queue_text)


# ==========================================================
# ADD STUDENT
# ==========================================================

elif menu == "➕ Add Student":

    st.header("➕ Add Student")

    st.write("Add a new student to the Queue.")

    student_id = st.text_input("Student ID")

    name = st.text_input("Student Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=18
    )

    department = st.selectbox(
        "Department",
        [
            "Computer Science and Engineering",
            "Artificial Intelligence and Machine Learning",
            "Information Technology",
            "Electronics and Communication Engineering",
            "Electrical and Electronics Engineering",
            "Mechanical Engineering",
            "Civil Engineering"
        ]
    )

    marks = st.number_input(
        "Marks",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    if st.button("➕ Add Student", use_container_width=True):

        if student_id == "" or name == "":

            st.error("Please enter Student ID and Name.")

        else:

            # Check duplicate ID
            duplicate = False

            for student in st.session_state.students:

                if student["ID"] == student_id:
                    duplicate = True
                    break

            if duplicate:

                st.error("Student ID already exists!")

            else:

                student = {
                    "ID": student_id,
                    "Name": name,
                    "Age": age,
                    "Department": department,
                    "Marks": marks
                }

                # ENQUEUE
                st.session_state.students.append(student)

                st.success(
                    "Student added successfully! ✅"
                )

                st.write("Data Structure Operation: **ENQUEUE**")


# ==========================================================
# DISPLAY STUDENTS
# ==========================================================

elif menu == "📋 Display Students":

    st.header("📋 Student Records")

    if len(st.session_state.students) == 0:

        st.warning("No student records available.")

    else:

        students = list(st.session_state.students)

        st.dataframe(
            students,
            use_container_width=True,
            hide_index=True
        )

        st.write(
            "Total Students:",
            len(st.session_state.students)
        )


# ==========================================================
# UPDATE STUDENT
# ==========================================================

elif menu == "✏️ Update Student":

    st.header("✏️ Update Student")

    if len(st.session_state.students) == 0:

        st.warning("No student records available.")

    else:

        update_id = st.text_input(
            "Enter Student ID to Update"
        )

        if st.button("Find Student", use_container_width=True):

            found = None

            for student in st.session_state.students:

                if student["ID"] == update_id:
                    found = student
                    break

            if found:

                st.session_state.update_student = found
                st.success("Student found! Scroll down to update.")

            else:

                st.error("Student not found.")

        if "update_student" in st.session_state:

            student = st.session_state.update_student

            st.write("### Update Details")

            new_name = st.text_input(
                "Name",
                value=student["Name"]
            )

            new_age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=int(student["Age"])
            )

            departments = [
                "Computer Science and Engineering",
                "Artificial Intelligence and Machine Learning",
                "Information Technology",
                "Electronics and Communication Engineering",
                "Electrical and Electronics Engineering",
                "Mechanical Engineering",
                "Civil Engineering"
            ]

            current_department = student["Department"]

            department_index = (
                departments.index(current_department)
                if current_department in departments
                else 0
            )

            new_department = st.selectbox(
                "Department",
                departments,
                index=department_index
            )

            new_marks = st.number_input(
                "Marks",
                min_value=0.0,
                max_value=100.0,
                value=float(student["Marks"])
            )

            if st.button(
                "💾 Update Student",
                use_container_width=True
            ):

                student["Name"] = new_name
                student["Age"] = new_age
                student["Department"] = new_department
                student["Marks"] = new_marks

                st.success(
                    "Student details updated successfully! ✅"
                )

                del st.session_state.update_student


# ==========================================================
# SEARCH STUDENT
# ==========================================================

elif menu == "🔍 Search Student":

    st.header("🔍 Search Student")

    search_id = st.text_input(
        "Enter Student ID"
    )

    if st.button(
        "🔍 Search",
        use_container_width=True
    ):

        found = None

        for student in st.session_state.students:

            if student["ID"] == search_id:

                found = student
                break

        if found:

            st.success("Student Found! ✅")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Student ID:**", found["ID"])
                st.write("**Name:**", found["Name"])
                st.write("**Age:**", found["Age"])

            with col2:

                st.write(
                    "**Department:**",
                    found["Department"]
                )

                st.write(
                    "**Marks:**",
                    found["Marks"]
                )

        else:

            st.error("Student not found ❌")


# ==========================================================
# DELETE STUDENT
# ==========================================================

elif menu == "🗑️ Delete Student":

    st.header("🗑️ Delete Student")

    if len(st.session_state.students) == 0:

        st.warning("No student records available.")

    else:

        delete_id = st.text_input(
            "Enter Student ID to Delete"
        )

        if st.button(
            "🗑️ Delete Student",
            use_container_width=True
        ):

            found = False

            new_queue = deque()

            for student in st.session_state.students:

                if student["ID"] == delete_id:

                    found = True

                else:

                    new_queue.append(student)

            if found:

                st.session_state.students = new_queue

                st.success(
                    "Student deleted successfully! ✅"
                )

            else:

                st.error("Student not found ❌")