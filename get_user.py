import requests

def test_user_service():
    base_url = "https://petstore.swagger.io/v2/user"
    test_results = []

    for user_id in range(100):
        response = requests.get(f"{base_url}/{user_id}")
        if response.status_code == 200:
            test_results.append(f"User ID {user_id}: Passed (200 OK)")
        elif response.status_code == 404:
            test_results.append(f"User ID {user_id}: Passed (404 Not Found)")
        else:
            test_results.append(f"User ID {user_id}: Failed ({response.status_code})")

    with open("user_test_results.txt", "w") as file:
        file.write("\n".join(test_results))

if __name__ == "__main__":
    test_user_service()
