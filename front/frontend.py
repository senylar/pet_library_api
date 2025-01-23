import streamlit as st
import requests

API_BASE_URL = "https://3196439-cd71947.twc1.net"  # Базовый URL вашего API

st.set_page_config(page_title="Library Management", layout="centered", page_icon="📚")


st.title("📚 Library Management System")
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Choose an action:", ["Books", "Issues", "Readers"])


def fetch_data(endpoint):
    response = requests.get(f"{API_BASE_URL}{endpoint}")
    return response.json() if response.status_code == 200 else None

def post_data(endpoint, data):
    response = requests.post(f"{API_BASE_URL}{endpoint}", json=data)
    return response.json() if response.status_code == 200 else None

def put_data(endpoint, data):
    response = requests.put(f"{API_BASE_URL}{endpoint}", json=data)
    return response.json() if response.status_code == 200 else None

def delete_data(endpoint):
    response = requests.delete(f"{API_BASE_URL}{endpoint}")
    return response.status_code == 200


if menu == "Books":
    st.subheader("Manage Books")

    tab1, tab2, tab3 = st.tabs(["View All Books", "Add a Book", "Update/Delete a Book"])

    with tab1:
        st.write("### List of Books")
        books = fetch_data("/books/")
        if books:
            for book in books:
                st.write(f"**Title:** {book['title']} | **Author:** {book['author']} | **ID:** {book['id']}")
        else:
            st.error("No books found.")

    with tab2:
        st.write("### Add a New Book")
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year of Publication", min_value=0, format="%d")

        if st.button("Add Book"):
            new_book = {"title": title, "author": author, "year": year}
            response = post_data("/books/", new_book)
            if response:
                st.success(f"Book added successfully! (ID: {response['id']})")
            else:
                st.error("Failed to add book.")

    with tab3:
        st.write("### Update or Delete a Book")
        book_id = st.number_input("Enter Book ID", min_value=1, step=1, format="%d")

        col1, col2 = st.columns(2)
        with col1:
            updated_title = st.text_input("Updated Title")
            updated_author = st.text_input("Updated Author")
            updated_year = st.number_input("Updated Year", min_value=0, format="%d")

            if st.button("Update Book"):
                update_data = {"title": updated_title, "author": updated_author, "year": updated_year}
                response = put_data(f"/books/{book_id}", update_data)
                if response:
                    st.success("Book updated successfully!")
                else:
                    st.error("Failed to update book.")
        with col2:
            if st.button("Delete Book"):
                if delete_data(f"/books/{book_id}"):
                    st.success("Book deleted successfully!")
                else:
                    st.error("Failed to delete book.")

if menu == "Issues":
    st.subheader("Manage Issues")

    tab1, tab2, tab3 = st.tabs(["View All Issues", "Add an Issue", "Close/Delete an Issue"])

    with tab1:
        st.write("### List of Issues")
        issues = fetch_data("/issues/")
        if issues:
            for issue in issues:
                st.write(f"**Issue ID:** {issue['id']} | **Book ID:** {issue['book_id']} | **Reader ID:** {issue['reader_id']}")
        else:
            st.error("No issues found.")

    with tab2:
        st.write("### Add a New Issue")
        book_id = st.number_input("Book ID", min_value=1, step=1)
        reader_id = st.number_input("Reader ID", min_value=1, step=1)

        if st.button("Add Issue"):
            new_issue = {"book_id": book_id, "reader_id": reader_id}
            response = post_data("/issues/", new_issue)
            if response:
                st.success(f"Issue created successfully! (ID: {response['id']})")
            else:
                st.error("Failed to create issue.")

    with tab3:
        st.write("### Close/Delete an Issue")
        issue_id = st.number_input("Enter Issue ID", min_value=1, step=1)

        if st.button("Close Issue"):
            if delete_data(f"/issues/{issue_id}"):
                st.success("Issue closed successfully!")
            else:
                st.error("Failed to close issue.")

if menu == "Readers":
    st.subheader("Manage Readers")

    tab1, tab2, tab3 = st.tabs(["View All Readers", "Add a Reader", "Update/Delete a Reader"])

    with tab1:
        st.write("### List of Readers")
        readers = fetch_data("/readers/")
        if readers:
            for reader in readers:
                st.write(f"**Name:** {reader['name']} | **ID:** {reader['id']}")
        else:
            st.error("No readers found.")

    with tab2:
        st.write("### Add a New Reader")
        name = st.text_input("Reader's Name")

        if st.button("Add Reader"):
            new_reader = {"name": name}
            response = post_data("/readers/", new_reader)
            if response:
                st.success(f"Reader added successfully! (ID: {response['id']})")
            else:
                st.error("Failed to add reader.")

    with tab3:
        st.write("### Update or Delete a Reader")
        reader_id = st.number_input("Enter Reader ID", min_value=1, step=1)

        col1, col2 = st.columns(2)
        with col1:
            updated_name = st.text_input("Updated Name")

            if st.button("Update Reader"):
                update_data = {"name": updated_name}
                response = put_data(f"/readers/{reader_id}", update_data)
                if response:
                    st.success("Reader updated successfully!")
                else:
                    st.error("Failed to update reader.")
        with col2:
            if st.button("Delete Reader"):
                if delete_data(f"/readers/{reader_id}"):
                    st.success("Reader deleted successfully!")
                else:
                    st.error("Failed to delete reader.")