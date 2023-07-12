from backend import create_app


if __name__ == "__main__":
    app = create_app();
    print("Create app thanh cong")
    app.run(debug=True)